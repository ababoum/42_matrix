from my_complex import Complex
from my_math import ft_pow
from vector import Vector


class Matrix():
    def __init__(self, *args) -> None:
        if len(args) == 1 and len(args[0]) != 0 and len(args[0][0]) != 0:
            if (isinstance(args[0], list) and all(isinstance(i, list)) for i in args[0]):
                if all(len(j) == len(args[0][0]) and all(isinstance(k, (float, int, Complex)) for k in j) for j in args[0]):
                    self.values = args[0]
                    self.shape = (len(args[0]), len(args[0][0]))
                else:
                    raise TypeError(
                        "Matrix must be a list of lists of numbers of the same size")
            else:
                raise TypeError("Matrix must be a list of lists of numbers")
        else:
            raise TypeError("Matrix must be a list of lists of numbers")

    def __str__(self) -> str:
        return "Matrix ({})".format('\n\t'.join(map(str, self.values)))

    def __repr__(self) -> str:
        return "Matrix ({})".format('\n\t'.join(map(str, self.values)))

    def __add__(self, other):
        if isinstance(other, Matrix):
            if self.shape == other.shape:
                return Matrix([[self.values[i][j] + other.values[i][j] for j in range(len(self.values[0]))] for i in range(len(self.values))])
            else:
                raise TypeError("Cannot add matrices of different sizes")
        else:
            raise TypeError("Cannot add matrix to non-matrix")

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, Matrix):
            if self.shape == other.shape:
                return Matrix([[self.values[i][j] - other.values[i][j] for j in range(len(self.values[0]))] for i in range(len(self.values))])
            else:
                raise TypeError("Cannot subtract matrices of different sizes")
        else:
            raise TypeError("Cannot subtract matrix from non-matrix")

    def __rsub__(self, other):
        if isinstance(other, Matrix):
            other.__sub__(self)
        else:
            raise TypeError("Cannot subtract non-matrix from matrix")

    def __mul__(self, other):
        if isinstance(other, (float, int, Complex)):
            return Matrix([[i * other for i in j] for j in self.values])
        elif isinstance(other, Matrix):
            if self.shape[1] == other.shape[0]:
                return Matrix([[sum([self.values[i][k] * other.values[k][j] for k in range(len(self.values[0]))]) for j in range(len(other.values[0]))] for i in range(len(self.values))])
            else:
                raise TypeError("Cannot multiply matrices of different sizes")
        elif isinstance(other, Vector):
            if other.type == "column" and self.shape[1] == other.size():
                # returns a column vector
                return Vector([
                    [sum([self.values[i][j] * other[j]
                         for j in range(other.size())])]
                    for i in range(len(self.values))
                ])
            else:
                raise TypeError(
                    "Cannot multiply matrix and vector of different sizes")
        else:
            raise TypeError("Cannot multiply matrix by non-matrix")

    def __rmul__(self, other):
        if isinstance(other, (float, int)):
            return self.__mul__(other)
        elif isinstance(other, Matrix):
            other.__mul__(self)
        elif isinstance(other, Vector):
            if other.type == "row" and self.shape[0] == other.size():
                # returns a row vector
                return Vector([sum([self.values[i][j] * other[j] for j in range(len(other))]) for i in range(len(self.values))])
            else:
                raise TypeError(
                    "Cannot multiply matrix and vector of different sizes")
        else:
            raise TypeError("Cannot multiply non-matrix by matrix")

    ##### SUBMATRIX #####
    def submatrix(self, i, j):
        return Matrix([
            [self.values[x][k] for k in range(self.shape[1]) if k != j]
            for x in range(self.shape[0]) if x != i
        ])

    ##### TRACE #####

    def trace(self):
        if self.shape[0] == self.shape[1]:
            return sum([self.values[i][i] for i in range(len(self.values))])
        else:
            raise TypeError("Cannot find trace of non-square matrix")

    ##### TRANSPOSE #####

    def transpose(self):
        return Matrix([[self.values[j][i]for j in range(len(self.values))] for i in range(len(self.values[0]))])

    def conjugate_transpose(self):
        return Matrix([
            [self.values[j][i].conjugate() if isinstance(self.values[j][i], Complex) else self.values[j][i]
             for j in range(len(self.values))]
            for i in range(len(self.values[0]))])

    ##### ROW ECHELON FORM #####

    def row_echelon_form(self):
        rref = self.values.copy()
        m = self.shape[0]
        n = self.shape[1]

        r = 0
        # Step 1: Begin with the leftmost nonzero column. This is a pivot column. The pivot position is at the top.
        for j in range(n):
            if not all(rref[i][j] == 0 for i in range(m)):
                # Step 2: Select a nonzero entry in the pivot column as a pivot. If necessary, interchange rows to move this entry into the pivot position.
                i = r
                while i < m and rref[i][j] == 0:
                    i += 1
                if i < m:
                    rref[r], rref[i] = rref[i], rref[r]
                else:
                    continue
                # Step 3: Use row replacement operations to create zeros in all positions in the pivot column
                for i in range(m):
                    if rref[i][j] != 0 and i != r:
                        rref[i] = [rref[i][k] - rref[r][k] * rref[i][j] / rref[r][j]
                                   for k in range(n)]
                # Divide the pivot row by the pivot element to make the pivot element 1.
                rref[r] = [rref[r][k] / rref[r][j] for k in range(n)]
                rref[r] = [0.0 if x == -0.0 else x for x in rref[r]]
                r += 1
                if r == m:
                    break
        return Matrix(rref)

    ##### DETERMINANT #####

    def determinant(self):
        if self.shape[0] == self.shape[1]:
            if self.shape[0] == 1:
                return self.values[0][0]
            elif self.shape[0] == 2:
                return self.values[0][0] * self.values[1][1] - self.values[0][1] * self.values[1][0]
            elif self.shape[0] == 3:
                return self.values[0][0] * self.submatrix(0, 0).determinant() \
                    - self.values[0][1] * self.submatrix(0, 1).determinant() \
                    + self.values[0][2] * \
                    self.submatrix(0, 2).determinant()
            elif self.shape[0] == 4:
                return self.values[0][0] * self.submatrix(0, 0).determinant() \
                    - self.values[0][1] * self.submatrix(0, 1).determinant() \
                    + self.values[0][2] * self.submatrix(0, 2).determinant() \
                    - self.values[0][3] * \
                    self.submatrix(0, 3).determinant()
            else:
                raise TypeError(
                    "Cannot find determinant of matrix larger than 4x4")
        else:
            raise TypeError("Cannot find determinant of non-square matrix")

    ##### INVERSE #####

    def inverse(self):
        if self.shape[0] != self.shape[1]:
            raise TypeError("Cannot find inverse of non-square matrix")
        elif self.determinant() == 0:
            raise TypeError("Cannot find inverse of singular matrix")
        else:
            return Matrix([
                [ft_pow(-1, i + j) * self.submatrix(i, j).determinant()
                 for j in range(self.shape[1])]
                for i in range(self.shape[0])
            ]).transpose() * (1 / self.determinant())

    ##### RANK #####

    def rank(self):
        return self.row_echelon_form().shape[0] - \
            sum([all(i == 0 for i in j)
                for j in self.row_echelon_form().values])
