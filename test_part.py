#!/usr/bin/env python
"""This code is crashing with:

IndexError: index 32 is out of bounds for axis 1 with size 25
"""

import cPickle as pickle
from brainx import modularity as md

G3 = pickle.load(open("G3.pck", "rb"))
P3 = md.newman_partition(G3)
