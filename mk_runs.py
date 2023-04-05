#! /usr/bin/env python
#
#   script generator 
#
#   lmtinfo.py grep US-3 Science Map | awk '{print $2}' | sort


import os
import sys
from lmtoy import runs

project="2023-S1-US-18"

#        obsnums per source (make it negative if not added to the final combination)
on = {}
on['HZ1'] = [ 104675, 104676, 104677, 104679, 104680, 104681,
              104683, 104684, 104685, 104728, 104729, 104730,
              104732, 104733, 104734,-104736, 104738, 104739,  # CR mar 8 104734 bad tsys
              104740, ]                                        # feb 5

on["HZ2"] = [-104916,-104917,-104918,-104920,-104921,-104922,
             -104924,-104925,-104926,-104929,-104930,-104931,
             -104933,-104934,-104935,-104937,-104938,-104939,  # feb 8   104916-104939 are bad
              105062, 105063, 105064, 105066, 105067, 105068,
             -105070, 105071, 105072, 105075, 105076, 105077,  # CR mar 8 105070 bad tsys
              105079, 105080, 105081, 105084, 105085, 105086,] # feb 9

on["HZ3"] =  [ 105242, 105243, 105244, 105246, 105247,-105248,
               105250, 105251, 105252,-105255, 105256, 105257,
               105259, 105260, 105261, 105263, 105264, 105265,
               105289, 105290, 105291, 105293, 105294, 105295,
               105297, 105298, 105299,                          # feb 10
               105414, 105415, 105416, 105419, 105420, 105421,
               105423, 105424, 105425, 105427, 105428, 105429,
               105435, 105436, 105437,-105439,-105440, 105441,
               105443, 105444, 105445, 105449, 105450, 105451,
               105453, 105454, 105455, 105457, 105458, 105459,]  # feb 14

on['HZ4']  = [ 104090, 104091, 104092, 104094, 104095, 104096,
               104194, 104195, 104196, 104198, 104199, 104200,
               104202, 104203, 104204, 104669, 104670, 104671, ]  # feb 5
  

#        common parameters per source on the first dryrun (run1a, run2a)
pars1 = {}
pars1['HZ1']   = "bandzoom=3 badcb=2/3,3/3"
pars1["HZ2"]   = "bandzoom=2 badcb=0/2,1/2,3/3,3/4" # really only want to remove 2/3 from some
pars1["HZ3"]   = "bandzoom=2"
pars1['HZ4']   = "bandzoom=0 badcb=3/0" # badcb=0/2,3/3,3/4"

#        common parameters per source on subsequent runs (run1b, run2b)
pars2 = {}
pars2['HZ1']   = "srdp=1 admit=0"
pars2["HZ2"]   = "srdp=1 admit=0"
pars2["HZ3"]   = "srdp=1 admit=0"
pars2['HZ4']   = "srdp=1 admit=0"

runs.mk_runs(project, on, pars1, pars2)
