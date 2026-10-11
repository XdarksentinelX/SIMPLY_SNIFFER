
#!/usr/bin/env bash
set -Eeuo pipefail

PROJECT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
VENV_DIR="$PROJECT_DIR/.venv"
MAIN_FILE="$PROJECT_DIR/MAIN.PY"
LAUNCHER="/usr/local/bin/simply_sniffer"

echo "Installing SIMPLY_SNIFFER..."

# Check required commands
for cmd in python3 sudo; do
    if ! command -v "$cmd" >/dev/null 2>&1; then
        echo "Error: required command '$cmd' was not found." >&2
        exit 1
    fi
done

# Check project files
if [[ ! -f "$MAIN_FILE" ]]; then
    echo "Error: MAIN.PY was not found in $PROJECT_DIR" >&2
    exit 1
fi

# Create virtual environment
if ! python3 -m venv "$VENV_DIR"; then
    echo "Error: could not create virtual environment." >&2
    echo "On Debian/Ubuntu, install python3-venv and try again." >&2
    exit 1
fi

# Install dependencies
"$VENV_DIR/bin/python" -m pip install --upgrade pip
"$VENV_DIR/bin/python" -m pip install scapy

# Create launcher
sudo tee "$LAUNCHER" >/dev/null <<EOF
#!/usr/bin/env bash
exec "$VENV_DIR/bin/python" "$MAIN_FILE" "\$@"
EOF

sudo chmod 755 "$LAUNCHER"

echo
echo "SIMPLY_SNIFFER installed successfully."
echo "Run using:"
echo "  sudo $LAUNCHER"
echo
echo "If 'sudo simply_sniffer' is not found, use the full path above."
