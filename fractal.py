from pm import comp

S = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ<>'

def ispace(func,c,size=128,iterate=32):
    pxl = open('./plots/current.npxl','w')
    pxl.write(f'{2*size} {2*size}\n1 16\n')
    for imag in range(-size,size):
        colorlist = []
        for real in range(-size,size):
            x = comp(2.0*real/size, 2.0*imag/size)
            counter = 0
            while 0.0 < x.r*x.r + x.i*x.i < 4.0:
                x = func(x,c)
                counter += 1
                if counter >= iterate:
                    counter = 0
                    break
            colorlist.append(counter)
        for b in colorlist:
            pxl.write(S[b * 16 // iterate])
        pxl.write('\n')
    pxl.close()
    print(f'NPXL render at {2*size}px, iterate {iterate} complete')
def pspace(func,size=128,iterate=64,section=comp(0,0)):
    pxl = open('./plots/current.npxl','w')
    pxl.write(f'{2*size} {2*size}\n1 16\n')
    for imag in range(-size,size):
        colorlist = []
        for real in range(-size,size):
            c = comp(2.0*real/size, 2.0*imag/size)
            counter,x = 0,section
            while x.r*x.r + x.i*x.i < 4.0:
                x = func(x,c)
                counter += 1
                if counter >= iterate:
                    counter = 0
                    break
            colorlist.append(counter)
        for b in colorlist:
            pxl.write(S[b * 16 // iterate])
        pxl.write('\n')
    pxl.close()
    print(f'NPXL render at {2*size}px, iterate {iterate} complete')

def quadra(cr=0,ci=0,size=128,iterate=32):
    pxl = open('./plots/current.npxl','w')
    pxl.write(f'{2*size} {2*size}\n1 16\n')
    for imag in range(-size,size):
        colorlist = []
        for real in range(-size,size):
            zr,zi = 2*real/size, 2*imag/size
            counter = 0
            while zr*zr + zi*zi < 4.0:
                zr,zi = zr*zr - zi*zi + cr, 2*zr*zi + ci
                counter += 1
                if counter >= iterate:
                    counter = 0
                    break
            colorlist.append(counter)
        for b in colorlist:
            pxl.write(S[b * 16 // iterate])
        pxl.write('\n')
    pxl.close()
    print(f'NPXL render at {2*size}px, iterate {iterate} complete')
def mandelbrot(size=128,iterate=32,sectionr=0,sectioni=0):
    pxl = open('./plots/current.npxl','w')
    pxl.write(f'{2*size} {2*size}\n1 16\n')
    for imag in range(-size,size):
        colorlist = []
        for real in range(-size,size):
            cr,ci = 2*real/size, 2*imag/size
            counter,zr,zi = 0,sectionr,sectioni
            while zr*zr + zi*zi < 4.0:
                zr,zi = zr*zr - zi*zi + cr, 2*zr*zi + ci
                counter += 1
                if counter >= iterate:
                    counter = 0
                    break
            colorlist.append(counter)
        for b in colorlist:
            pxl.write(S[b * 16 // iterate])
        pxl.write('\n')
    pxl.close()
    print(f'NPXL render at {2*size}px, iterate {iterate} complete')

print('based fractals have arrived')
based = True