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


print(piftri(a=3, b=4, c=6))
