#!/usr/bin/env python3

from vector import Vector


if __name__ == "__main__":
    u = Vector([0., 0., 0.])
    print(f'{u.norm_1()}, {u.norm()}, {u.norm_inf()}')

    u = Vector([1., 2., 3.])
    print(f'{u.norm_1()}, {u.norm()}, {u.norm_inf()}')

    u = Vector([-1., -2.])
    print(f'{u.norm_1()}, {u.norm()}, {u.norm_inf()}')
