def sortFile(filename):
    with open(filename) as f:
        list = [line for line in f]
        list.sort()
        pass
    return list
