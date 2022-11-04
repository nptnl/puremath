# all four of your grandparents ;)
class quat:
    def __init__(self,real,imag,jmag,kmag):
        self.r, self.i, self.j, self.k = real,imag,jmag,kmag
    def __repr__(self):
        string = f'({self.r}'
        if self.i < 0:
            string += f'{self.i}i'
        else:
            string += f'+{self.i}i'
        if self.j < 0:
            string += f'{self.j}j'
        else:
            string += f'+{self.j}j'
        if self.k< 0:
            string += f'{self.k}k)'
        else:
            string += f'+{self.k}k)'
        return string
    def __neg__(self):
        return quat(-self.r,-self.i,-self.j,-self.k)
    def __add__(s1,s2):
        return quat(s1.r+s2.r,s1.i+s2.i,s1.j+s1.j,s1.k+s1.k)
    def __sub__(s1,s2):
        return quat(s1.r-s2.r,s1.i-s2.i,s1.j-s1.j,s1.k-s1.k)
    def __mul__(s1,s2):
        return quat(
            s1.r*s2.r - s1.i*s2.i - s1.j*s2.j - s1.k*s2.k,
            s1.r*s2.i + s1.i*s2.r + s1.j*s2.k - s1.k*s2.j,
            s1.r*s2.j - s1.i*s2.k + s1.j*s2.r + s1.k*s2.i,
            s1.r*s2.k + s1.i*s2.j - s1.j*s2.i + s1.k*s2.r)
    def conj(self):
        return quat(self.r,-self.i,-self.j,-self.k)
    def inv(self):
        divisor = self.r*self.r + self.i*self.i + self.j*self.j + self.k*self.k
        return quat(self.r/divisor, -self.i/divisor, -self.j/divisor, -self.k/divisor)
    def __truediv__(s1,s2):
        return s1 * s2.inv()
q1,qi,qj,qk = quat(1,0,0,0), quat(0,1,0,0), quat(0,0,1,0), quat(0,0,0,1)

based = True
print('based 4D numbers have arrived')