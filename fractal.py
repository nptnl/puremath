# fatou set and "multibrot" set plotting for
# f(z) = z2 + c, f(z) = z3 + c
# working on a general fatou set plotter
def fatou2(cr=0,ci=0,size=128,iterate=32):
    ppm = open('./plots/current.ppm','w')
    ppm.write(f'P3\n{2*size} {2*size}\n{iterate}\n')
    for imag in range(-size,size):
        colorlist = []
        for real in range(-size,size):
            zr,zi = 2*real/size, 2*imag/size
            counter = 0
            while zr*zr + zi*zi < 4:
                zr,zi = zr*zr - zi*zi + cr, 2*zr*zi + ci
                counter += 1
                if counter >= iterate:
                    counter = 0
                    break
            colorlist.append(counter)
        for b in colorlist:
            ppm.write((str(b)+' ')*3)
        ppm.write('\n')
def fatou3(cr=0,ci=0,size=128,iterate=32):
    ppm = open('./plots/current.ppm','w')
    ppm.write(f'P3\n{2*size} {2*size}\n{iterate}\n')
    for imag in range(-size,size):
        colorlist = []
        for real in range(-size,size):
            zr,zi = 2*real/size, 2*imag/size
            counter = 0
            while zr*zr + zi*zi < 4:
                zr,zi = zr*zr*zr - 3*zr*zi*zi + cr, zi*(3*zr*zr - zi*zi) + ci
                counter += 1
                if counter >= iterate:
                    counter = 0
                    break
            colorlist.append(counter)
        for b in colorlist:
            ppm.write((str(b)+' ')*3)
        ppm.write('\n')
def mandelbrot(size=128,iterate=32,sectionr=0,sectioni=0):
    ppm = open('./plots/current.ppm','w') # rename to save
    ppm.write(f'P3\n{2*size} {2*size}\n{iterate}\n')
    for imag in range(-size,size):
        colorlist = []
        for real in range(-size,size):
            cr,ci = 2*real/size, 2*imag/size
            counter,zr,zi = 0,sectionr,sectioni
            while zr*zr + zi*zi < 4:
                zr,zi = zr*zr - zi*zi + cr, 2*zr*zi + ci
                counter += 1
                if counter >= iterate:
                    counter = 0
                    break
            colorlist.append(counter)
        for b in colorlist:
            ppm.write((str(b)+' ')*3)
        ppm.write('\n')
def bibrot(size=128,iterate=32,sectionr=0,sectioni=0):
    ppm = open('./plots/current.ppm','w') # rename to save
    ppm.write(f'P3\n{2*size} {2*size}\n{iterate}\n')
    for imag in range(-size,size):
        colorlist = []
        for real in range(-size,size):
            cr,ci = 2*real/size, 2*imag/size
            counter,zr,zi = 0,sectionr,sectioni
            while zr*zr + zi*zi < 4:
                zr,zi = zr*zr*zr - 3*zr*zi*zi + cr, zi*(3*zr*zr - zi*zi) + ci
                counter += 1
                if counter >= iterate:
                    counter = 0
                    break
            colorlist.append(counter)
        for b in colorlist:
            ppm.write((str(b)+' ')*3)
        ppm.write('\n')

print('based fractals have arrived')
based = True