from py_expression_eval import Parser
parser = Parser()

errorCheck = lambda a,e : abs((a - e) / a)

DEV = True

def aproximateByBolzonaro(fx, a, b, stop):
    
    i = 0
    prev = {}

    while(prev.get('error') == None or prev.get('error')  >= stop):
        mn = (a + b) / 2.0
        fa = fx(a)
        fmn = fx(mn)

        error = errorCheck(mn, prev.get('mn')) if prev.get('mn') else None
        prev = {'i': i, 'a': a, 'b': b, 'mn': mn, 'fa': fa, 'fmn': fmn, 'error': error}
        
        printIteration(prev)

        if (fa * fmn < 0):
            b = mn
        else:
            a = mn
        # End if

        i += 1
    # End while
# End aproximateByBolzonaro

def printIteration(it):
    if (it['error']):
        str_format = 'i: %i, a: %.4f, b: %.4f, mn: %.4f, fa: %.4f, fmn: %.4f, error: %.2f'
        print(str_format % (it['i'], it['a'], it['b'], it['mn'], it['fa'], it['fmn'], it['error']))
    else:
        str_format = 'i: %i, a: %.4f, b: %.4f, mn: %.4f, fa: %.4f, fmn: %.4f, error: ---'
        print(str_format % (it['i'], it['a'], it['b'], it['mn'], it['fa'], it['fmn']))
    # End if
# End printIteration

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

    aproximateByBolzonaro(fx, rangeStart, rangeEnd, errorStop)

# End init


init()