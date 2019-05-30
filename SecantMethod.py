import math

errorThreshold = 0.0001 # Must vary between from 0 to 1;
errorCheck = lambda a,e : abs((a - e) / a)

def f(x):
    return math.exp(-x) - x
# End f    

def doSecant(x0, xi):
    return xi - f(xi) * (x0 - xi) / (f(x0) - f(xi))
# End doNewtonRaphson


def printIteration(i, current):
    if (current['error'] != None):
        print(('i: %i, x: %.4f, error: %.2f') % (i, current['x'], current['error']))
    else: 
        print(('i: %i, x: %.4f, error: ---') % (i, current['x']))
    # End if
# End printIteration


def init():
    prev = { 'x': 0, 'error': None }
    current = { 'x': 1, 'error': None }
    current['error'] = errorCheck(current['x'], prev['x'])

    execute = True
    i = 0

    printIteration(i - 1, prev)
    printIteration(i, current)

    while(execute):
        newX = doSecant(prev['x'], current['x']) 
        prev = current

        current = { 'x': newX, 'error': errorCheck(newX, prev['x']) }

        execute = current['error'] >= errorThreshold
        i += 1
        printIteration(i, current)
    # End while

# End init


init()