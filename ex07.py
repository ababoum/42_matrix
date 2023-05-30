#!/usr/bin/env python3

from vector import Vector
from matrix import Matrix


if __name__ == "__main__":
    u = Matrix([[1., 0.],
                [0., 1.]])
    v = Vector([[4.], [2.]])
    print(u * v)
    # [[4.], [2.]]

    u = Matrix([[2., 0.],
                [0., 2.]])
    v = Vector([[4.], [2.]])
    print(u * v)
    # [[8.], [4.]]

    u = Matrix([[2., -2.],
                [-2., 2.]])
    v = Vector([[4.], [2.]])
    print(u * v)
    # [[4.], [-4.]]

    u = Matrix([[1., 0.],
                [0., 1.]])
    v = Matrix([[1., 0.],
                [0., 1.]])
    print(u * v)
    # [1., 0.]
    # [0., 1.]

    u = Matrix([[1., 0.],
                [0., 1.]])
    v = Matrix([[2., 1.],
                [4., 2.]])
    print(u * v)
    # [2., 1.]
    # [4., 2.]

    u = Matrix([[3., -5.],
                [6., 8.]])
    v = Matrix([[2., 1.],
                [4., 2.]])
    print(u * v)
    # [-14., -7.]
    # [44., 22.]
