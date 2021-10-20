from scapy.all import *

src_spoofed = "200.1.1.14"
dest_network = "200.1.1."
interface = "eth0"
#message = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
  
# ICMP Ping to find active hosts
scapy.send(IP(src=src_spoofed,dst=dest_ip)/ICMP()/message)

for i in range(1,255):
  dest_host = dest_network + str(i)
  message = sr1(IP(dst=dest_host)/ICMP(), timeout=1, verbose=0)
  
  if message:
    print("Host: " + message.src)

# 
packets = scapy.sniff(iface=interface,store=true,prn=process_packet)
