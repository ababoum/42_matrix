#!/usr/bin/env python3

from vector import Vector


if __name__ == "__main__":
    u = Vector([0., 0.])
    v = Vector([1., 1.])

    print(u.dot(v))
    print(v.dot(u))
    print('*' * 80)

    u = Vector([1., 1.])
    v = Vector([1., 1.])

    print(u.dot(v))
    print(v.dot(u))
    print('*' * 80)

    u = Vector([-1., 6.])
    v = Vector([3., 2.])

    print(u.dot(v))
    print(v.dot(u))

