# somewhat in-depth documentation of every function

### **`class comp:` Complex number objects**

`__init__(self,real,imag)` inputs a real and imaginary part for a complex number in form `(a+bi)` and creates the object

`__repr__(self)` uses some positive-negative and string action to return/print comp objects

`__neg__(self)` simply negates both the real and imaginary part to negate the complex number

`__abs__(self)` uses the square root and the distance formula to find the absolute value of a complex number

`__add__(s1,s2)` adds two complex numbers, simply by adding real and imaginary parts

`__sub__(s1,s2)` subtracts two complex numbers, simply by subtracting real and imaginary parts

`__mul__(s1,s2)` uses `(a+bi)(c+di) == a2 - c2 + 2bdi` to multiply complex numbers

`conj(self)` negates only the imaginary part to return a complex number's conjugate

`inv(self)` uses the conjugate to compute the inverse of a complex number

`__truediv__(s1,s2)` simply multiplies one complex number by the other's inverse to divide properly

`__pow__(s1,s2)` uses `exp` and `ln` to compute complex exponentiation

### **`class poly:` Polynomial objects**

`__init__(self,coef)` takes only one argument, a list of coefficients in descending exponent order, and this will include zeros for a term that is not in the polynomial

`__repr__(self)` returns/prints polynomials using each coefficient and exponent (this will be updated in the future)

`__neg__(self)` simply negates each coefficient to negate the polynomial

`__add__(s1,s2)` adds zeroes to the smaller list until it is the same length as the larger one, then adds each term to reach a sum

`__sub__(s1,s2)` does the same process as addition but with subtraction in each term

`__mul__(s1,s2)` uses nested `for` loops and addition to expand and multiply polynomials

`rootdiv(self,rt)` uses the process of synthetic division to factor out a root from a polynomial; don't use this unless you already know that `rt` is a root of the polynomial

`val(self,x)` uses the coefficients and exponents to evaluate a polynomial at an input `x`

`dvt(self)` uses the power rule to return a derivative polynomial

`itg(self,C=0)` cannot compute real integration, but rather returns an antiderivative of the polynomial with a given C-value assumed to be 0

`solve(self,y=0)` uses `newton` and `rootdiv`to find an approximate solution to a polynomial, then factor it out and repeat the process, finding all solutions to any polynomial at value `y`

### **More polynomial functions**

`newton(p,y=0)` uses Newton's method to approximate an x-value such that `p.val(x) == y`, or simply the solutions of a polynomial

`rnewton(p,y=0)` is just `newton` but only tolerating real inputs and outputs (the starting seed value is real, so the root it finds will always be real)

`sqrt(x)` creates the polynomial `poly([1,0,0])` or x2 and solves it for a given value

`cbrt(x)` is the same process, just with a cubic x3

`root(n,x)` is the general radical, creating a polynomial with any amount of zeroes to find the nth-roots of an input

`buildp(rootlist)` takes a list of numbers and builds a polynomial with those numbers as its roots

### **Funky exponential stuff**

`exp(x)` uses an order-12 Taylor polynomial to approximate the exponential function e^x evaluated around x=0

`ixp(x)` is shorthand for e^ix or `exp(ii*x)`

`realn(x)` range-fixes real logarithm inputs, then uses Newton's method on the Taylor polynomial to approximate the natural logarithm

`ln(x)` separates an input's absolute value and corresponding unit-circle value, then uses `realn` and `newton` to reach the natural logarithms of each and combines them

`log(n,x)` uses `log(n,x) == ln(x) / ln(n)` to compute logarithms of any base

### **`class angle:` Angle objects and more!**

`__init__(self,me,mx=1)` creates an angle object given a measure and a maximum representing the measure of a full circle; in this notation, 30° is `angle(30,360)` and one-third of a circle is `angle(1,3)` - this function also fixes the measure to a value between 0 and 1

`__repr__(self)` returns/prints the angle in terms of π, which is very helpful

`__add__(s1,s2)` adds two angle measures together

`__sub__(s1,s2)` subtracts two angles' measures

`sin(self), cos(self), tan(self), csc(self), sec(self),` and `cot(self)` use the exponential function to approximate trigonometric functions on angles

`asin(x), acos(x), atan(x), acsc(x), asec(x),` and `acot(x)` use natural logarithms and square roots to perform inverse trigonometric functions, returning an angle object

### **`class polar:` Complex numbers in polar form**

`__init__(self,radius,angle):` creates the object while measure-fixing the angle

`__repr__(self)` creates a string with the angle in terms of π

`__neg__(self)` adds π to the angle to negate the complex number

`__mul__(s1,s2)` multiplies objects by multiplying radii and adding angles

`__truediv__(s1,s2)` divides objects by dividing radii and subtracting angles

### **`class frac:` Rational number objects**

`gcf(n1,n2)` finds the greatest common factor of two natural numbers

`__init__(self,den=1)` creates a rational object by simplifying a numerator and denominator

`__repr__(self)` displays the fraction

`__mul__(s1,s2)` multiplies fractions very simply

`inv(self)` creates the reciprocal of a fraction

`__truediv__(s1,s2)` divides fractions very simply

`__add__(s1,s2)` adds fractions with a few multiplication operations

`__sub__(s1,s2)` subtracts fractions with a few multiplication operations

### **`quat.py`: Quaternions!**

`__init__(self,real,imag,jmag,kmag)` takes four real numbers as coefficients to create a quaternion object

`__repr__(self)` creates a quaternion string similar to that of `comp`s

`__neg__(self)` negates all coefficients to negate the quaternion

`__add__(s1,s2)` adds all coefficients to add quaternions

`__sub__(s1,s2)` subtracts all coefficients to subtract quaternions

`__mul__(s1,s2)` is strange becuase quaternion multiplication is non-commutative, but uses just a few multiplications and additions to properly multiply quaternions

`conj(self)` negates all imaginary part coefficents to create a quaternion conjugate

`inv(self)` uses the conjugate to compute the inverse of a quaternion

`__truediv__(s1,s2)` simply multiplies one quaternion by the other's inverse to divide quaternions properly

### **`fractal.py`: Fractals!**

`ispace(func,c,size=128,iterate=32)` uses a given, defined function's convergence and divergence to plot an input space fractal for a given value `c`

`pspace(func,c,size=128,iterate=32)` uses a given, defined function's convergence and divergence to plot a parameter space fractal for starting value `section`

`quadra` more efficiently plots the famous input space for `z2 + c`, and `mandelbrot` plots its even more famous parameter space

*more coming soon (some of it might be on `todo.md`)*