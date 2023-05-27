class Vector():
    def __init__(self, *args) -> None:
        if len(args) == 0:
            self.values = []
            self.shape = (0, 0)

        elif len(args) == 1:
            # Row vector
            if isinstance(args[0], list) and all(isinstance(i, (float, int)) for i in args[0]):
                self.values = args[0]
                self.shape = (1, len(args[0]))
                self.type = "row"
            # Column vector
            elif isinstance(args[0], list) and all(isinstance(i, list) for i in args[0]) and \
                    all(len(i) == 1 for i in args[0]) and all(isinstance(i[0], (float, int)) for i in args[0]):
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
        return "Vector ({})".format(self.values)

    def __repr__(self) -> str:
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

    ##### DOT PRODUCT #####

    def dot(self, other):
        if isinstance(other, Vector):
            if self.shape == other.shape:
                if self.type == 'row':
                    return sum([self.values[i] * other.values[i] for i in range(len(self.values))])
                elif self.type == 'column':
                    return sum([self.values[i][0] * other.values[i][0] for i in range(len(self.values))])
                else:
                    raise Exception("Vector type not recognized")
            else:
                raise TypeError(
                    "Cannot dot product vectors of different sizes")
        else:
            raise TypeError(
                "Cannot compute dot product of vector with non-vector")
