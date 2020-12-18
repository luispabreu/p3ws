# You will want this import for Step 4
from operator import itemgetter

def countWords(counts,line):
    # You should write this function in Step 1,

    # Remove characters and turn to lowercase
    line = line.lower()
    
    temp_list = line.split()
    list = [i.strip('-?.!,[]—:;"\'') for i in temp_list]

    for word in list:
        if word in counts:
            counts[word] = counts[word] + 1
            pass
        else:
            counts[word] = 1
            pass
    return counts

def printResults(counts):
    # You will replace this code in Step 3 and 4
    newlist = [(str(x) + " : " + str(y)) for x, y in counts.items()]
    newlist.sort()
    print(newlist)
    


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


def main():
    countFile("test.txt")

if __name__=="__main__":
    main()
    

