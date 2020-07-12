import sys
sys.path.append("..")
from scapy.all import sr1,IP,ICMP,conf
from ngn.methods.submethods import ttlosd

conf.verb = 0

def scan(ip, args):
    #print(ip)
    for i in range(args.pn):
        p=sr1(IP(dst=ip)/ICMP()/"XXXXX",timeout=2)
        if p:
            #p.show()
            IPh = p[IP]
            ICMPh = p[ICMP]
            print(ip + " (ICMP Reply) ttl: " + str(IPh.ttl) + "; " + "load: " + str(ICMPh.load) + " (OS Detection: " + ttlosd.main(IPh.ttl) + ")")
            