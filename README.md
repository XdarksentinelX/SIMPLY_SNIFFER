# SIMPLY_SNIFFER

A lightweight Python network sniffer built with Scapy. The project captures network packets, displays live protocol statistics, and saves captured traffic to PCAP files for later analysis in Wireshark.

## Features

- Network interface selection
- Live packet counter and protocol statistics
- TCP, UDP, ICMP, ARP, and OTHER packet classification
- PCAP capture using Scapy's `PcapWriter`
- Automatic creation of the default `captures` directory
- Custom capture directory selection
- Automatic capture filename numbering (`capture_001.pcap`, `capture_002.pcap`, etc.)
- Installation script for setting up the Python environment and command-line launcher

## Requirements

- Linux
- Python 3
- Git
- Sufficient privileges for packet capture
- Wireshark (optional, for analyzing PCAP files)

## Installation

Clone the repository:

```bash
git clone https://github.com/XdarksentinelX/SIMPLY_SNIFFER.git
cd SIMPLY_SNIFFER
```

Run the installer:

```bash
chmod +x install.sh
./install.sh
```

The installer creates a Python virtual environment, installs Scapy, and creates the `simply_sniffer` command in `/usr/local/bin`.

## Usage

Start the sniffer with elevated privileges:

```bash
sudo simply_sniffer
```

1. Select a network interface.
2. Choose the default capture directory or enter a custom directory.
3. Monitor live packet statistics.
4. Press `Ctrl+C` to stop capturing and close the PCAP file.

## Capture Storage

By default, captures are saved in the project's `captures` directory.

You can also select a custom directory. Capture files are numbered automatically to avoid overwriting existing files.

Example:

```text
captures/
├── capture_001.pcap
├── capture_002.pcap
└── capture_003.pcap
```

## Analyzing Captures with Wireshark

Open a generated `.pcap` file in Wireshark to inspect captured packets and analyze network traffic.

## Technologies

- Python
- Scapy
- Linux
- PCAP
- Wireshark

## Limitations

This version is designed for Linux systems. Termux and Android support may be explored in a future version.

## Responsible Use

Only capture network traffic on systems and networks you own or are explicitly authorized to monitor.

## Author

darksentinel
