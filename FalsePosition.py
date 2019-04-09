from py_expression_eval import Parser
parser = Parser()

errorCheck = lambda a,e : abs((a - e) / a)

DEV = True

def aproximateByFalsePosition(fx, a, b, stop):
    
    a = float(a)
    B = float(b)

    i = 0
    prev = {}

    while(prev.get('error') == None or prev.get('error')  >= stop):
        fa = fx(a)
        fb = fx(b)
        mn = (a*fb - b*fa) / (fb - fa)
        fmn = fx(mn)

        error = errorCheck(mn, prev.get('mn')) if prev.get('mn') else None
        prev = {'i': i, 'a': a, 'b': b, 'mn': mn, 'fa': fa, 'fb': fb, 'fmn': fmn, 'error': error}
        if DEV : print(prev)

        if (fa * fmn < 0):
            b = mn
        else:
            a = mn
        # End if

        i += 1
    # End while
# End aproximateByFalsePosition

def checkTypes():
    print('wait!')
# End checkTypes

def init():

    # fx = raw_input('Enter a lineal function with a single variable(x):')

    # rangeStart = float(raw_input('Enter the initial range'))
    # rangeEnd = float(raw_input('Enter the initial range'))

    # errorStop = raw_input('Enter the error stop percentage')

    fx = 'PI*x^3 - 9*PI*x^2 + 90'
    rangeStart = 1
    rangeEnd = 3

    expr = parser.parse(fx)

    fx = lambda x: expr.evaluate({'x': x})
    errorStop = 0.001

    aproximateByFalsePosition(fx, rangeStart, rangeEnd, errorStop)

# End init


init()