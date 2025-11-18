#!/bin/bash
set -euo pipefail

# Only run this hook in remote environments (Claude Code on the web)
if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

# Set Python path for the project
if [ -n "${CLAUDE_ENV_FILE:-}" ]; then
  echo 'export PYTHONPATH="$CLAUDE_PROJECT_DIR:$PYTHONPATH"' >> "$CLAUDE_ENV_FILE"
fi

# Install Python dependencies if requirements.txt exists
if [ -f "$CLAUDE_PROJECT_DIR/requirements.txt" ]; then
  echo "Installing Python dependencies from requirements.txt..."
  pip install --quiet --no-warn-script-location -r "$CLAUDE_PROJECT_DIR/requirements.txt"
fi

echo "Session start hook completed successfully"
