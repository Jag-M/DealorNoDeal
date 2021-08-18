import numpy as np
import random
import math
cases = {1:' ', 2:' ', 3:' ', 4:' ', 5:' '}

while len(cases) > 1:
    print(cases)
    for i in cases:
        if cases[i] == ' ':
            cases[i] = random.randint(0,50)

    userCase = input("Choose a case: ")
    print(cases[int(userCase)])

    cases.pop(int(userCase))

    def RMS():
# Need to input five since we are popping user input early on
        counter = 0

        length = len(cases)
        RMS = []
        while length > 0:
            square = cases[length]*cases[length]
            length = length - 1
            RMS.append(square)

        for i in RMS:
            counter = counter + i

        full = math.sqrt(counter/len(cases))
        print("The offer of the bank is: " + str(full))

    def otherRMS():
        remainingAmounts = []
        squares = []
        counter = 0

        for i in cases:
            remainingAmounts.append(cases[int(i)])

        for i in remainingAmounts:
            square = i*i
            squares.append(square)

        for i in squares:
            counter = counter + i

        final = math.sqrt(counter/len(remainingAmounts))
        print("The Bank's Offer For This Turn Is: " + str(final))



    otherRMS()







