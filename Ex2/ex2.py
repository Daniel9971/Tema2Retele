from scapy.all import *

eth=Ether(dst='ff:ff:ff:ff:ff:ff')
arp=ARP(pdst='198.13.13.0/16')
ans, unans = srp(eth/arp)

i=0
while True:
    try:
        print 'IP' + '--' + 'MAC'
        print ans[i][1].psrc + '--' + ans[i][1].hwsrc
        i = i+1
    except IndexError:
        print 'Finish!'
        break
        
   
