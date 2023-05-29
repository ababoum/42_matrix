'''Complex number class.'''

from my_math import ft_abs


class Complex():
    def __init__(self, real, imaginary) -> None:
        self.real = real
        self.imaginary = imaginary

    def __str__(self) -> str:
        return f'{self.real} {("+", "-")[self.imaginary < 0]} {ft_abs(self.imaginary)}i'

    def __repr__(self) -> str:
        return f'{self.real} {("+", "-")[self.imaginary < 0]} {ft_abs(self.imaginary)}i'

    def __add__(self, other):
        if isinstance(other, Complex):
            return Complex(self.real + other.real, self.imaginary + other.imaginary)
        elif isinstance(other, (int, float)):
            return Complex(self.real + other, self.imaginary)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, Complex):
            return Complex(self.real - other.real, self.imaginary - other.imaginary)
        elif isinstance(other, (int, float)):
            return Complex(self.real - other, self.imaginary)

    def __rsub__(self, other):
        return self.__add__(-1 * other)

    def __mul__(self, other):
        if isinstance(other, Complex):
            return Complex(self.real * other.real - self.imaginary * other.imaginary, self.real * other.imaginary + self.imaginary * other.real)
        elif isinstance(other, (int, float)):
            return Complex(self.real * other, self.imaginary * other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, Complex):
            return Complex((self.real * other.real + self.imaginary * other.imaginary) / (other.real * other.real + other.imaginary * other.imaginary),
                           (self.imaginary * other.real - self.real * other.imaginary) / (other.real * other.real + other.imaginary * other.imaginary))
        elif isinstance(other, (int, float)):
            return Complex(self.real / other, self.imaginary / other)

    def __rtruediv__(self, other):
        if isinstance(other, Complex):
            return Complex((other.real * self.real + other.imaginary * self.imaginary) / (self.real * self.real + self.imaginary * self.imaginary),
                           (other.imaginary * self.real - other.real * self.imaginary) / (self.real * self.real + self.imaginary * self.imaginary))
        elif isinstance(other, (int, float)):
            return Complex(other / self.real, other / self.imaginary)

    def __eq__(self, other):
        if isinstance(other, (int, float)):
            return self.real == other and self.imaginary == 0
        elif isinstance(other, Complex):
            return self.real == other.real and self.imaginary == other.imaginary
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)
