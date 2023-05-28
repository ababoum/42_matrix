#!/usr/bin/env python3

from matrix import Matrix

if __name__ == "__main__":
    
    m1 = Matrix([[1, 2, 3], [4, 5, 6]])
    m2 = Matrix([[1, 2], [3, 4], [5, 6]])
    m3 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    print(m1.transpose())
    print(m2.transpose())
    print(m3.transpose())
