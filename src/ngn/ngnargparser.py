import argparse
import sys
from netaddr import IPNetwork
import struct, socket

parser = argparse.ArgumentParser()
#parser.add_argument('--types', type=str, help='Choose query types')
#parser.add_argument('--detailed', help='Get a very detailed view of the responses', action="store_true")
#parser.add_argument('--pretty', help='Get a very pretty view of the responses', action="store_true")
parser.add_argument('-p', help='Run ICMP scan', action="store_true")

arguments = parser.parse_known_args()

#if arguments[0].detailed and arguments[0].pretty:
#    print("[X] You can't use --detailed and --pretty at the same time!")
#    exit()

targets = []
for target in sys.argv[1].split(","):
    if "/" in target:
        (ip, cidr) = target.split('/')
        cidr = int(cidr) 
        host_bits = 32 - cidr
        i = struct.unpack('>I', socket.inet_aton(ip))[0] # note the endianness
        start = (i >> host_bits) << host_bits # clear the host bits
        end = start | ((1 << host_bits) - 1)
        # excludes the first and last address in the subnet
        for i in range(start, end):
            print(socket.inet_ntoa(struct.pack('>I',i)))
    else:
        targets.append(target)