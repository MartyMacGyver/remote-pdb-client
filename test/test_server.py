#!/usr/bin/env python3

from remote_pdb import RemotePdb
import sys

if len(sys.argv) <= 1:
    HOST = '0.0.0.0'
    PORT = 4244
else:
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])

avar = 42
print("Hello", avar)
print(sys.argv)
RemotePdb(HOST, PORT).set_trace()
# from remote_pdb import RemotePdb; RemotePdb('0.0.0.0', 4244).set_trace()
print("Bye", avar)
