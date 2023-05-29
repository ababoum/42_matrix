#!/usr/bin/env python3

from vector import Vector
from matrix import Matrix
from my_complex import Complex

if __name__ == "__main__":

    print('#' * 80)
    print("COMPLEX NUMBERS --- EX00\n\n")
    print('#' * 80)
    u = Vector([Complex(2., 1.), Complex(3., 4.)])
    v = Vector([Complex(1., 2.), Complex(5., 6.)])

    print(u + v)
    print(u - v)
    print(u * 2)
    print(2 * u)

    print('#' * 15)

    u = Matrix([[Complex(1, 2), Complex(3, 4)],
               [Complex(5, 6), Complex(7, 8)]])
    v = Matrix([[Complex(5.5, 7.5), Complex(8.5, 0.5)],
               [Complex(9.5, 1.5), Complex(2.5, 3.5)]])

    print(u + v)
    print(u - v)
    print(2 * u)

    print('#' * 80)
    print("COMPLEX NUMBERS --- EX01\n\n")
    print('#' * 80)