from pm import comp
from render import co2D,image

def julia(c,size=128):
    # z = z*z + c
    colist = []
    for real in range(size):
        for imag in range(size):
            point = co2D(real,imag)
            counter = 0
            z = comp(4*real/size - 2, 4*real/size - 2)
            while z.r*z.r + z.i*z.i < 2:
                z = z*z + c
                counter += 1
                if counter > 100:
                    colist.append(point)
                    break
    return image(colist,size)
def mandelbrot(size=128):
    colist = []
    for real in range(size):
        for imag in range(size):
            point = co2D(real,imag)
            counter = 0
            c = comp(4*real/size - 2, 4*imag/size - 2)
            z = comp(0,0)
            while z.r*z.r + z.i*z.i < 2:
                z = z*z + c
                counter += 1
                if counter > 100:
                    colist.append(point)
                    break
    return image(colist,size)

print('based fractals have arrived')
based = True