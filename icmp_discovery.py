from scapy.all import *
import logging

# Pre-definitions
dest_network = "10.1.1."
hosts = []

# Suppress Warning Output
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

# Loop Through Network to Identify Hosts.
print("Available Hosts\n--------------------------------------")
for i in range(1,255):
  dest_host = dest_network + str(i)
  
  # ICMP Ping to find active hosts
  message = sr1(IP(src=RandIP(), dst=dest_host)/ICMP(), timeout=1, verbose=0)
  
  if message:
    print("Host: " + message.src)
    hosts.append(message.src)
    
sys.exit(0)
