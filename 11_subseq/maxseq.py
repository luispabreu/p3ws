def maxSeq(list):
    if len(list) < 2:
        return len(list)
    length_now = 1
    length_max = 1
    for i in range(1,len(list)):
        if list[i] > list[i-1]:
            length_now += 1
        else:
            length_now = 1
            pass
        if length_now > length_max:
            length_max = length_now
            pass
        pass
    return length_max

        
