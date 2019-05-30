
calcNewError = lambda a, e : abs((a - e) / a)
errorThreshold = 0.0001 # Must vary between from 0 to 1;

# This is the matrix to resolve
A = [
    [ 4, -1,  0, -1,  0,  0],
    [-1,  4, -1,  0, -1,  0],
    [ 0, -1,  4,  0,  0, -1],
    [-1,  0,  0,  4, -1,  0],
    [ 0, -1,  0, -1,  4, -1],
    [ 0,  0, -1,  0, -1,  4],
]

# This is the independent matrix
B = [0, 5, 0, 6, -2, 6]


def initXMat():
    X = []

    for a in A:
        X.append({'prev': 0, 'current': 0, 'error': None})
    # End for
    
    return X
# End initXMat

def updateAndCheckErrorForResults(XMat):
    
    isEveryResultUnderThreshold = True
    for x in XMat:
        updateSingleResultError(x)
        error = x['error']
        isEveryResultUnderThreshold = isEveryResultUnderThreshold and error != None and error <= errorThreshold
    # End for

    return not isEveryResultUnderThreshold
# End updateAndCheckErrorForResults

def updateSingleResultError(x):

    current = x['current']
    prev = x['prev']

    if (current):
        x['error'] = calcNewError(current, prev)
    # End if

# End updateSingleResultError

def calcNewXFromPos(i, XMat):
    newX = B[i]

    for j in range(0, len(A)):
        if (i != j):
            currentXValue = XMat[j]['current']
            newX += -1 * A[i][j] * currentXValue
        # End if
    # End for

    newX /= A[i][i]
    return newX
# End calcNewXFromPos

def calcPosition(i, XMat):
    newX = calcNewXFromPos(i, XMat)
    XMat[i]['prev'] = XMat[i]['current']
    XMat[i]['current'] = newX
# End calcPosition

def printMat(it, XMat):
    stringsToPrint = [('it: %d, ') % (it)]

    for i in range(0, len(XMat)):
        x = XMat[i]
        if (x['error'] != None): 
            stringsToPrint.append(('x%i: %.4f, error-x%i: %.2f,') % (i+1, x['current'], i+1, x['error']))
        else:
            stringsToPrint.append(('x%i: %.4f, error-x%i: -,') % (i+1, x['current'], i+1))
        # End if
    # End for

    print(' '.join(stringsToPrint))
# End 

# This resolves the equation
def gaussSeidel():
    XMat = initXMat()

    execute = True
    it = 0
    while (execute):

        for i in range(0, len(XMat)):
            calcPosition(i, XMat)
        # End for
        
        execute = updateAndCheckErrorForResults(XMat)
        printMat(it, XMat) # Enable This to print every iterarion
        it += 1
    # End while

    # printMat(it, XMat) # This prints the last iteration
    print('finish')
# End gaussSeidel


gaussSeidel()