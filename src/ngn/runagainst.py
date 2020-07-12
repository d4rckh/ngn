import sys
sys.path.append("..")
import ngn.methods.pingScan as pingScan

def start(ip, args):
    options = args[0]
    if options.p:
        pingScan.scan(ip)