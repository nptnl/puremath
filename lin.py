def makix(rows, cols):
    if cols == 1:
        return vec(rows)
    return matrix(rows, cols)
def vecs_to_cols(vecs):
    result = matrix(len(vecs[0].D[0]), len(vecs))
    for each in range(len(vecs)):
        result.D[each] = vecs[each].D[0]
    return result

class matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.D = [[0 for _row in range(rows)] for _col in range(cols)]
    def __repr__(self):
        return '\n'.join([' '.join([str(self.D[col][row]) for col in range(self.cols)]) for row in range(self.rows)])
    def __add__(self, other):
        if self.cols != other.cols or self.rows != other.rows:
            raise ValueError("matrix dimensions don't match for addition")
        result = makix(self.rows, self.cols)
        for col in range(self.cols):
            for entry in range(self.rows):
                result.D[col][entry] = self.D[col][entry] + other.D[col][entry]
        return result
    def __sub__(self, other):
        if self.cols != other.cols or self.rows != other.rows:
            raise ValueError("matrix dimensions don't match for subtraction")
        result = makix(self.rows, self.cols)
        for col in range(self.cols):
            for entry in range(self.rows):
                result.D[col][entry] = self.D[col][entry] - other.D[col][entry]
        return result
    def __mul__(self, other):
        if self.cols != other.rows:
            raise ValueError("matrix dimensions incompatible for multiplication")
        result = makix(self.rows, other.cols)
        for col in range(other.cols):
            for row in range(self.rows):
                entry = 0
                for each in range(self.cols):
                    entry += self.D[each][row] * other.D[col][each]
                result.D[col][row] = entry
        return result
    def transpose(self):
        result = makix(self.cols, self.rows)
        for row in range(self.rows):
            for col in range(self.cols):
                result.D[row][col] = self.D[col][row]
        return result
    def scl(self, factor):
        result = makix(self.rows, self.cols)
        for col in range(self.cols):
            for row in range(self.rows):
                result.D[col][row] = self.D[col][row] * factor
        return result

class vec(matrix):
    def __init__(self, dim):
        self.rows = dim
        self.cols = 1
        self.D = [[0 for _entry in range(dim)]]
    def __repr__(self):
        return '\n'.join([str(self.D[0][entry]) for entry in range(self.rows)])
    def __mul__(self, other):
        if other.cols != 1:
            return super()
        if other.rows != self.rows:
            raise ValueError("vector dimensions do not match for dot product")
        tot = 0
        for entry in range(self.rows):
            tot += self.D[0][entry] * other.D[0][entry]
        return tot
    def mag2(self):
        tot = 0
        for entry in self.D[0]:
            tot += entry * entry
        return tot
    def proj(self, other):
        if other.mag2() == 0:
            return other
        return other.scl( (self * other) / (other.mag2()) )