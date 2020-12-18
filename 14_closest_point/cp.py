import math

from point import Point

def closestPoint(s,p):
    # If S has 0 point in it, give an answer of "no answer exists"
    assert len(s) > 0
    first = 1
    
    for i in s:
        # Compute the distance between So & p, call it bestDistance
        currentDistance = p.distance_from(i)

        if first == 1:
            # Start with the best choice of So
            bestChoice = i
            bestDistance = currentDistance
            first = 0
            pass
        else:
            # If current distance is smaller than bestDistance
            if currentDistance > bestDistance:
                # Update bestChoice to Si and bestDistance to currentDistance
                bestDistance == currentDistance
                bestChoice == i
                pass
            pass
        # Give anser of bestChoice
        return bestDistance
