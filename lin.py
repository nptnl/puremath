def makix(rows, cols):
    if cols == 1:
        return vec(rows)
    return matrix(rows, cols)
def vecs_to_cols(vecs):
    result = matrix(len(vecs[0].D[0]), len(vecs))
    for each in range(len(vecs)):
        result.D[each] = vecs[each].D[0]
    return result
def cols_to_vecs(mtx):
    result = []
    for col in mtx.D:
        next = vec(mtx.rows)
        next.D[0] = col
        result.append(next)
    return result
def diag(values):
    result = matrix(len(values), len(values))
    for indx in range(len(values)):
        result.D[indx][indx] = values[indx]
    return result
def identity(dim):
    result = matrix(dim, dim)
    for indx in range(dim):
        result.D[indx][indx] = 1
    return result
def zerovec(dim):
    result = vec(dim)
    for indx in range(dim):
        result.D[0][indx] = 0
    return result

def sqrt(x):
    t1, t2 = 2.0, 1.0
    while abs(t2 - t1) > 0.0001:
        t1 = t2
        t2 -= 0.5*(t2*t2 - x) / t2
    return t2

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
    def clone(self):
        result = makix(self.rows, self.cols)
        for col in range(self.cols):
            for row in range(self.rows):
                result.D[col][row] = self.D[col][row]
        return result
    def inverse(self):
        if self.cols != self.rows:
            raise ValueError("matrix is not square for inverse")
        if self.det() == 0:
            raise ValueError("matrix is singular as self.det() == 0")
        aug = self.clone()
        aug.augment(identity(self.cols))
        aug.reduce()
        result = matrix(self.cols, self.cols)
        result.D = aug.D[self.cols:]
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
    def cut(self, cut_row, cut_col):
        result = matrix(self.rows - 1, self.cols - 1)
        col_add = 0
        for col in range(self.cols):
            row_add = 0
            if col == cut_col:
                col_add = -1
                continue
            for row in range(self.rows):
                if row == cut_row:
                    row_add = -1
                    continue
                result.D[col + col_add][row + row_add] = self.D[col][row]
        return result
    def slice(self, indx):
        data = []
        if indx < 0:
            result = matrix(self.rows, -indx)
            for col in range(indx, 0):
                data.append(self.D[col])
            result.D = data
            return result
        else:
            result = matrix(self.rows, indx)
            for col in range(0, indx):
                data.append(self.D[col])
            result.D = data
            return result

    def det(self):
        if self.rows != self.cols:
            raise ValueError("matrix must be square to have a determinant")
        if self.rows == 1:
            return self.D[0][0]
        elif self.rows == 2:
            return self.D[0][0] * self.D[1][1] - self.D[0][1] * self.D[1][0]
        tot = 0
        multi = 1
        for cut_row in range(self.rows):
            tot += self.D[0][cut_row] * self.cut(cut_row, 0).det() * multi
            multi = -multi
        return tot
    
    def rowop_swap(self, row1, row2):
        for col in range(self.cols):
            self.D[col][row1], self.D[col][row2] = self.D[col][row2], self.D[col][row1]
    def rowop_add(self, onto_row, from_row, factor):
        for col in range(self.cols):
            self.D[col][onto_row] += self.D[col][from_row] * factor
    def rowop_scl(self, row, factor):
        for col in range(self.cols):
            self.D[col][row] *= factor
    def put_value_in_topleft(self, runcol, runrow):
        if self.D[runcol][runrow] != 0:
            return 0
        for possible_row in range(runrow, self.rows):
            if self.D[runcol][possible_row] != 0:
                self.rowop_swap(runrow, possible_row)
                return 1
        return 2
    def rid_column_below(self, runcol, runrow):
        for possible_row in range(runrow+1, self.rows):
            if self.D[runcol][possible_row] != 0:
                factor = - self.D[runcol][possible_row] / self.D[runcol][runrow]
                self.rowop_add(possible_row, runrow, factor)
                self.D[runcol][possible_row] = 0
    def rid_column_above(self, runcol, runrow):
        for possible_row in range(runrow):
            if self.D[runcol][possible_row] != 0:
                factor = - self.D[runcol][possible_row] / self.D[runcol][runrow]
                self.rowop_add(possible_row, runrow, factor)
                self.D[runcol][possible_row] = 0
    def echelon(self):
        result = self.clone()
        runcol = 0
        for runrow in range(self.rows):
            pivot_in_this_col = result.put_value_in_topleft(runcol, runrow)
            if pivot_in_this_col != 2:
                result.rid_column_below(runcol, runrow)
                runcol += 1
        return result
    def echelon_without_swaps(self):
        result = self.clone()
        runcol = 0
        for runrow in range(self.rows):
            pivot_in_this_col = result.put_value_in_topleft(runcol, runrow)
            if pivot_in_this_col == 1:
                raise ValueError("cannot be echelon-ed without swaps!")
            if pivot_in_this_col == 0:
                result.rid_column_below(runcol, runrow)
                runcol += 1
        return result
    def reduce(self):
        result = self.clone()
        runcol = 0
        for runrow in range(self.rows):
            pivot_in_this_col = result.put_value_in_topleft(runcol, runrow)
            if pivot_in_this_col != 2:
                result.rid_column_above(runcol, runrow)
                result.rid_column_below(runcol, runrow)
                result.rowop_scl(runrow, 1.0 / result.D[runcol][runrow])
                runcol += 1
        return result
    def augment(self, extra):
        if self.rows != extra.rows:
            raise ValueError("augmentation dimensions do not match")
        result = matrix(self.rows, self.cols + extra.cols)
        data = []
        for col in self.D:
            data.append(col)
        for col in extra.D:
            data.append(col)
        result.D = data
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
            return super().__mul__(other)
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
    def mag1(self):
        return sqrt(self.mag2())
    def proj(self, other):
        if other.mag2() == 0:
            return other
        return other.scl( (self * other) / (other.mag2()) )
    def unit(self):
        return self.scl(1.0 / self.mag1())

def gram_smit(spanning):
    result = []
    for inp in spanning:
        next = inp.clone()
        for ortho in result:
            next -= inp.proj(ortho)
        result.append(next)
    return result
def normal_gram_smit(spanning):
    result = gram_smit(spanning)
    for indx in range(len(result)):
        result[indx] = result[indx].unit()
    return result

def factor_lu(A):
    # A = L U
    # A must be echelon-able without swap operations
    # L is lower triangular
    # U is upper triangular

    run1 = A.augment(identity(A.rows)).echelon_without_swaps()
    U = run1.slice(A.cols)
    run2 = run1.slice(-A.rows).augment(identity(A.rows)).reduce()
    L = run2.slice(-A.rows)
    return L, U
def factor_qr(A):
    # A = Q R
    # A must have independent cols
    # Q is orthogonal
    # R is upper triangular

    Q = vecs_to_cols( normal_gram_smit( cols_to_vecs(A) ) )
    R = Q.transpose() * A
    return Q, R