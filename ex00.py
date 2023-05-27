#!/usr/bin/env python3

from vector import Vector
from matrix import Matrix


if __name__ == "__main__":
    u = Vector([2, 3])
    v = Vector([5, 7])

    print(u + v)
    print(u - v)
    print(u * 2)
    print(2 * u)

    print('#' * 80)

    u = Matrix([[1, 2], [3, 4]])
    v = Matrix([[7, 4], [-2, 2]])

    print(u + v)
    print(u - v)
    print(2 * u)
