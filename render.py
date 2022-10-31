# four bones five bone (64x64)
import pm
dim  = 64
class co2D:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        if x > 0 and x < dim and y > 0 and y < dim:
            self.domain = True
        else:
            self.domain = False
    def __repr__(self):
        return f'2D({self.x},{self.y})'
    def whole(self):
        return co2D(round(self.x),round(self.y))
    def __add__(s1,s2): # translation
        return co2D(s1.x+s2.x,s1.y+s2.y)
    def swap(self):
        return co2D(self.y,self.x)
    def ref(self):
        return co2D(self.x,-self.y+dim)
    def rotate(self,angle):
        d = 0.5 * dim
        x,y = self.x-d,self.y-d
        value = pm.comp(x,y) * pm.ixp(angle)
        return co2D(value.r+d,value.i+d).whole()
class co3D:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def __repr__(self):
        return f'3D({self.x},{self.y},{self.z})'
    def project(self,focal=dim):
        Px = ((self.x-dim/2)*focal / (self.z+focal)) + dim/2
        Py = ((self.y-dim/2)*focal / (self.z+focal)) + dim/2
        return co2D(Px,Py).whole()
    def whole(self):
        return co3D(round(self.x),round(self.y),round(self.z))
    def __add__(s1,s2):
        return co3D(s1.x+s2.x,s1.y+s2.y,s1.z+s2.z)
    def rotate(self,axis,angle):
        d = 0.5 * dim
        x,y,z = self.x-d, self.y-d, self.z-d
        if axis == 'x':
            value = pm.comp(y,z) * pm.ixp(angle)
            return co3D(x+d,value.r+d,value.i+d)
        elif axis == 'y':
            value = pm.comp(x,z) * pm.ixp(angle)
            return co3D(value.r+d,y+d,value.i+d)
        elif axis == 'z':
            value = pm.comp(x,y) * pm.ixp(angle)
            return co3D(value.r+d,value.i+d,z+d)
def basicLine(c1,c2):
    slope = (c2.y - c1.y)/(c2.x - c1.x)
    current = co2D(c1.x,c1.y)
    colist = []
    error = 0.5
    while current.x != c2.x:
        colist.append(current.whole())
        current.x += 1
        error += slope
        if error >= 1:
            error -= 1
            current.y += 1
    colist.append(c2.whole())
    return colist
def horizLine(c1,c2):
    colist = []
    current = c1.x
    while current <= c2.x:
        colist.append(co2D(current,c1.y))
        current += 1
    colist.append(c2)
    return colist
def Line(c1,c2):
    if c1.y == c2.y:
        if c2.x >= c1.x:
            out = horizLine(c1,c2)
        else:
            out = horizLine(c2,c1)
    elif c1.x == c2.x:
        if c2.y >= c1.y:
            out = horizLine(c1.swap(),c2.swap())
        else:
            out = horizLine(c2.swap(),c1.swap())
        for indx in range(len(out)):
            out[indx] = out[indx].swap()
    else:
        slope = (c2.y - c1.y)/(c2.x - c1.x)
        if slope >= 0:
            if slope <= 1:
                if c1.x > c2.x:
                    out = basicLine(c2,c1)
                else:
                    out = basicLine(c1,c2)
            else:
                if c1.x > c2.x:
                    out = basicLine(c2.swap(),c1.swap())
                else:
                    out = basicLine(c1.swap(),c2.swap())
                for indx in range(len(out)):
                    out[indx] = out[indx].swap()
        else:
            if -slope <= 1:
                if c1.x > c2.x:
                    out = basicLine(c2.ref(),c1.ref())
                else:
                    out = basicLine(c1.ref(),c2.ref())
            else:
                if c1.x > c2.x:
                    out = basicLine(c2.ref().swap(),c1.ref().swap())
                else:
                    out = basicLine(c1.ref().swap(),c2.ref().swap())
                for indx in range(len(out)):
                    out[indx] = out[indx].swap()
            for indx in range(len(out)):
                out[indx] = out[indx].ref()
    return out
def Line3D(w1,w2,focal=dim):
    return Line(w1.project(focal),w2.project(focal))

class frame2D:
    def __init__(self,coordset,lineset):
        self.coset = coordset
        self.lset = lineset
    def __repr__(self):
        return f'{self.coset} ++ {self.lset}'
    def __add__(s,co):
        for indx in range(len(s.coset)):
            s.coset[indx] += co
        return s
    def rotate(self,angle):
        out = self.coset + []
        for indx in range(len(out)):
            out[indx] = out[indx].rotate(angle)
        return frame2D(out,self.lset)
    def lines(self):
        points = []
        for each in self.lset:
            points += Line(self.coset[each[0]],self.coset[each[1]])
        return points
