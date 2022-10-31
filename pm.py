# both of your parents ;)
class comp:
    def __init__(self,real,imag):
        self.r = real
        self.i = imag
    def __repr__(self):
        if self.i == 0:
            return f'({self.r}+0i)'
        elif self.i < 0:
            return f'({self.r}{self.i}i)'
        else:
            return f'({self.r}+{self.i}i)'
    def __neg__(self):
        return comp(-self.r,-self.i)
    def __abs__(self):
        return sqrt(self.r*self.r + self.i*self.i)[0].r
    def __add__(s1,s2):
        if isinstance(s2,comp):
            return comp(s1.r+s2.r,s1.i+s2.i)
        return comp(s1.r+s2,s1.i)
    def __sub__(s1,s2):
        if isinstance(s2,comp):
            return comp(s1.r-s2.r,s1.i-s2.i)
        return comp(s1.r-s2,s1.i)
    def __mul__(s1,s2):
        if isinstance(s2,comp):
            return comp(s1.r*s2.r - s1.i*s2.i, s1.r*s2.i + s1.i*s2.r)
        return comp(s1.r*s2,s1.i*s2)
    def conj(self):
        return comp(self.r,-self.i)
    def inv(self):
        divisor = self.r*self.r + self.i*self.i
        return comp(self.r/divisor, -self.i/divisor)
    def __truediv__(s1,s2):
        if isinstance(s2,comp):
            return s1 * s2.inv()
        return comp(s1.r/s2,s1.i/s2)
    def __pow__(s1,s2):
        return exp(ln(s1) * s2)
class poly:
    def __init__(self,coef):
        while coef[0] == 0 and len(coef) > 1:
            coef.pop(0)
        self.le = len(coef)
        if coef == []:
            coef = [0]
        self.co = coef
    def __repr__(self):
        string = ''
        for order in range(-self.le,0):
            coef = self.co[order]
            if isinstance(coef,comp):
                term = f'+{coef}x{-order-1}'
            elif coef < 0:
                term = f'{coef}x{-order-1}'
            else:
                term = f'+{coef}x{-order-1}'
            string += term
        return string
    def __neg__(self):
        p1 = self.co
        for term in p1:
            term = -term
        return poly(p1)
    def __add__(s1,s2):
        p1 = s1.co
        p2 = s2.co
        polysum = []
        while len(p1) < len(p2):
            p1.insert(0,0)
        while len(p1) > len(p2):
            p2.insert(0,0)
        for term in range(len(p1)):
            if isinstance(p2[term],comp):
                polysum.append(p2[term]+p1[term])
            else:
                polysum.append(p1[term]+p2[term])
        return poly(polysum)
    def __sub__(s1,s2):
        p1 = s1.co
        p2 = s2.co
        polysum = []
        while len(p1) < len(p2):
            p1.insert(0,0)
        while len(p1) > len(p2):
            p2.insert(0,0)
        for term in range(len(p1)):
            if isinstance(p2[term],comp):
                polysum.append(p2[term]-p1[term])
            else:
                polysum.append(p1[term]-p2[term])
        return poly(polysum)
    def __mul__(s1,s2):
        p1 = s1.co
        p2 = s2.co
        product = []
        while len(product) < s1.le + s2.le - 1:
            product.append(0)
        for t1 in range(-s1.le,0):
            for t2 in range(-s2.le,0):
                if isinstance(p2[t2],comp):
                    product[t1+t2+1] = p2[t2] * p1[t1] + product[t1+t2+1]
                elif isinstance(p1[t1],comp):
                    product[t1+t2+1] = p1[t1] * p2[t2] + product[t1+t2+1]
                else:
                    product[t1+t2+1] += p1[t1] * p2[t2]
        return poly(product)
    def rootdiv(self,rt):
        quotient = [self.co[0]]
        C = self.co[0]
        for time in range(1,self.le):
            C = rt*C + self.co[time]
            quotient.append(C)
        quotient.pop()
        return poly(quotient)
    def val(self,x):
        total = comp(0,0)
        for term in range(-self.le,0):
            temp = comp(1,0)
            for time in range(-term-1):
                temp *= x
            total += temp*self.co[term]
        return total
    def dvt(self):
        derivative = []
        for term in range(-self.le,-1):
            derivative.append(self.co[term] * (-term-1))
        return poly(derivative)
    def itg(self,C=0):
        integral = []
        for term in range(-self.le,0):
            integral.append(self.co[term] / -term)
        integral.append(C) # enter your own C-value, assumes it's 0
        return poly(integral)
    def solve(self,y=0): # welcome to cracked math
        p = self - poly([y])
        rootlist = []
        string = ''
        while p.le > 1:
            solution = newton(p)
            rootlist.append(solution)
            p = p.rootdiv(solution)
        return rootlist

ii = comp(0,1)
i1 = comp(1,0)
pi = 3.14159265358979
tau = 2*pi
e = 2.718282

