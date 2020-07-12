import sys
sys.path.append("..")
import ngn.ngnargparser as args
from ngn.runagainst import start as runAgainst

def run():
    for target in args.targets:
        runAgainst(target, args.arguments)