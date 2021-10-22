import os

def main():
    choice = input('Select an attack to use: \nPress 1. ARP Spoofing Attack\nPress 2. EIGRP Attack\nPress 3. STP Attack\nPress 4. SYN Flooding Attack\nPress -> ')
    print(f'You chose {choice} attack...')
    if choice == '1':
        sys = 'python arp_poisoning.py'
        os.system(f'{sys} -h') 
        arg = input('Enter only Command line arguments starting from -ti -> ')
        os.system(f'{sys} {arg}')
    elif choice == '2':
        sys = 'python eigrp_route_poisoning.py'
        os.system(f'{sys} -h') 
        arg = input('Enter only Command line arguments starting from -src -> ')
        os.system(f'{sys} {arg}')   
    elif choice == '3':
        sys = 'python stp_root_attack.py'
        os.system(f'{sys} -h') 
        arg = input('Enter only Command line arguments starting from -src -> ')
        os.system(f'{sys} {arg}')
    elif choice == '4':
        sys = 'python syn_flooding.py'
        os.system(f'{sys} -h') 
        arg = input('Enter only Command line arguments starting from -tg -> ')
        os.system(f'{sys} {arg}')
    else:
        print('Choose from options 1-4')

main()
