#!/usr/bin/env python3

'''
Mathematical functions.
'''


def ft_abs(x: float) -> float:
    '''Returns the absolute value of x.'''
    return x if x >= 0 else -x


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
