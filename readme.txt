# Summary instructions - brainx modularity problems.

The npy files in here are all causing problems with modularity extraction,
there are altogether 4 different types of errors.

1. The following commands all fail with 
ValueError: Empty module after node move

%run NewmanMod_debug.py cmat_kki_adhd_aal_adhd_S0B0_0.0499866345897.npy adjust
%run NewmanMod_debug.py cmat_kki_adhd_aal_adhd_S7B0_0.149959903769.npy adjust
%run NewmanMod_debug.py cmat_kki_adhd_aal_td_S0B0_0.249933172948.npy adjust
%run NewmanMod_debug.py cmat_kki_adhd_aal_td_S10B0_0.0999732691794.npy adjust

2. This one fails with:
UnboundLocalError: local variable 'gp_best' referenced before assignment

%run NewmanMod_debug.py cmat_kki_adhd_aal_td_S4B1_0.199946538359.npy adjust

3. This one fails with:
ValueError: The eigenvalue range specified is not valid.
Valid range is [0,-1]

%run NewmanMod_debug.py cmat_kki_adhd_aal_adhd_S1B0_0.0499866345897.npy newman

4. These fail with
RuntimeError: maximum recursion depth exceeded while calling a Python object

%run NewmanMod_debug.py cmat_kki_adhd_aal_td_S12B1_0.149959903769.npy newman
%run NewmanMod_debug.py cmat_kki_adhd_aal_adhd_S0B1_0.199946538359.npy newman
%run NewmanMod_debug.py cmat_kki_adhd_aal_td_S14B1_0.249933172948.npy newman

5. And last, this one, which loads a pickled graph, fails with
IndexError: index 32 is out of bounds for axis 1 with size 25

%run test_part.py

6. And one last one, rob_g3.npy has a new error that may be related to hierarchical partitioning

########################################################################################################

# More detailed info.  What follows is just more detail, all commands that
create errors have been pasted above in the summary instructions.

This file lists the commands I ran and the cmat output files associated with each that are saved in this directory. Note that I have 3 blocks for each subject (0/1/2).

To debug, run: NewmanMod_debug.py with two arguments:
1) cmat filename (file name convention: cmat_<project>_<atlas>_<subgroup>_S<subject#>_B<block#>_<cost>.npy)
2) failed command (newman or adjust)

########################################################################################################
Errors associated with md.adjust_partition (there were 3; I chose one subject that failed for each cost)
########################################################################################################

ERROR ONE INITIAL COMMAND THAT FAILED (from /home/despo/jrcohen/gitrepos/graphtheory dir)

%run NewmanMod.py kki_adhd aal adhd '' none '' 0.05 0 1 1 'all' cmat_kki_adhd_aal_adhd_S0BX_0.0499866345897.npy

DEBUG COMMAND:

%run NewmanMod_debug.py cmat_kki_adhd_aal_adhd_S0B0_0.0499866345897.npy adjust

-you can also run it with B1 or B2 substituted for the B0, but some of those runs might work

run NewmanMod.py kki_adhd aal adhd '' none '' 0.15 7 8 1 'all'
cmat_kki_adhd_aal_adhd_S7BX_0.149959903769.npy

DEBUG COMMAND:

%run NewmanMod_debug.py cmat_kki_adhd_aal_adhd_S7B0_0.149959903769.npy adjust

-you can also run it with B1 or B2 substituted for the B0, but some of those runs might work

run NewmanMod.py kki_adhd aal td '' none '' 0.25 0 1 1 'all'
cmat_kki_adhd_aal_td_S0BX_0.249933172948.npy

DEBUG COMMAND:

%run NewmanMod_debug.py cmat_kki_adhd_aal_td_S0B0_0.249933172948.npy adjust

-you can also run it with B1 or B2 substituted for the B0, but some of those runs might work

ERROR TWO INITIAL COMMAND THAT FAILED (from /home/despo/jrcohen/gitrepos/graphtheory dir)
*this is actually the same error as the newman error below, so it's actually a problem with the newman_partition function
run NewmanMod.py kki_adhd aal td '' none '' 0.1 10 11 1 'all'
cmat_kki_adhd_aal_td_S10BX_0.0999732691794.npy

