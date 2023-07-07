from scapy.all import *

# Craft an ICMP ping request packet
packet = Ether() / IP()
packet.show()