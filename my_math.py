#!/usr/bin/env python3

'''
Mathematical functions.
'''


from my_complex import Complex


def Re(z: Complex | float | int) -> float:
    '''Returns the real part of z.'''
    if isinstance(z, (int, float)):
        return z
    return z.real

def ft_abs(x: float | int | Complex, type='euclidian') -> float:
    '''Returns the absolute value of x.'''
    if isinstance(x, (int, float)):
        return x if x >= 0 else -x
    elif isinstance(x, Complex):
        if type == 'euclidian':
            return ft_sqrt(x.real * x.real + x.imaginary * x.imaginary)
        elif type == 'manhattan':
            return ft_abs(x.real) + ft_abs(x.imaginary)


def ft_sqrt(x: float, epsilon=1e-6) -> float:
    '''Returns the square root of x.'''
    if x < 0:
        raise ValueError("Cannot compute square root of a negative number.")
    if x == 0:
        return 0
    guess = x / 2
    while ft_abs(guess * guess - x) > epsilon:
        guess = (guess + x / guess) / 2
    return guess


def ft_pow(x: float, n: int) -> float:
    '''Returns x raised to the power of n.'''
    if n < 0:
        raise ValueError("Cannot compute negative powers.")
    if n == 0:
        return 1
    return x * ft_pow(x, n - 1)


if __name__ == "__main__":
    print(f'{ft_sqrt(4)} vs {4**0.5}')
    print(f'{ft_sqrt(9)} vs {9**0.5}')
    print(f'{ft_sqrt(16.87458)} vs {16.87458**0.5}')
    print(f'{ft_sqrt(0)} vs {0**0.5}')
    print(f'{ft_sqrt(1)} vs {1**0.5}')
    print(f'{ft_sqrt(157484.58)} vs {157484.58**0.5}')
