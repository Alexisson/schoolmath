import math as m


def queq(a, b=0, c=0):
    if b == 0:
        try:
            return m.sqrt(-c/a), m.sqrt(-c/a)
        except (ZeroDivisionError, ValueError):
            return 'No roots'
    elif c == 0:
        try:
            return -b/a
        except (ZeroDivisionError, ValueError):
            return 'No roots'
    else:
        D = m.pow(b, 2)-4*a*c
        if D < 0:
            return 'No roots'
        elif D < 0:
            return float('{:.2f}'.format(-b/(2*a)))
        else:
            X1 = float('{:.2f}'.format((-b-m.sqrt(D))/(2*a)))
            X2 = float('{:.2f}'.format((-b+m.sqrt(D))/(2*a)))
            return X1, X2


def piftri(a=0, b=0, c=0):
    if a == 0:
        return m.sqrt(m.pow(c, 2)-m.pow(b, 2))
    elif b == 0:
        return m.sqrt(m.pow(c, 2)-m.pow(a, 2))
    elif c == 0:
        return m.sqrt(m.pow(a, 2)+m.pow(b, 2))
    else:
        if m.pow(c, 2) == m.pow(a, 2)+m.pow(b, 2):
            return True
        else:
            return False


def arifmp(d, n, astart=0, afinish=0):
    if astart == 0:
        return -afinish+d*(n-1)
    elif afinish == 0:
        return astart+d*(n-1)
    else:
        return('Non-correct data')


def arifmpsum(n, astart, afinish):
    return ((astart+afinish)/2)*n


def geomp(q, n, bstart=0, bfinish=0):
    if bstart == 0:
        return bfinish/m.pow(q, n-1)
    elif bfinish == 0:
        return bstart/m.pow(q, n-1)
    else:
        return('Non-correct data')


def geompsumasc(q, n, bstart=0):
    return (bstart*(1-m.pow(q, n)))/(1-q)


def geompsumdesc(q, bstart=0):
    if abs(q) < 1:
        return bstart/(1-q)
