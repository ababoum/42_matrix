#!/usr/bin/env python3

from vector import Vector
from matrix import Matrix


def lerp(u, v, t: float):
    """Returns the linear interpolation between vectors u and v at time t."""
    try:
        if 0 <= t <= 1:
            return u + t * (v - u)
        else:
            raise ValueError
    except TypeError:
        raise TypeError(
            "u and v must be vectors/matrices and t must be a number.")
    except ValueError:
        raise ValueError("t must be between 0 and 1.")
    except:
        raise Exception("Linear interpolation: something went wrong.")


if __name__ == "__main__":
    print(lerp(0., 1., 0.))
    print(lerp(0., 1., 1.))
    print(lerp(0., 1., 0.5))
    print(lerp(21., 42., 0.3))

    print('*' * 80)

    print(lerp(Vector([2., 1.]), Vector([4., 2.]), 0.3))
    print(lerp(Matrix([[2., 1.], [3., 4.]]),
          Matrix([[20., 10.], [30., 40.]]), 0.5))
    
    
