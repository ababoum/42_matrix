#!/usr/bin/env python3

from vector import Vector


def cross_product(u: Vector, v: Vector) -> Vector:
    if u.size() != 3 or v.size() != 3:
        raise ValueError("Cross product is only defined in 3D")
    if u.shape != v.shape:
        raise ValueError("Vectors must have the same shape")
    return Vector([u[1] * v[2] - u[2] * v[1],
                   u[2] * v[0] - u[0] * v[2],
                   u[0] * v[1] - u[1] * v[0]])


if __name__ == "__main__":
    u = Vector([0., 0., 1.])
    v = Vector([1., 0., 0.])
    print(cross_product(u, v))

    u = Vector([1., 2., 3.])
    v = Vector([4., 5., 6.])
    print(cross_product(u, v))

    u = Vector([4., 2., -3.])
    v = Vector([-2., -5., 16.])
    print(cross_product(u, v))
