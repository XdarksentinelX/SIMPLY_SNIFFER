from scapy.all import *

print("PROGRAM START")

working_interfaces = get_working_ifaces()

print(working_interfaces)

for numer, interface in enumerate(working_interfaces, start=1):
    print(numer, interface)


user_choice = int(input("SELECT YOUR INTERFACE:"))
selected_interface = working_interfaces[user_choice - 1]
print(selected_interface)
len(working_interfaces)