from ipaddress import *
ip = '117.184.113.45'
net = '117.184.64.0'
for mask in range(33):
    s= ip_network(f'{ip}/{mask}', 0)
    if net == str(s.network_address):
        print(s.netmask)