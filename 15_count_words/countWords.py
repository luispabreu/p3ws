#You will want this import for Step 4
from operator import itemgetter

def countWords(counts,line):
    # You should write this function in Step 1,
    # and improve it in Step 2
    return counts

def printResults(counts):
    # You will replace this code in Step 3 and 4
    print(counts)
    pass


# You do not need to modify this function.
# It will call your countWords and printResults functions
def countFile(fname):
    counts={}
    with open(fname) as f:
        for line in f:
            countWords(counts,line)
            pass
        pass
    printResults(counts)
    pass
