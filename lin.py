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
        for possible_row in range(runrow, self.rows):
            if self.D[runcol][possible_row] != 0:
                self.rowop_swap(runrow, possible_row)
                return True
        return False
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
        runcol = 0
        for runrow in range(self.rows):
            pivot_in_this_col = self.put_value_in_topleft(runcol, runrow)
            if pivot_in_this_col:
                self.rid_column_below(runcol, runrow)
                runcol += 1
            runrow += 1
    def reduce(self):
        runcol = 0
        for runrow in range(self.rows):
            pivot_in_this_col = self.put_value_in_topleft(runcol, runrow)
            if pivot_in_this_col:
                self.rid_column_above(runcol, runrow)
                self.rid_column_below(runcol, runrow)
                self.rowop_scl(runrow, 1.0 / self.D[runcol][runrow])
                runcol += 1
            runrow += 1
    def augment(self, extra):
        if self.rows != len(extra[0]):
            raise ValueError("augmentation dimensions do not match")
        self.cols += len(extra)
        for col in extra:
            self.D.append(col)


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