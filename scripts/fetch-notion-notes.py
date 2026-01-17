#!/usr/bin/env python3
"""
Fetch technical notes from Notion and convert to Hugo markdown.

This script:
1. Fetches all published notes from Notion database
2. Converts Notion blocks to markdown (preserving structure verbatim)
3. Downloads images to Hugo static directory
4. Generates Hugo frontmatter with SEO metadata

Usage:
    python scripts/fetch-notion-notes.py

Environment variables required:
    NOTION_API_KEY: Your Notion integration token
    NOTION_DATABASE_ID: ID of your Technical Notes database
"""

import os
import sys
import requests
import json
import base64
from pathlib import Path
from datetime import datetime
from urllib.parse import urlparse

# Configuration
NOTION_API_KEY = os.environ.get('NOTION_API_KEY')
NOTION_DATABASE_ID = os.environ.get('NOTION_DATABASE_ID')
NOTION_VERSION = '2022-06-28'
CONTENT_DIR = Path(__file__).parent.parent / 'content' / 'notes'
STATIC_DIR = Path(__file__).parent.parent / 'static' / 'images' / 'notes'

# Notion API headers
HEADERS = {
    'Authorization': f'Bearer {NOTION_API_KEY}',
    'Notion-Version': NOTION_VERSION,
    'Content-Type': 'application/json'
}


def check_environment():
    """Verify required environment variables are set."""
    if not NOTION_API_KEY:
        print("ERROR: NOTION_API_KEY environment variable not set")
        print("Get your key from: https://www.notion.so/my-integrations")
        sys.exit(1)

    if not NOTION_DATABASE_ID:
        print("ERROR: NOTION_DATABASE_ID environment variable not set")
        print("Find it in your database URL: notion.so/username/<DATABASE_ID>?v=...")
        sys.exit(1)

    print(f"✓ Environment variables configured")


def query_database():
    """Fetch all published notes from Notion database."""
    url = f'https://api.notion.com/v1/databases/{NOTION_DATABASE_ID}/query'

    # Filter for only published notes
    payload = {
        'filter': {
            'property': 'Status',
            'select': {
                'equals': 'Published'
            }
        },
        'sorts': [
            {
                'property': 'Date',
                'direction': 'descending'
            }
        ]
    }

    response = requests.post(url, headers=HEADERS, json=payload)

    if response.status_code != 200:
        print(f"ERROR: Failed to query database: {response.text}")
        sys.exit(1)

    results = response.json()['results']
    print(f"✓ Found {len(results)} published notes")
    return results


def get_page_content(page_id):
    """Fetch all blocks (content) from a Notion page."""
    url = f'https://api.notion.com/v1/blocks/{page_id}/children'

    all_blocks = []
    has_more = True
    start_cursor = None

    while has_more:
        params = {}
        if start_cursor:
            params['start_cursor'] = start_cursor

        response = requests.get(url, headers=HEADERS, params=params)

        if response.status_code != 200:
            print(f"ERROR: Failed to fetch page content: {response.text}")
            return []

        data = response.json()
        all_blocks.extend(data['results'])
        has_more = data['has_more']
        start_cursor = data.get('next_cursor')

    return all_blocks


def download_image(image_url, slug, image_filename):
    """Download image from Notion CDN or decode base64 data URL to Hugo static directory."""
    # Create directory for this note's images
    note_images_dir = STATIC_DIR / slug
    note_images_dir.mkdir(parents=True, exist_ok=True)

    image_path = note_images_dir / image_filename

    # Check if it's a data URL (base64 encoded inline image)
    if image_url.startswith('data:'):
        try:
            # Extract base64 data after the comma
            header, data = image_url.split(',', 1)
            image_data = base64.b64decode(data)
            with open(image_path, 'wb') as f:
                f.write(image_data)
            return f'/images/notes/{slug}/{image_filename}'
        except Exception as e:
            print(f"ERROR: Failed to decode base64 image: {e}")
            return None
    else:
        # Handle HTTP/HTTPS URLs (regular Notion CDN images)
        response = requests.get(image_url)
        if response.status_code == 200:
            with open(image_path, 'wb') as f:
                f.write(response.content)
            return f'/images/notes/{slug}/{image_filename}'

    return None


def extract_rich_text(rich_text_array):
    """Extract plain text from Notion rich text array, preserving annotations."""
    if not rich_text_array:
        return ''

    text = ''
    for item in rich_text_array:
        content = item['text']['content']
        annotations = item['annotations']

        # Apply markdown formatting based on annotations
        if annotations['bold']:
            content = f'**{content}**'
        if annotations['italic']:
            content = f'*{content}*'
        if annotations['code']:
            content = f'`{content}`'

        text += content

    return text


