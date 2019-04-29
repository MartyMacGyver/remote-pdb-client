#!/usr/bin/env python3

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

from remote_pdb import RemotePdb; RemotePdb(HOST, PORT).set_trace()  # noqa

print("Do something", avar)
print("Bye", avar)
