def printTriangle(size):
    # Start with starCount being 0.
    starCount = 0
    # Count from 0 (inclusive) to size (exclusive), 
    # and for each number i that you count,
    for i in range (0, size + 1): 
        # count from 0 (inclusive) to i (inclusive),
        for j in range (0, i):
            # and for each number j that you count,
            # print a "*" without printing a newline,
            print('*', end='')
            # increment starCount.
            starCount += 1
            # When you finish counting on j, 
            pass
        # print a newline ("\n").
        print("\n")
        # When you finish counting on i, 
        pass
    # your answer is starCount.
    return starCount

def main():
    print('Here is a triangle with height 4:')
    numStars = printTriangle(4)
    print('That triangle had ' + str(numStars) + ' total stars.')
    # Now print "Here is a triangle with height 7:"
    print('Here is a triangle with height 7:')
    
    # Then call printTriangle, passing in 7, 
    # and assign the result to numStars 
    numStars = printTriangle(7)

    # Finally, print "That triangle had [numStars] total stars." such
    # that the [numStars] prints the value of numStars.
    print('That triangle had ' + str(numStars) + ' total stars.')


main()
