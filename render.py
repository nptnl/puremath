# four bones five bone (64x64)
dim  = 64
class co2D:
    def __init__(self,x,y):
        self.x = x
        self.y = y
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
            return horizLine(c1.swap(),c2.swap())
        else:
            return horizLine(c2.swap(),c1.swap())
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
def Line3D(w1,w2):
    return Line(w1.project(),w2.project())

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
    for coord in colist:
        grid[-coord.y-1] = (grid[-coord.y-1][:2*coord.x] + 
        '[]' + grid[-coord.y-1][2*coord.x+2:])
    for indx in range(-len(grid),0):
        print(grid[indx])

def Cube32(big,depth): #ignore this cancer its for testing
    t = big/2

    p1 = co3D(dim/2-t,dim/2-t,depth).project()
    p2 = co3D(dim/2-t,dim/2+t,depth).project()
    p3 = co3D(dim/2+t,dim/2-t,depth).project()
    p4 = co3D(dim/2+t,dim/2+t,depth).project()
    p5 = co3D(dim/2-t,dim/2-t,depth+big).project()
    p6 = co3D(dim/2-t,dim/2+t,depth+big).project()
    p7 = co3D(dim/2+t,dim/2-t,depth+big).project()
    p8 = co3D(dim/2+t,dim/2+t,depth+big).project()

    structure = (Line(p1,p2) + Line(p1,p3) + Line(p4,p2) + Line(p4,p3)
    + Line(p1,p5) + Line(p2,p6) + Line(p3,p7) + Line(p4,p8)
    + Line(p5,p6) + Line(p5,p7) + Line(p8,p6) + Line(p8,p7) )

    return structure

print('based lines have arrived')
based = True