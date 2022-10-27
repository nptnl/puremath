# all four of your grandparents :p
dim  = 32
class co2D:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __repr__(self):
        return f'({self.x},{self.y})'
    def whole(self):
        return co2D(round(self.x),round(self.y))
    def swap(self):
        return co2D(self.y,self.x)
    def ref(self):
        return co2D(self.x,-self.y+dim)

def Line(c1,c2):
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

emptygrid = [
    '                                                                ',
    '                                                                ',
    '                                                                ',
    '                                                                ',
    '                                                                ',
    '                                                                ',
    '                                                                ',
    '                                                                ',
    '                                                                ',
    '                                                                ',
    '                                                                ',
    '                                                                ',
    '                                                                ',
    '                                                                ',
    '                                                                ',
    '                                                                ',
    '                                                                ',
    '                                                                ',
    '                                                                ',
    '                                                                ',
    '                                                                ',
    '                                                                ',
    '                                                                ',
    '                                                                ',
    '                                                                ',
    '                                                                ',
    '                                                                ',
    '                                                                ',
    '                                                                ',
    '                                                                ',
    '                                                                ',
    '                                                                ']
def plot(colist):
    grid = emptygrid + ['']
    for coord in colist:
        grid[-coord.y-1] = (grid[-coord.y-1][:2*coord.x] + 
        '[]' + grid[-coord.y-1][2*coord.x+2:])
    for indx in range(-len(grid),0):
        print(grid[indx])

print('based lines have arrived')
based = True