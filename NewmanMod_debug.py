# Modules from the stdlib
import sys
import pickle

# Third-party modules
import networkx as nx
import numpy as np

# Our own modules
from brainx import util
from brainx import modularity as md

# While debugging the library, reload everything
map(reload,[util,md])

def main(argv = sys.argv):

    filename = argv[1] # file name convention: cmat_<project>_<atlas>_<subgroup>_S<subject#>_B<block#>_<cost>.npy
    failedcmd = argv[2] # newman or adjust
    

    # Load saved cmat generated from NewmanMod.py
    cmat_1 = np.load(filename)

    # newman.partition fails if there are Inf/nan's in cmat_1 
    # this occurs on the diagonal (Z-transformed autocorrelation == Inf)
    # so we'll convert the diagonal to 0
    # NOTE: this manipulation to cmat_1 also changes modularity values 
    # calculated with simulated annealing - we don't understand why this happens

    temp=np.isnan(cmat_1)
    cmat_1[temp]=0

    G1 = nx.Graph(weighted = False)
    G1 = nx.from_numpy_matrix(cmat_1,G1)

    P1 = md.newman_partition(G1)
    if failedcmd == 'adjust':
        P1 = md.adjust_partition(G1,P1)

    print('Modularity: ', P1.modularity())

    #save partition information (nodelist is not relabeled here)
    pname = 'part_norelabel_' + '_'.join(filename.split('_')[1:])
    pout = open(pname,'w')
    pickle.dump(P1.index,pout)
    pout.close()
    print('Wrote ',pname)

    #clear variables
    del P1, cmat_1, G1

### MAIN SCRIPT ###
if __name__ == '__main__':
    main()