def newton(p,y=0):
    counter = 0
    pp = p.dvt()
    x1,x2 = comp(2,1),comp(1,1)
    while abs(x2.r-x1.r) > 0.0001 or abs(x2.i-x1.i) > 0.0001:
        if counter > 100:
            x2 += 1
            counter = 0
        x1 = x2
        x2 -= (p.val(x1)-y) / pp.val(x1)
        counter += 1
    return comp(round(x2.r,5),round(x2.i,5))
def rnewton(p,y=0):
    counter = 0
    pp = p.dvt()
    x1,x2 = 2,1
    while abs(x2-x1) > 0.0001:
        if counter > 100:
            x2 += 1
            counter = 0
        x1 = x2
        x2 -= (p.val(x1).r-y) / pp.val(x1).r
        counter += 1
    return round(x2,5)
def sqrt(x):
    return poly([1,0,0]).solve(x)
def cbrt(x):
    return poly([1,0,0,0]).solve(x)
def root(n,x):
    p = [1]
    while len(p) < n:
        p.append(0)
    p.append(-x)
    return poly(p).solve()
def buildp(rootlist):
    function = poly([1])
    for rt in rootlist:
        function *= poly([1,-rt])
    return function

def rangefix(x,rng):
    diff = 0
    if x > rng:
        diff = int(x - rng)
        x -= diff
    elif x < -rng:
        diff = -int(-rng - x)
        x -= diff
    return x,diff
def anglefix(a):
    while a < -pi:
        a += tau
    while a > pi:
        a -= tau
    return a
series = poly([
    2.08767569878681e-09,2.505210838544172e-08,
    2.7557319223985894e-07,2.7557319223985893e-06,
    2.48015873015873e-05,0.0001984126984126984,
    0.001388888888888889,0.008333333333333333,
    0.041666666666666664,0.16666666666666666,0.5,1.0,1.0])
def exp(x):
    if isinstance(x,comp):
        inp = x
    else:
        inp = comp(x,0)    
    inp.i = anglefix(inp.i)
    inp.r,extra = rangefix(inp.r,3)
    calc = series.val(inp)
    if extra > 0:
        for time in range(extra):
            calc *= e
    elif extra < 0:
        for time in range(-extra):
            calc /= e
    return comp(round(calc.r,6),round(calc.i,6))
def ixp(x):
    return exp(ii*x)
def realn(x):
    inp = x
    diff = 0
    if inp != 0:
        while abs(inp) >= 3:
            inp /= e
            diff += 1
        while abs(inp) <= 0.3:
            inp *= e
            diff -= 1
    return rnewton(series,inp) + diff
def ln(x):
    reflect = 1
    real = realn(abs(x))
    unit = x / abs(x)
    if isinstance(x,comp) and unit.i < 0:
        unit.i = -unit.i
        reflect = -1
    imag = newton(series,unit).i * reflect
    return comp(real,imag)
def log(n,x):
    return ln(x) / ln(n)

class angle:
    def __init__(self,me,mx=1):
        one = me/mx
        while one > 1:
            one -= 1
        while one < 0:
            one += 1
        self.rad = one*tau
        self.deg = one*360
        self.one = one
    def __repr__(self):
        return f'< {self.one*2}π >'
    def __add__(s1,s2):
        return angle(s1.one+s2.one)
    def __sub__(s1,s2):
        return angle(s1.one-s2.one)

def sin(x):
    if isinstance(x,angle):
        inp = x.rad
    else:
        inp = x
    return (ixp(inp) - ixp(-inp))/comp(0,2)
def cos(x):
    if isinstance(x,angle):
        inp = x.rad
    else:
        inp = x
    return (ixp(inp) + ixp(-inp))/2
def tan(x):
    return sin(x) / cos(x)
def csc(x):
    return i1 / sin(x)
def sec(x):
    return i1 / cos(x)
def cot(x):
    return cos(x) / sin(x)
def acos(x):
    return -ii*ln(sqrt(x*x-1)[0]+x)
def asin(x):
    return acos(x) + pi/2
def atan(x):
    return ii/2 * (ln(-ii*x+1)-ln(ii*x+1))
def asec(x):
    return acos(i1 / x)
def acsc(x):
    return asin(i1 / x)
def acot(x):
    return atan(i1 / x)
class polar:
    def __init__(self,radius,angle):
        if radius < 0:
            radius = -radius
            angle += pi
        angle = anglefix(angle)
        self.r = radius
        self.a = angle / pi
    def __repr__(self):
        return f'{self.r}*e^({self.a}iπ)'
    def __neg__(self):
        return polar(self.r,self.a+pi)
    def __mul__(s1,s2):
        return polar(s1.r*s2.r,s1.a+s2.a)
    def __truediv__(s1,s2):
        return polar(s1.r/s2.r,s1.a-s2.a)

print('based math has arrived')
based = True