import sys
from scapy.all import sr,IP,ICMP

def scan(ip):
    ans,unans=sr(IP(dst="1.1.1.1")/ICMP())
    ans.summary( lambda ss,r : r.sprintf("{IP: %IP.src% is alive}") )
