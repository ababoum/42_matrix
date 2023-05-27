class Matrix():
    def __init__(self, *args) -> None:
        if len(args) == 0:
            self.values = []
            self.shape = (0, 0)
        elif len(args) == 1:
            if (isinstance(args[0], list) and all(isinstance(i, list)) for i in args[0]):
                if all(len(j) == len(args[0][0]) and all(isinstance(k, (float, int)) for k in j) for j in args[0]):
                    self.values = args[0]
                    self.shape = (len(args), len(args[0]))
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
        if isinstance(other, (float, int)):
            return Matrix([[i * other for i in j] for j in self.values])
        elif isinstance(other, Matrix):
            if self.shape[1] == other.shape[0]:
                return Matrix([[sum([self.values[i][k] * other.values[k][j] for k in range(len(self.values[0]))]) for j in range(len(other.values[0]))] for i in range(len(self.values))])
            else:
                raise TypeError("Cannot multiply matrices of different sizes")
        else:
            raise TypeError("Cannot multiply matrix by non-matrix")

    def __rmul__(self, other):
        if isinstance(other, (float, int)):
            return self.__mul__(other)
        elif isinstance(other, Matrix):
            other.__mul__(self)
        else:
            raise TypeError("Cannot multiply non-matrix by matrix")
