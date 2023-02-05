#! /usr/bin/env python
#
#   script generator 
#
#   lmtinfo.py grep US-3 Science Map | awk '{print $2}' | sort


import os
import sys

# in prep of the new lmtoy module
try:
    lmtoy = os.environ['LMTOY']
    sys.path.append(lmtoy)
    from lmtoy import runs
except:
    print("No LMTOY with runs.py")
    sys.exit(0)

project="2023-S1-US-18"

#        obsnums per source (make it negative if not added to the final combination)
on = {}
on['HZ4'] = [ 104090, 104091, 104092, 104094, 104095, 104096,
              104198, 104199, 104200, 104202, 104203, 104204,
              104669, 104670, 104671 ]                         # feb 5
on['HZ1'] = [ 104675, 104676, 104677, 104679, 104680, 104681,
              104683, 104684, 104685, 104728, 104729, 104730,
              104732, 104733, 104734, 104736, 104738, 104739,
              104740 ]                                         # feb 5

#        common parameters per source on the first dryrun (run1a, run2a)
pars1 = {}
pars1['HZ1']   = ""
pars1['HZ4']   = "bandzoom=0 rthr=0.01 cthr=0.01"

#        common parameters per source on subsequent runs (run1b, run2b)
pars2 = {}
pars2['HZ1']   = ""
pars2['HZ4']   = "srdp=1 admit=0"

runs.mk_runs(project, on, pars1, pars2)
