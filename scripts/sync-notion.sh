#!/bin/bash
#
# Sync technical notes from Notion to Hugo
#
# Usage:
#   ./scripts/sync-notion.sh
#
# Environment variables required:
#   NOTION_API_KEY: Your Notion integration token
#   NOTION_DATABASE_ID: ID of your Technical Notes database

set -e

echo "==================================="
echo "Notion → Hugo Sync"
echo "==================================="
echo ""

# Check if environment variables are set
if [ -z "$NOTION_API_KEY" ]; then
    echo "ERROR: NOTION_API_KEY not set"
    echo ""
    echo "Set it with:"
    echo "  export NOTION_API_KEY='secret_...'"
    echo ""
    echo "Get your key from: https://www.notion.so/my-integrations"
    exit 1
fi

if [ -z "$NOTION_DATABASE_ID" ]; then
    echo "ERROR: NOTION_DATABASE_ID not set"
    echo ""
    echo "Set it with:"
    echo "  export NOTION_DATABASE_ID='...'"
    echo ""
    echo "Find it in your Notion database URL:"
    echo "  notion.so/username/<DATABASE_ID>?v=..."
    exit 1
fi

# Install Python dependencies if needed
echo "Checking Python dependencies..."
pip3 install -q -r scripts/requirements.txt

# Run the sync script
echo ""
python3 scripts/fetch-notion-notes.py

echo ""
echo "==================================="
echo "Sync complete!"
echo "==================================="
