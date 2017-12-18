#!/usr/bin/env python3

import sys
from remote_pdb import RemotePdb


avar = 42
print("Hello", avar)
print(sys.argv)
RemotePdb(sys.argv[1], int(sys.argv[2])).set_trace()
# from remote_pdb import RemotePdb; RemotePdb('0.0.0.0', 4244).set_trace()
print("Bye", avar)
