# Task 2 Scripts

## main.py

## icmp_discovery.py
A simple scanner that conducts an ICMP Ping scan to 255 addresses within a network. Used to identify hosts present within the network.

## syn_flooding.py
A script that takes in the target IP address as an argument, to conduct a SYN flooding attack on the target IP specified. It also includes a source IP spoofer. Packet data, size and target port can be modified.

*Usage: python syn_flooding.py -t <IP Address>*

## arp_poisoning.py
A script that takes in a number of arguments, to conduct an ARP Poisoning attack on the specified target IP and MAC address. IP and Physical address spoofing will be used, as well as specifying amount of packets to send.

*Usage: python arp_poisoning.py -ti <target_ip> -tm <target_mac> -fi <fake_ip> -fm <fake_mac> -c <count>"*


## stp_root_attack.py

## eigrp_route_poisoning.pu
