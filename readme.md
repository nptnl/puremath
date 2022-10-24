# based math has arrived

## class comp:
Complex numbers but they use i instead of j
(more based)

Addition, subtraction, multiplication, and division work fine, but there's no exponentiation yet

## class poly:
Polynomials as lists in form `poly([a,b,c]) == ax2 + bx + c`
(with style)

Addition, subtraction, and multiplication work properly, but no polynomial long division

Also we have `self.val(x)`, `self.dvt`, and `self.itg` for evalutation, differentiation, and integration
*(integration just returns an anti-derivative polynomial, assuming C = 0)*

Instead there is `self.rootdiv(rt)`, using synthetic division to factor out a root

`self.solve()` uses Newton's method and synthetic division to find all solutions to any polynomial (my crowning achievement)

`exp(x)` uses a Taylor series to evaluate the exponential function

`ln(x)` uses Newton's method on the exponential Taylor series for the natural logarithm, and `log(n,x)` uses `ln(x)/ln(n)`

`sqrt(x)` and `cbrt(x)` return all valid roots

## class angle:
Angle objects in terms of π, compatible with any measuring unit
(also with complex trig)

Angles can add, subtract, and multiply/divide by a scalar.

Trig functions `self.sin(), self.cos(), self.tan(), self.csc(), self.sec(), self.cot()` use the exponential Taylor series to do trig stuff

Inverse trig functions `asin(x), acos(x), atan(x), acsc(x), asec(x), acot(x)` use square roots and the natural logarithm to output angle values for inverse trig functions
