# fatou set plotting of f(z) = z2 + c
def julia(cr=0,ci=0,size=128,iterate=64):
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
def mandelbrot(size=128,iterate=64,sectionr=0,sectioni=0):
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

print('based fractals have arrived')
based = True