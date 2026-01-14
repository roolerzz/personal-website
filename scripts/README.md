# Scripts Directory

This directory contains automation scripts for managing your Hugo website.

## Notion Integration Scripts

### `fetch-notion-notes.py`

Fetches technical notes from Notion and converts them to Hugo markdown format.

**Features:**
- Fetches all "Published" notes from Notion database
- Converts Notion blocks to markdown (preserving structure verbatim)
- Downloads images from Notion CDN to local static directory
- Generates Hugo frontmatter with SEO metadata
- Adds citation information (BibTeX, APA)

**Usage:**
```bash
# Set environment variables
export NOTION_API_KEY="secret_..."
export NOTION_DATABASE_ID="..."

# Run script
python3 scripts/fetch-notion-notes.py
```

**Output:**
- Markdown files: `content/notes/<slug>/index.md`
- Images: `static/images/notes/<slug>/image-*.png`

### `sync-notion.sh`

Convenience wrapper around `fetch-notion-notes.py`.

**Usage:**
```bash
./scripts/sync-notion.sh
```

Checks environment variables and runs the Python script.

### `requirements.txt`

Python dependencies for Notion integration.

**Installation:**
```bash
pip3 install -r scripts/requirements.txt
```

## Environment Variables

Set these in your environment (or Netlify dashboard):

| Variable | Description | Example |
|----------|-------------|---------|
| `NOTION_API_KEY` | Notion integration token | `secret_abcd1234...` |
| `NOTION_DATABASE_ID` | Database ID from Notion URL | `32-character hex string` |

## Netlify Build Process

On every deploy, Netlify runs:

```bash
pip3 install -r scripts/requirements.txt
python3 scripts/fetch-notion-notes.py
hugo --gc --minify
```

Configured in `netlify.toml`.

## Local Development

Test locally before deploying:

```bash
# 1. Set environment variables
export NOTION_API_KEY="..."
export NOTION_DATABASE_ID="..."

# 2. Sync notes from Notion
./scripts/sync-notion.sh

# 3. Build and preview
hugo server

# 4. Visit http://localhost:1313
```

## Troubleshooting

**"NOTION_API_KEY not set"**
- Set the environment variable or add to Netlify

**"Failed to query database"**
- Check database ID is correct
- Verify integration has access to database
- Ensure API key is valid

**Images not loading**
- Check Netlify build logs for download errors
- Verify images exist in `static/images/notes/`

## Complete Setup Guide

See [NOTION_SETUP.md](../NOTION_SETUP.md) for full setup instructions.
