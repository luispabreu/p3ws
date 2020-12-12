def calculateRetirement(start_age, initial, working, retired):
    for i in range(working[0]):
        print('Age {:3d} month {:2d} you have ${:.2f}'.format(start_age//12, start_age % 12, initial))
        initial = initial + (initial * working[2]) + working[1]
        start_age += 1
        pass
    for j in range(retired[0]):
        print('Age {:3d} month {:2d} you have ${:.2f}'.format(start_age//12, start_age % 12, initial))
        initial = initial + (initial * working[2]) + working[1]
        start_age += 1
        pass
    return 0

def main():
    working = (489, 1000, .045 / 12)
    retired = (384, -4000, .01 / 12)
    age = 327
    savings = 21345
    calculateRetirement(age,savings,working,retired)
    return 0

main()

       
             
