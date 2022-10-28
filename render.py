# four bones five bone (64x64)
import main as pm
dim  = 64

def propatan(y,x):
    if y > 0:
        return pm.atan(y/x)
    return pm.atan(y/x) + pm.pi
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
    def swap(self):
        return co2D(self.y,self.x)
    def ref(self):
        return co2D(self.x,-self.y+dim)
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
    def rotate(self,axis,angle):
        d = 0.5 * dim
        x,y,z = self.x-d, self.y-d, self.z-d
        if axis == 'z': #theres probably some optimization i'll make later
            mag = abs(pm.comp(x,y))
            if x == 0:
                angle1 = pm.pi / 2
            else:
                angle1 = propatan(y,x).r
            new = pm.ixp(angle1+angle) * mag
            return co3D(new.r+d, new.i+d, z+d).whole()
        elif axis == 'y':
            mag = abs(pm.comp(x,z))
            if x == 0:
                angle1 = pm.pi / 2
            else:
                angle1 = propatan(z,x).r
            new = pm.ixp(angle1+angle) * mag
            return co3D(new.r+d, y+d, new.i+d).whole()
        elif axis == 'x':
            mag = abs(pm.comp(y,z))
            if y == 0:
                angle1 = pm.pi / 2
            else:
                angle1 = propatan(z,y).r
            new = pm.ixp(angle1+angle) * mag
            return co3D(x+d, new.r+d, new.i+d).whole()
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

class wireframe:
    def __init__(self,coordset,lineset):
        self.coset = coordset
        self.lset  = lineset
    def __repr__(self):
        return f'{self.coset} ++ {self.lset}'
    def rotate(self,axis,angle):
        out = self.coset + []
        for indx in range(len(out)):
            out[indx] = out[indx].rotate(axis,angle)
        return wireframe(out,self.lset)
    def project(self):
        for indx in range(len(self.coset)):
            self.coset[indx] = self.coset[indx].project()
    def lines(self,focal=dim):
        points = []
        for each in self.lset:
            points += Line3D(self.coset[each[0]],self.coset[each[1]],focal)
        return points
def Cube(big=32,depth=16):
    t = int(0.5*big)
    d = int(0.5*dim)
    pointset = [ co3D(d-t,d-t,depth), co3D(d-t,d+t,depth),
        co3D(d+t,d-t,depth), co3D(d+t,d+t,depth),
        co3D(d-t,d-t,depth+big), co3D(d-t,d+t,depth+big),
        co3D(d+t,d-t,depth+big), co3D(d+t,d+t,depth+big) ]
    lineset = [(0,1),(0,2),(1,3),(2,3),(4,5),(4,6),(5,7),(6,7),(0,4),(1,5),(2,6),(3,7)]
    return wireframe(pointset,lineset)
def Pyramid(big=32,depth=16):
    t = int(0.5*big)
    d = int(0.5*dim)
    pointset = [ co3D(d-t,d-t,depth), co3D(d+t,d-t,depth),
    co3D(d-t,d-t,depth+big), co3D(d+t,d-t,depth+big), co3D(d,d+t/3,depth+t) ]
    lineset = [(0,1),(0,2),(1,3),(2,3),(0,4),(1,4),(2,4),(3,4)]
    return wireframe(pointset,lineset)

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

print('based rendering has arrived')
based = True

def spinspin(shape=Cube,dr='y'):
    angle = 0
    while angle <= pm.pi:
        plot(
            shape(32,16).rotate(dr,angle).lines(64)
        )
        angle += pm.pi / 120