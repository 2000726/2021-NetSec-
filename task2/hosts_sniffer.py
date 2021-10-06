from scapy.all import *

src_spoofed = "192.168.1.144"
dest_ip = "192.168.1.1"
interface = "eth0"
message = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
  
# ICMP Ping to find active hosts
scapy.send(IP(src=src_spoofed,dst=dest_ip)/ICMP()/message)

# 
packets = scapy.sniff(iface=interface,store=true,prn=process_packet)
