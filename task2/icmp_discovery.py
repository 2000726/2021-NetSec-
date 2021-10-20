from scapy.all import *
import logging

# Pre-definitions
src_spoofed = "200.1.1.14"
dest_network = "200.1.1."
hosts = []
#interface = "eth0"

# Suppress Warning Output
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

# Loop Through Network to Identify Hosts.
print("Available Hosts\n--------------------------------------")
for i in range(1,255):
  dest_host = dest_network + str(i)
  
  # ICMP Ping to find active hosts
  message = sr1(IP(dst=dest_host)/ICMP(), timeout=1, verbose=0)
  
  if message:
    print("Host: " + message.src)
    hosts.append(message.src)
    

