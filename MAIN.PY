from scapy.all import *
import os


def clear_terminal():
    os.system("clear")


def show_banner():
    print("=" * 40)
    print("SIMPLY SNIFFER".center(40))
    print("=" * 40)
    print("***created by darksentinel***".center(40))
    print()


# =========================
# INTERFACE SELECTION
# =========================

clear_terminal()
show_banner()

working_interfaces = get_working_ifaces()

print("AVAILABLE INTERFACES:")
print()

for numer, interface in enumerate(working_interfaces, start=1):
    print(f"[{numer}] {interface}")

print()

user_choice = int(input("SELECT YOUR INTERFACE: "))

while user_choice < 1 or user_choice > len(working_interfaces):
    user_choice = int(input("SELECT YOUR INTERFACE: "))

selected_interface = working_interfaces[user_choice - 1]


# =========================
# SAVE CAPTURE LOCATION
# =========================

def save_location():
    print("=" * 40)
    print("SAVE CAPTURE".center(40))
    print("=" * 40)
    print()
    print("[1] Default location")
    print("[2] Choose location")
    print()

    save_capture_choice = int(input("CHOOSE LOCATION YOUR SAVE: "))

    return save_capture_choice


save_capture_choice = save_location()


if save_capture_choice == 1:

    project_path = os.path.dirname(os.path.abspath(__file__))

    default_path = os.path.join(project_path, "captures")

    os.makedirs(default_path, exist_ok=True)

    save_path = default_path


elif save_capture_choice == 2:

    choose_location_path = input("ENTER SAVE PATH: ")

    if os.path.exists(choose_location_path):
        save_path = choose_location_path

    else:
        os.makedirs(choose_location_path, exist_ok=True)
        save_path = choose_location_path


# =========================
# CAPTURE FILE NAME
# =========================

capture_number = 1

capture_name = f"capture_{capture_number:03d}.pcap"

while os.path.exists(os.path.join(save_path, capture_name)):

    capture_number = capture_number + 1

    capture_name = f"capture_{capture_number:03d}.pcap"


capture_file = os.path.join(save_path, capture_name)


# =========================
# PCAP WRITER
# =========================

pcap_writer = PcapWriter(
    capture_file,
    append=False,
    sync=True
)


# =========================
# PACKET STATISTICS
# =========================

packets = 0
tcp_packets = 0
udp_packets = 0
icmp_packets = 0
arp_packets = 0
other_packets = 0


def show_statistics():

    print("\033[1;1H", end="")

    print("=" * 40)
    print("PACKET STATISTICS".center(40))
    print("=" * 40)
    print()

    print("Interface:", selected_interface)
    print("Captured packets:", packets)
    print("TCP packets:", tcp_packets)
    print("UDP packets:", udp_packets)
    print("ICMP packets:", icmp_packets)
    print("ARP packets:", arp_packets)
    print("OTHER packets:", other_packets)

    print("\033[0J", end="", flush=True)


def show_packet(packet):

    global packets
    global tcp_packets
    global udp_packets
    global icmp_packets
    global arp_packets
    global other_packets

    packets = packets + 1

    pcap_writer.write(packet)

    if packet.haslayer(TCP):
        tcp_packets = tcp_packets + 1

    elif packet.haslayer(UDP):
        udp_packets = udp_packets + 1

    elif packet.haslayer(ICMP):
        icmp_packets = icmp_packets + 1

    elif packet.haslayer(ARP):
        arp_packets = arp_packets + 1

    else:
        other_packets = other_packets + 1

    show_statistics()


# =========================
# PACKET CAPTURE
# =========================

clear_terminal()

try:

    sniff(
        iface=selected_interface,
        prn=show_packet,
        store=False
    )

except KeyboardInterrupt:

    pass

finally:

    pcap_writer.close()

    clear_terminal()

    print("Saved:", capture_file)