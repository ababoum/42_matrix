#!/usr/bin/env python3

from vector import Vector
from matrix import Matrix
from my_complex import Complex
from ex01 import linear_combination
from ex02 import lerp
from ex05 import angle_cos

if __name__ == "__main__":

    # print('#' * 80)
    # print("\n\nCOMPLEX NUMBERS --- EX00\n\n")
    # print('#' * 80)
    # u = Vector([Complex(2., 1.), Complex(3., 4.)])
    # v = Vector([Complex(1., 2.), Complex(5., 6.)])

    # print(u + v)
    # print(u - v)
    # print(u * 2)
    # print(2 * u)

    # print('#' * 15)

    # u = Matrix([[Complex(1, 2), Complex(3, 4)],
    #            [Complex(5, 6), Complex(7, 8)]])
    # v = Matrix([[Complex(5.5, 7.5), Complex(8.5, 0.5)],
    #            [Complex(9.5, 1.5), Complex(2.5, 3.5)]])

    # print(u + v)
    # print(u - v)
    # print(2 * u)

    # print('#' * 80)
    # print("\n\nCOMPLEX NUMBERS --- EX01\n\n")
    # print('#' * 80)

    # e1 = Vector([Complex(1., 0.), Complex(0., 0.), Complex(0., 0.)])
    # e2 = Vector([Complex(0., 0.), Complex(1., 0.), Complex(0., 0.)])
    # e3 = Vector([Complex(0., 0.), Complex(0., 0.), Complex(1., 0.)])

    # v1 = Vector([Complex(1., 0.), Complex(2., 0.), Complex(3., 0.)])
    # v2 = Vector([Complex(0., 0.), Complex(10., 0.), Complex(-100., 0.)])

    # print(linear_combination([e1, e2, e3], [10., -2., 0.5]))
    # print(linear_combination([v1, v2], [10., -2.]))

    # print('#' * 80)
    # print("\n\nCOMPLEX NUMBERS --- EX02\n\n")
    # print('#' * 80)

    # print(lerp(Complex(0., 1.), Complex(1., 0.), 0.))
    # print(lerp(Complex(0., 1.), Complex(1., 0.), 1.))
    # print(lerp(Complex(0., 1.), Complex(1., 0.), 0.5))
    # print(lerp(Complex(21., 42.), Complex(42., 21.), 0.3))

    # print('*' * 20)

    # print(lerp(Vector([Complex(2., 1.), Complex(4., 2.)]),
    #         Vector([Complex(20., 10.), Complex(30., 40.)]), 0.5))
    # print(lerp(Matrix([[Complex(2., 1.), Complex(3., 4.)],
    #                     [Complex(4., 2.), Complex(5., 6.)]]),
    #         Matrix([[Complex(20., 10.), Complex(30., 40.)],
    #                 [Complex(40., 20.), Complex(50., 60.)]]), 0.5))

    # print('#' * 80)
    # print("\n\nCOMPLEX NUMBERS --- EX03\n\n")
    # print('#' * 80)

    # u = Vector([Complex(0., 0.), Complex(0., 0.)])
    # v = Vector([Complex(1., 1.), Complex(1., 1.)])

    # print(u.dot(v))
    # print(v.dot(u))

    # print('*' * 20)

    # u = Vector([Complex(1., 1.), Complex(1., 1.)])
    # v = Vector([Complex(1., 1.), Complex(1., 1.)])

    # print(u.dot(v))
    # print(v.dot(u))

    # print('*' * 20)

    # u = Vector([Complex(-1., 6.), Complex(3., 2.)])
    # v = Vector([Complex(3., 2.), Complex(-1., 6.)])

    # print(u.dot(v))
    # print(v.dot(u))

    # print('#' * 80)
    # print("\n\nCOMPLEX NUMBERS --- EX04\n\n")
    # print('#' * 80)

    # u = Vector([Complex(0., 0.), Complex(0., 0.), Complex(0., 0.)])
    # print(f'{u.norm_1()}, {u.norm()}, {u.norm_inf()}')

    # u = Vector([Complex(1., 2.), Complex(3., 4.), Complex(5., 6.)])
    # print(f'{u.norm_1()}, {u.norm()}, {u.norm_inf()}')

    # u = Vector([Complex(-1., -2.), Complex(-3., -4.)])
    # print(f'{u.norm_1()}, {u.norm()}, {u.norm_inf()}')

    print('#' * 80)
    print("\n\nCOMPLEX NUMBERS --- EX05\n\n")
    print('#' * 80)

    u = Vector([Complex(1., 0.), Complex(0., 0.)])
    v = Vector([Complex(1., 0.), Complex(0., 0.)])
    print(angle_cos(u, v))

    u = Vector([Complex(1., 0.), Complex(0., 0.)])
    v = Vector([Complex(0., 0.), Complex(1., 0.)])
    print(angle_cos(u, v))

    u = Vector([Complex(-1., 1.), Complex(1., -1.)])
    v = Vector([Complex(1., -1.), Complex(-1., 1.)])
    print(angle_cos(u, v))

    u = Vector([Complex(2., 1.), Complex(1., 2.)])
    v = Vector([Complex(4., 2.), Complex(2., 4.)])
    print(angle_cos(u, v))

    u = Vector([Complex(1., 2.), Complex(3., 4.), Complex(5., 6.)])
    v = Vector([Complex(4., 5.), Complex(6., 7.), Complex(8., 9.)])
    print(angle_cos(u, v))

    print('#' * 80)
    print("\n\nCOMPLEX NUMBERS --- EX06\n\n")
    print('#' * 80)
