from my_math import ft_abs, ft_sqrt
from my_complex import Complex


class Vector():
    def __init__(self, *args) -> None:
        if len(args) == 1:
            # Row vector
            if isinstance(args[0], list) and all(isinstance(i, (float, int, Complex)) for i in args[0]):
                self.values = args[0]
                self.shape = (1, len(args[0]))
                self.type = "row"
            # Column vector
            elif isinstance(args[0], list) and all(isinstance(i, list) for i in args[0]) and \
                    all(len(i) == 1 for i in args[0]) and all(isinstance(i[0], (float, int, Complex)) for i in args[0]):
                self.values = args[0]
                self.shape = (len(args[0]), 1)
                self.type = "column"
            else:
                raise TypeError(
                    "Vector must be a list of numbers or a list of singleton-lists of numbers")
        else:
            raise TypeError(
                "Vector must be a list of numbers or a list of singleton-lists of numbers")

    def size(self) -> int:
        return len(self.values)

    def __str__(self) -> str:
        if self.type == 'column':
            return "Vector ({})".format('\n\t'.join(map(str, self.values)))
        return "Vector ({})".format(self.values)

    def __repr__(self) -> str:
        if self.type == 'column':
            return "Vector ({})".format('\n\t'.join(map(str, self.values)))
        return "Vector ({})".format(self.values)

    def __add__(self, other):
        if isinstance(other, Vector):
            if self.shape == other.shape:
                return Vector([self.values[i] + other.values[i] for i in range(len(self.values))])
            else:
                raise TypeError("Cannot add vectors of different sizes")
        else:
            raise TypeError("Cannot add vector to non-vector")

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, Vector):
            if self.shape == other.shape:
                return Vector([self.values[i] - other.values[i] for i in range(len(self.values))])
            else:
                raise TypeError("Cannot subtract vectors of different sizes")
        else:
            raise TypeError("Cannot subtract vector from non-vector")

    def __rsub__(self, other):
        if isinstance(other, Vector):
            other.__sub__(self)
        else:
            raise TypeError("Cannot subtract non-vector from vector")

    def __mul__(self, other):
        if isinstance(other, (float, int)):
            return Vector([i * other for i in self.values])
        elif isinstance(other, Vector):
            if self.shape == other.shape:
                return sum([self.values[i] * other.values[i] for i in range(len(self.values))])
            else:
                raise TypeError("Cannot multiply vectors of different sizes")
        else:
            raise TypeError("Cannot multiply vector by non-vector")

    def __rmul__(self, other):
        if isinstance(other, (float, int)):
            return self.__mul__(other)
        else:
            if isinstance(other, Vector):
                return other.__mul__(self)

    def __getitem__(self, key):
        if self.type == 'row':
            return self.values[key]
        elif self.type == 'column':
            return self.values[key][0]
        else:
            raise Exception("Vector type not recognized")

    ##### DOT PRODUCT #####

    def dot(self, other) -> float:
        if isinstance(other, Vector):
            if self.shape == other.shape:
                if self.type == 'row':
                    right_operand = Vector([other.values[i].conjugate() if isinstance(
                        other.values[i], Complex) else other.values[i] for i in range(len(other.values))])
                    return sum([
                        self.values[i] * right_operand.values[i]
                        for i in range(len(self.values))
                    ])
                elif self.type == 'column':
                    right_operand = Vector([other.values[i][0].conjugate() if isinstance(
                        other.values[i][0], Complex) else other.values[i][0] for i in range(len(other.values))])
                    return sum([self.values[i][0] * right_operand[i] for i in range(len(self.values))])
                else:
                    raise Exception("Vector type not recognized")
            else:
                raise TypeError(
                    "Cannot dot product vectors of different sizes")
        else:
            raise TypeError(
                "Cannot compute dot product of vector with non-vector")

    ##### NORMS #####

    def norm_1(self):
        if self.type == 'row':
            return sum([ft_abs(i, type='manhattan') for i in self.values])
        elif self.type == 'column':
            return sum([ft_abs(i[0], type='manhattan') for i in self.values])
        else:
            raise Exception("Vector type not recognized")

    def norm(self):
        if self.type == 'row':
            return ft_sqrt(sum([ft_abs(i) * ft_abs(i) for i in self.values]))
        elif self.type == 'column':
            return ft_sqrt(sum([ft_abs(i[0]) * ft_abs(i[0]) for i in self.values]))
        else:
            raise Exception("Vector type not recognized")

    def norm_inf(self):
        if self.type == 'row':
            return max([ft_abs(i) for i in self.values])
        elif self.type == 'column':
            return max([ft_abs(i[0]) for i in self.values])
        else:
            raise Exception("Vector type not recognized")
