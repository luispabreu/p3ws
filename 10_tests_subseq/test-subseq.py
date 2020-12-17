from subseq import maxSeq
import sys

#write your test cases list this
if (maxSeq([1,2,3]) != 3):
    sys.exit(1)
    pass

if (maxSeq([2,5,100]) != 3):
    sys.exit(1)
    pass

if (maxSeq([1,2,3,1,8]) != 3):
    sys.exit(1)
    pass

if (maxSeq([1,1,1]) != 1):
    sys.exit(1)
    pass

if (maxSeq([]) != 0):
    sys.exit(1)
    pass

if (maxSeq([3,2,1]) != 1):
    sys.exit(1)
    pass

if (maxSeq([1]) != 1):
    sys.exit(1)
    pass

if (maxSeq([-1000,2,3]) != 3):
    sys.exit(1)
    pass

if (maxSeq([1,2,1,2,3]) != 3):
    sys.exit(1)
    pass

if (maxSeq([-1,-2,-3]) != 1):
    sys.exit(1)
    pass

if (maxSeq([-1,0,1]) != 3):
    sys.exit(1)
    pass

if (maxSeq([1,2,3,1,2]) != 3):
    sys.exit(1)
    pass

if (maxSeq([1,2,1,2,3,1,2]) != 3):
    sys.exit(1)
    pass

if (maxSeq([65,97]) != 2):
    sys.exit(1)
    pass



