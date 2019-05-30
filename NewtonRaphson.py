import math

errorThreshold = 0.0001 # Must vary between from 0 to 1;
errorCheck = lambda a,e : abs((a - e) / a)

def df(x):
    return -math.exp(-x) - 1
# End df

def f(x):
    return math.exp(-x) - x
# End f    

def doNewtonRaphson(x):
    return x - f(x) / df(x)
# End doNewtonRaphson


def printIteration(i, current):
    if (current['error'] != None):
        print(('i: %f, x: %f, error: %f') % (i, current['x'], current['error']))
    else: 
        print(('i: %f, x: %f, error: -') % (i, current['x']))

    # End if
# End printIteration


def init():
    prev = None
    current = { 'x': 0, 'error': None }

    execute = True
    i = 0

    printIteration(i, current)

    while(execute):
        prev = current

        newX = doNewtonRaphson(current['x']) 
        current = { 'x': newX, 'error': errorCheck(newX, prev['x']) }

        execute = current['error'] >= errorThreshold
        i += 1
        printIteration(i, current)
    # End while

# End init


init()