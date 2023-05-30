#!/usr/bin/env python3

from vector import Vector
from matrix import Matrix
from my_complex import Complex
from ex01 import linear_combination
from ex02 import lerp
from ex05 import angle_cos
from ex06 import cross_product

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

    # print('#' * 80)
    # print("\n\nCOMPLEX NUMBERS --- EX05\n\n")
    # print('#' * 80)

    # u = Vector([Complex(1., 0.), Complex(0., 0.)])
    # v = Vector([Complex(1., 0.), Complex(0., 0.)])
    # print(angle_cos(u, v))

    # u = Vector([Complex(1., 0.), Complex(0., 0.)])
    # v = Vector([Complex(0., 0.), Complex(1., 0.)])
    # print(angle_cos(u, v))

    # u = Vector([Complex(-1., 1.), Complex(1., -1.)])
    # v = Vector([Complex(1., -1.), Complex(-1., 1.)])
    # print(angle_cos(u, v))

    # u = Vector([Complex(2., 1.), Complex(1., 2.)])
    # v = Vector([Complex(4., 2.), Complex(2., 4.)])
    # print(angle_cos(u, v))

    # u = Vector([Complex(1., 2.), Complex(3., 4.), Complex(5., 6.)])
    # v = Vector([Complex(4., 5.), Complex(6., 7.), Complex(8., 9.)])
    # print(angle_cos(u, v))

    # print('#' * 80)
    # print("\n\nCOMPLEX NUMBERS --- EX06\n\n")
    # print('#' * 80)

    # u = Vector([Complex(0., 0.), Complex(0., 0.), Complex(1., 0.)])
    # v = Vector([Complex(1., 0.), Complex(0., 0.), Complex(0., 0.)])
    # print(cross_product(u, v))
    # # [0, 1, 0]

    # u = Vector([Complex(1., 0.), Complex(2., 0.), Complex(3., 0.)])
    # v = Vector([Complex(4., 0.), Complex(5., 0.), Complex(6., 0.)])
    # print(cross_product(u, v))
    # # [-3, 6, -3]

    # u = Vector([Complex(4., 2.), Complex(2., -5.), Complex(-3., 16.)])
    # v = Vector([Complex(-2., 1.), Complex(-5., 0.5), Complex(16., 0.8)])
    # print(cross_product(u, v))
    # # [29.0 + 3.0999999999999943i, -72.4 - 70.2i, -22.0 - 20.0i]

    # print('#' * 80)
    # print("\n\nCOMPLEX NUMBERS --- EX07\n\n")
    # print('#' * 80)

    # u = Matrix([[Complex(1., 0.), Complex(0., 0.)],
    #             [Complex(0., 0.), Complex(1., 0.)]])
    # v = Vector([[Complex(4., 0.)],
    #             [Complex(2., 0.)]])
    # print(u * v)

    # u = Matrix([[Complex(2., 0.5), Complex(0.5, 0.5)],
    #             [Complex(1.5, 0.), Complex(2., 3.)]])
    # v = Vector([[Complex(4., 0.)],
    #             [Complex(2., 0.)]])
    # print(u * v)

    # u = Matrix([[Complex(2., 0.5), Complex(0.5, 0.5)],
    #             [Complex(1.5, 0.), Complex(2., 3.)]])
    # v = Vector([[Complex(4., 0.)],
    #             [Complex(2., 0.)]])
    # print(u * v)

    # u = Matrix([[Complex(2., 0.5), Complex(0.5, 0.5)],
    #             [Complex(1.5, 0.), Complex(2., 3.)]])
    # v = Matrix([[Complex(4., 0.), Complex(2., 0.)],
    #             [Complex(1., 0.), Complex(0., 0.)]])
    # print(u * v)

    # u = Matrix([[Complex(1., 0.), Complex(0., 0.)],
    #             [Complex(0., 0.), Complex(1., 0.)]])
    # v = Matrix([[Complex(1., 0.), Complex(0., 0.)],
    #             [Complex(0., 0.), Complex(1., 0.)]])
    # print(u * v)

    # u = Matrix([[Complex(1., 0.), Complex(0., 0.)],
    #             [Complex(0., 0.), Complex(1., 0.)]])
    # v = Matrix([[Complex(2., 0.), Complex(1., 0.)],
    #             [Complex(4., 0.), Complex(2., 0.)]])
    # print(u * v)

    # u = Matrix([[Complex(3., 0.), Complex(-5., 0.)],
    #             [Complex(6., 0.), Complex(8., 0.)]])
    # v = Matrix([[Complex(2., 0.), Complex(1., 0.)],
    #             [Complex(4., 0.), Complex(2., 0.)]])
    # print(u * v)

    # print('#' * 80)
    # print("\n\nCOMPLEX NUMBERS --- EX08\n\n")
    # print('#' * 80)

    # u = Matrix([[Complex(1., 0.), Complex(0., 0.)],
    #             [Complex(0., 0.), Complex(1., 0.)]])
    # print(u.trace())
    # # 2.0

    # u = Matrix([[Complex(2., 0.), Complex(-5., 0.), Complex(0., 0.)],
    #             [Complex(4., 0.), Complex(3., 0.), Complex(7., 0.)],
    #             [Complex(-2., 0.), Complex(3., 0.), Complex(4., 0.)]])

    # print(u.trace())
    # # 9.0

    # u = Matrix([[Complex(-2., 0.), Complex(-8., 0.), Complex(4., 0.)],
    #             [Complex(1., 0.), Complex(-23., 0.), Complex(4., 0.)],
    #             [Complex(0., 0.), Complex(6., 0.), Complex(4., 0.)]])
    # print(u.trace())
    # # -21.0

    # u = Matrix([[Complex(-2., 0.8), Complex(-8., 0.), Complex(4., 0.)],
    #             [Complex(1., 0.), Complex(-23., 0.2), Complex(4., 0.)],
    #             [Complex(0., 0.), Complex(6., 0.), Complex(4., 41.)]])
    # print(u.trace())
    # # -21.0 + 42.0i

    # print('#' * 80)
    # print("\n\nCOMPLEX NUMBERS --- EX09\n\n")
    # print('#' * 80)

    # m1 = Matrix([[Complex(1., 2.), Complex(3., 4.), Complex(5., 6.)],
    #              [Complex(7., 8.), Complex(9., 10.), Complex(11., 12.)]])
    # m2 = Matrix([[Complex(1., 2.), Complex(3., 4.)],
    #              [Complex(5., 6.), Complex(7., 8.)],
    #              [Complex(9., 10.), Complex(11., 12.)]])
    # m3 = Matrix([[Complex(1., 2.), Complex(3., 4.), Complex(5., 6.)],
    #              [Complex(7., 8.), Complex(9., 10.), Complex(11., 12.)],
    #              [Complex(13., 14.), Complex(15., 16.), Complex(17., 18.)]])

    # print(m1.transpose())
    # print(m2.transpose())
    # print(m3.transpose())
    # print(m1.conjugate_transpose())
    # print(m2.conjugate_transpose())
    # print(m3.conjugate_transpose())

    # print('#' * 80)
    # print("\n\nCOMPLEX NUMBERS --- EX10\n\n")
    # print('#' * 80)

    # u = Matrix([[Complex(1., 0.), Complex(0., 0.), Complex(0., 0.)],
    #             [Complex(0., 0.), Complex(1., 0.), Complex(0., 0.)],
    #             [Complex(0., 0.), Complex(0., 0.), Complex(1., 0.)]])
    # print(u.row_echelon_form())

    # u = Matrix([[Complex(1., 0.), Complex(2., 0.)],
    #             [Complex(3., 0.), Complex(4., 0.)]])
    # print(u.row_echelon_form())

    # u = Matrix([[Complex(1., 5.), Complex(2., 6.), Complex(3., 7.)],
    #             [Complex(0., 7.), Complex(-5., 1.), Complex(2., 3.)]])
    # print(u.row_echelon_form())

    # print('#' * 80)
    # print("\n\nCOMPLEX NUMBERS --- EX11\n\n")
    # print('#' * 80)

    # u = Matrix([[Complex(1., 0.), Complex(-1., 0.)],
    #             [Complex(-1., 0.), Complex(1., 0.)]])
    # print(u.determinant())

    # u = Matrix([[Complex(2., 0.), Complex(0., 0.), Complex(0., 0.)],
    #             [Complex(0., 0.), Complex(2., 0.), Complex(0., 0.)],
    #             [Complex(0., 0.), Complex(0., 0.), Complex(2., 0.)]])
    # print(u.determinant())

    # u = Matrix([[Complex(8., 0.5), Complex(5., 0.8), Complex(-2., 0.7)],
    #             [Complex(4., 0.2), Complex(7., 0.3), Complex(20., 0.4)],
    #             [Complex(7., 0.1), Complex(6., 1.9), Complex(1., 0.6)]])
    # print(u.determinant())

    print('#' * 80)
    print("\n\nCOMPLEX NUMBERS --- EX12\n\n")
    print('#' * 80)

    u = Matrix([[Complex(1., 0.), Complex(0., 0.), Complex(0., 0.)],
                [Complex(0., 0.), Complex(1., 0.), Complex(0., 0.)],
                [Complex(0., 0.), Complex(0., 0.), Complex(1., 0.)]])
    print(u.inverse())

    u = Matrix([[Complex(2., 0.), Complex(0., 0.), Complex(0., 0.)],
                [Complex(0., 0.), Complex(2., 0.), Complex(0., 0.)],
                [Complex(0., 0.), Complex(0., 0.), Complex(2., 0.)]])
    print(u.inverse())

    u = Matrix([[Complex(0., 1.), Complex(0., 0.), Complex(0., 0.)],
                [Complex(0., 0.), Complex(0., 1.), Complex(0., 0.)],
                [Complex(0., 0.), Complex(0., 0.), Complex(0., 1.)]])
    print(u.inverse())
