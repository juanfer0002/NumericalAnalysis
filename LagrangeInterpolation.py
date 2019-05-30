
X_POINTS = [2, 2.5, 3.2, 4]
FX_POINTS = [8, 14, 15, 8]



def printFunction(L):
    print(L)
# End def


def getFraction(i):

    numerator = ''
    denominator = 1

    currentX = X_POINTS[i]

    for j in range(0, len(X_POINTS)):
        if (i != j):
            numerator += ('(x - %.2f)') % (X_POINTS[j]) 
            denominator *= (currentX - X_POINTS[j])

        # End if
    # End for

    return ('[ %s / %.2f ] * %.2f ') % (numerator, denominator, FX_POINTS[i])
# End getDenominator

def init():
    L = []

    for i in range(0, len(X_POINTS)):
        L.append(getFraction(i))
    # End for

    printFunction(L)


# End init


init()