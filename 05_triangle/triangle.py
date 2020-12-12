def printTriangle(size):
    # Start with starCount being 0.

    # Count from 0 (inclusive) to size (exclusive), 
    # and for each number i that you count,

        # count from 0 (inclusive) to i (inclusive), 
        # and for each number j that you count,

            # print a "*" without printing a newline,

            # increment starCount.

            # When you finish counting on j, 

        # print a newline ("\n").

        # When you finish counting on i, 

    # your answer is starCount.


def main():
    print('Here is a triangle with height 4:')
    numStars = printTriangle(4)
    print('That triangle had ' + str(numStars) + ' total stars.')
    # Now print "Here is a triangle with height 7:"

    # Then call printTriangle, passing in 7, 
    # and assign the result to numStars 

    # Finally, print "That triangle had [numStars] total stars." such
    # that the [numStars] prints the value of numStars.


main()