def block_to_markdown(block, slug, image_counter):
    """Convert a Notion block to markdown, preserving structure verbatim."""
    block_type = block['type']
    markdown = ''

    if block_type == 'paragraph':
        text = extract_rich_text(block['paragraph']['rich_text'])
        markdown = f'{text}\n\n'

    elif block_type == 'heading_1':
        text = extract_rich_text(block['heading_1']['rich_text'])
        markdown = f'# {text}\n\n'

    elif block_type == 'heading_2':
        text = extract_rich_text(block['heading_2']['rich_text'])
        markdown = f'## {text}\n\n'

    elif block_type == 'heading_3':
        text = extract_rich_text(block['heading_3']['rich_text'])
        markdown = f'### {text}\n\n'

    elif block_type == 'bulleted_list_item':
        text = extract_rich_text(block['bulleted_list_item']['rich_text'])
        markdown = f'- {text}\n'

    elif block_type == 'numbered_list_item':
        text = extract_rich_text(block['numbered_list_item']['rich_text'])
        markdown = f'1. {text}\n'

    elif block_type == 'code':
        code = extract_rich_text(block['code']['rich_text'])
        language = block['code']['language']
        markdown = f'```{language}\n{code}\n```\n\n'

    elif block_type == 'quote':
        text = extract_rich_text(block['quote']['rich_text'])
        markdown = f'> {text}\n\n'

    elif block_type == 'image':
        image_data = block['image']

        # Get image URL (external or uploaded)
        if image_data['type'] == 'external':
            image_url = image_data['external']['url']
        else:
            image_url = image_data['file']['url']

        # Download image and get local path
        image_filename = f'image-{image_counter[0]}.png'
        local_path = download_image(image_url, slug, image_filename)

        if local_path:
            # Get caption if exists
            caption = extract_rich_text(image_data.get('caption', []))
            if caption:
                markdown = f'![{caption}]({local_path})\n\n'
            else:
                markdown = f'![]({local_path})\n\n'
            image_counter[0] += 1

    elif block_type == 'divider':
        markdown = '---\n\n'

    elif block_type == 'table':
        # Tables require fetching child rows
        # For now, add placeholder (can enhance later)
        markdown = '\n*[Table content - requires manual formatting]*\n\n'

    elif block_type == 'callout':
        text = extract_rich_text(block['callout']['rich_text'])
        markdown = f'> **Note:** {text}\n\n'

    return markdown


def convert_page_to_markdown(page, blocks):
    """Convert Notion page and blocks to Hugo markdown file."""
    properties = page['properties']

    # Extract metadata
    title = extract_rich_text(properties['Title']['title'])
    slug = properties['Slug']['rich_text'][0]['text']['content'] if properties['Slug']['rich_text'] else ''
    paper_url = properties['Paper URL']['url'] if properties['Paper URL'].get('url') else ''
    date = properties['Date']['date']['start'] if properties['Date'].get('date') else datetime.now().strftime('%Y-%m-%d')
    tags = [tag['name'] for tag in properties['Tags']['multi_select']]
    category = properties['Category']['select']['name'] if properties['Category'].get('select') else 'paper-notes'

    # Generate Hugo frontmatter
    frontmatter = f"""---
title: "{title}"
date: {date}
draft: false
tags: {json.dumps(tags)}
categories: ["{category}"]
ShowToc: true
TocOpen: true
weight: 1
---

**Paper:** [{title}]({paper_url})

---

"""

    # Convert blocks to markdown
    content = ''
    image_counter = [1]  # Mutable counter for images

    for block in blocks:
        content += block_to_markdown(block, slug, image_counter)

    # Add footer
    footer = f"""
---

**Paper Link:** {paper_url}

---

*Last updated: {datetime.now().strftime('%B %d, %Y')}*

*Questions or discussion? [Email me](mailto:sethi.hemant@gmail.com)*
"""

    full_content = frontmatter + content + footer

    # Write to Hugo content directory
    note_dir = CONTENT_DIR / slug
    note_dir.mkdir(parents=True, exist_ok=True)

    output_file = note_dir / 'index.md'
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(full_content)

    print(f"  ✓ Generated: {output_file}")
    return slug


def main():
    """Main execution flow."""
    print("Starting Notion → Hugo sync...\n")

    # Step 1: Check environment
    check_environment()

    # Step 2: Create directories if needed
    CONTENT_DIR.mkdir(parents=True, exist_ok=True)
    STATIC_DIR.mkdir(parents=True, exist_ok=True)

    # Step 3: Query Notion database
    pages = query_database()

    if not pages:
        print("No published notes found. Mark notes as 'Published' in Notion.")
        sys.exit(0)

    # Step 4: Convert each page
    print("\nConverting pages to Hugo markdown...\n")
    converted_slugs = []

    for page in pages:
        page_id = page['id']
        title = extract_rich_text(page['properties']['Title']['title'])

        print(f"Processing: {title}")

        # Fetch page content
        blocks = get_page_content(page_id)

        # Convert to markdown
        slug = convert_page_to_markdown(page, blocks)
        converted_slugs.append(slug)

    print(f"\n✓ Successfully converted {len(converted_slugs)} notes")
    print(f"✓ Notes written to: {CONTENT_DIR}")
    print(f"✓ Images saved to: {STATIC_DIR}")
    print("\nRun 'hugo server' to preview changes locally.")


if __name__ == '__main__':
    main()
