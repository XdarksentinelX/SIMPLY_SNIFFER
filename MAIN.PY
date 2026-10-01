from scapy.all import *
import shutil


packets = 0


def clear_terminal():
    print("\033[2J\033[H", end="")


def show_banner():

    width = shutil.get_terminal_size().columns

    print("=" * 40)
    print("SIMPLY SNIFFER".center(40))
    print("=" * 40)
    print("created by darksentinel".center(40))
    print()


def show_packet(packet):

    global packets

    packets = packets + 1

    print("\rCAPTURED PACKETS:", packets, end="", flush=True)


# ==============================
# START
# ==============================

clear_terminal()
show_banner()

working_interfaces = get_working_ifaces()

print("AVAILABLE INTERFACES:")
print()

for numer, interface in enumerate(working_interfaces, start=1):

    print(f"[{numer}] {interface}")


user_choice = int(input("\nSELECT YOUR INTERFACE: "))


while user_choice < 1 or user_choice > len(working_interfaces):

    user_choice = int(input("SELECT YOUR INTERFACE: "))


selected_interface = working_interfaces[user_choice - 1]


# ==============================
# PACKET CAPTURE SCREEN
# ==============================

clear_terminal()

print("=" * 40)
print("             PACKET CAPTURE")
print("=" * 40)
print()
print("Interface:", selected_interface)
print()


try:

    captured = sniff(
        iface=selected_interface,
        prn=show_packet,
        store=True
    )

except KeyboardInterrupt:

    print("\n")

    clear_terminal()

    print("=" * 40)
    print("          CAPTURE FINISHED")
    print("=" * 40)
    print()
    print("Interface:", selected_interface)
    print("Captured packets:", packets)
    print()

    wrpcap("capture.pcap", captured)

    print("Saved: capture.pcap")