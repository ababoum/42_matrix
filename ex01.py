#!/usr/bin/env python3

from vector import Vector


def linear_combination(u: list, coefs: list) -> Vector:
    """Returns the linear combination of vectors u and coefficients coefs."""
    try:
        if len(u) == len(coefs):
            ret = Vector([0. for i in range(u[0].size())])
            for i in range(len(u)):
                ret += u[i] * coefs[i]
            return ret
        else:
            raise ValueError
    except TypeError:
        raise TypeError("u and coefs must be lists of numbers.")
    except ValueError:
        raise ValueError("u and coefs must be the same length.")
    except:
        raise Exception("Linear combination: something went wrong.")


if __name__ == "__main__":
    e1 = Vector([1., 0., 0.])
    e2 = Vector([0., 1., 0.])
    e3 = Vector([0., 0., 1.])

    v1 = Vector([1., 2., 3.])
    v2 = Vector([0., 10., -100.])

    print(linear_combination([e1, e2, e3], [10., -2., 0.5]))
    print(linear_combination([v1, v2], [10., -2.]))

    try:
        print(linear_combination([1, 2, 3], [10., -2., 0.5]))
    except Exception as e:
        print(e)

    try:
        print(linear_combination([e1, e2, e3], [10., -2.]))
    except Exception as e:
        print(e)
