from decimal import Decimal, getcontext

# https://en.wikipedia.org/wiki/Beatty_sequence
def solution(s):
    n = Decimal(s)
    getcontext().prec = 102
    r = Decimal(2).sqrt()
    s = r / (r-1)

    def recursion(n):
        if n == 0:
            return 0
        nn = int(r * n)
        sn = int(Decimal(nn) / s)
        return (nn * (nn + 1)) / 2 - recursion(sn) - sn * (sn + 1)
    return str(int(recursion(n)))
