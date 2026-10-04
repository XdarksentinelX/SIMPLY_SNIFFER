#!/bin/bash

PROJECT_DIR="$(cd "$(dirname "$0")" && pwd)"
VENV_DIR="$PROJECT_DIR/.venv"
MAIN_FILE="$PROJECT_DIR/MAIN.PY"

echo "Installing SIMPLY SNIFFER..."

python3 -m venv "$VENV_DIR"

"$VENV_DIR/bin/python" -m pip install --upgrade pip
"$VENV_DIR/bin/python" -m pip install scapy

sudo tee /usr/local/bin/simply_sniffer > /dev/null <<EOF
#!/bin/bash

"$VENV_DIR/bin/python" "$MAIN_FILE"
EOF

sudo chmod +x /usr/local/bin/simply_sniffer

echo
echo "SIMPLY SNIFFER installed successfully."
echo "Run: sudo simply_sniffer"