class frame3D:
    def __init__(self,coordset,lineset):
        self.coset = coordset
        self.lset  = lineset
    def __repr__(self):
        return f'{self.coset} ++ {self.lset}'
    def __add__(s,co):
        for indx in range(len(s.coset)):
            s.coset[indx] += co
            return s
    def rotate(self,axis,angle):
        out = self.coset + []
        for indx in range(len(out)):
            out[indx] = out[indx].rotate(axis,angle)
        return frame3D(out,self.lset)
    def project(self):
        for indx in range(len(self.coset)):
            self.coset[indx] = self.coset[indx].project()
    def lines(self,focal=dim):
        points = []
        for each in self.lset:
            points += Line3D(self.coset[each[0]],self.coset[each[1]],focal)
        return points

square = frame2D([ co2D(16,16), co2D(16,48), co2D(48,16), co2D(48,48) ],
    [ (0,1),(0,2),(1,3),(2,3) ])
cube = frame3D([ co3D(16,16,16), co3D(16,48,16), co3D(48,16,16), co3D(48,48,16),
        co3D(16,16,48), co3D(16,48,48), co3D(48,16,48), co3D(48,48,48) ],
        [ (0,1),(0,2),(1,3),(2,3),(4,5),(4,6),(5,7),(6,7),(0,4),(1,5),(2,6),(3,7) ])
pyramid = frame3D([ co3D(16,24,16), co3D(48,24,16), co3D(16,24,48), co3D(48,24,48), co3D(32,40,32) ],
    [ (0,1),(0,2),(1,3),(2,3),(0,4),(1,4),(2,4),(3,4) ])
ssquare = frame2D([ co2D(24,24), co2D(24,40), co2D(40,24), co2D(40,40) ],
    [(0,1),(0,2),(1,3),(2,3) ])

emptygrid = [
    '                                                                                                                                ',
    '                                                                                                                                ',
    '                                                                                                                                ',
    '                                                                                                                                ',
    '                                                                                                                                ',
    '                                                                                                                                ',
    '                                                                                                                                ',
    '                                                                                                                                ',
    '                                                                                                                                ',
    '                                                                                                                                ',
    '                                                                                                                                ',
    '                                                                                                                                ',
    '                                                                                                                                ',
    '                                                                                                                                ',
    '                                                                                                                                ',
    '                                                                                                                                ',
    '                                                                                                                                ',
    '                                                                                                                                ',
    '                                                                                                                                ',
    '                                                                                                                                ',
    '                                                                                                                                ',
    '                                                                                                                                ',
    '                                                                                                                                ',
    '                                                                                                                                ',
    '                                                                                                                                ',
    '                                                                                                                                ',
    '                                                                                                                                ',
    '                                                                                                                                ',
    '                                                                                                                                ',
    '                                                                                                                                ',
    '                                                                                                                                ',
    '                                                                                                                                ',
    '                                                                                                                                ',
    '                                                                                                                                ',
    '                                                                                                                                ',
    '                                                                                                                                ',
    '                                                                                                                                ',
    '                                                                                                                                ',
    '                                                                                                                                ',
    '                                                                                                                                ',
    '                                                                                                                                ',
    '                                                                                                                                ',
    '                                                                                                                                ',
    '                                                                                                                                ',
    '                                                                                                                                ',
    '                                                                                                                                ',
    '                                                                                                                                ',
    '                                                                                                                                ',
    '                                                                                                                                ',
    '                                                                                                                                ',
    '                                                                                                                                ',
    '                                                                                                                                ',
    '                                                                                                                                ',
    '                                                                                                                                ',
    '                                                                                                                                ',
    '                                                                                                                                ',
    '                                                                                                                                ',
    '                                                                                                                                ',
    '                                                                                                                                ',
    '                                                                                                                                ',
    '                                                                                                                                ',
    '                                                                                                                                ',
    '                                                                                                                                ']
def plot(colist):
    grid = emptygrid + ['']
    output = ''
    for coord in colist:
        if not coord.domain:
            continue
        grid[-coord.y-1] = (grid[-coord.y-1][:2*coord.x] + 
        '[]' + grid[-coord.y-1][2*coord.x+2:])
    for indx in range(-len(grid),0):
        output += grid[indx] + '\n'
    print(output)

# testing purposes
def realspin(shape,axis='y'):
    import time
    angle = 0
    if isinstance(shape,frame2D):
        while True:
            plot(shape.rotate(angle).lines())
            angle += 0.0314159
            time.sleep(0.02)
    elif isinstance(shape,frame3D):
        while True:
            plot(shape.rotate(axis,angle).lines())
            angle += 0.0314159
            time.sleep(0.02)
def spinmove(shape,axis='y',move=1):
    import time
    angle = 0
    tran = 0
    while True:
        plot((shape.rotate(angle) + co2D(tran,0)).lines())
        tran = round(16 * pm.cos(angle).r)
        angle += 0.0314159
        time.sleep(0.02)

print('based rendering has arrived')
based = True