DEBUG COMMAND:

%run NewmanMod_debug.py cmat_kki_adhd_aal_td_S10B0_0.0999732691794.npy adjust

-you can also run it with B1 or B2 substituted for the B0, but some of those runs might work

ERROR THREE INITIAL COMMAND THAT FAILED (from /home/despo/jrcohen/gitrepos/graphtheory dir)
run NewmanMod.py kki_adhd aal td '' none '' 0.2 4 5 1 'all'
cmat_kki_adhd_aal_td_S4BX_0.199946538359.npy

DEBUG COMMAND:

%run NewmanMod_debug.py cmat_kki_adhd_aal_td_S4B1_0.199946538359.npy adjust

-you can also run it with B0 or B2 substituted for the B1 (B0 works, not sure about B2)

####################################################################################################################
Errors associated with md.newman_partition (all errors were the same; I chose one subject that failed for each cost)
####################################################################################################################

ERROR ONE INITIAL COMMAND THAT FAILED (from /home/despo/jrcohen/gitrepos/graphtheory dir)
run NewmanMod.py kki_adhd aal adhd '' none '' 0.05 1 2 1 'all' cmat_kki_adhd_aal_adhd_S1BX_0.0499866345897.npy
(all blocks failed)

DEBUG COMMAND:

%run NewmanMod_debug.py cmat_kki_adhd_aal_adhd_S1B0_0.0499866345897.npy newman

-you can also run it with B1 or B2 substituted for the B0, but some of those runs might work

ERROR ONE INITIAL COMMAND THAT FAILED (from /home/despo/jrcohen/gitrepos/graphtheory dir)
run NewmanMod.py kki_adhd aal td '' none '' 0.1 10 11 1 'all'
cmat_kki_adhd_aal_td_S10BX_0.0999732691794.npy
(all blocks failed)

DEBUG COMMAND:

%run NewmanMod_debug.py cmat_kki_adhd_aal_td_S10B0_0.0999732691794.npy newman

-you can also run it with B1 or B2 substituted for the B0, but some of those runs might work

ERROR ONE INITIAL COMMAND THAT FAILED (from /home/despo/jrcohen/gitrepos/graphtheory dir)
run NewmanMod.py kki_adhd aal td '' none '' 0.15 12 13 1 'all'
cmat_kki_adhd_aal_td_S12BX_0.149959903769.npy
(block 0 was fine; blocks 1/2 failed)

DEBUG COMMAND:

%run NewmanMod_debug.py cmat_kki_adhd_aal_td_S12B1_0.149959903769.npy newman

-you can also run it with B0 or B2 substituted for the B1 (B0 works, not sure about B2)

run NewmanMod.py kki_adhd aal adhd '' none '' 0.2 0 1 1 'all'
cmat_kki_adhd_aal_adhd_S0BX_0.199946538359.npy
(block 0 was fine; blocks 1/2 failed)

DEBUG COMMAND:

%run NewmanMod_debug.py cmat_kki_adhd_aal_adhd_S0B1_0.199946538359.npy newman

-you can also run it with B0 or B2 substituted for the B1 (B0 works, not sure about B2)

ERROR ONE INITIAL COMMAND THAT FAILED (from /home/despo/jrcohen/gitrepos/graphtheory dir)
run NewmanMod.py kki_adhd aal td '' none '' 0.25 14 15 1 'all'
cmat_kki_adhd_aal_td_S14BX_0.249933172948.npy
(block 0 was fine; blocks 1/2 failed)

DEBUG COMMAND:

%run NewmanMod_debug.py cmat_kki_adhd_aal_td_S14B1_0.249933172948.npy newman

-you can also run it with B0 or B2 substituted for the B1 (B0 works, not sure about B2)


#######################################################################################
Rob wrote out:
cmat_3011_0.14997684113.npy and part_norelabel_3011_0.14997684113.npy
-perhaps to show that zeroing out the diagnoal of cmat_1 changes the modularity values?
#######################################################################################
