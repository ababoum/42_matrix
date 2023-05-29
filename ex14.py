#!/usr/bin/env python3

from matrix import Matrix
import sys
import os
from math import tan


def projection(fov: float, ratio: float, near: float, far: float) -> Matrix:
    '''
    Returns the projection matrix for a given field of view, aspect ratio,
    near plane and far plane.
    The FOV needs to be in degrees.
    Source:
    https://www.scratchapixel.com/lessons/3d-basic-rendering/perspective-and-orthographic-projection-matrix/building-basic-perspective-projection-matrix.html
    '''
    fov_rad = fov * 3.14159265358979323846 / 180.0
    x_scale = 1.0 / (ratio * tan(fov_rad / 2.0))
    y_scale = 1.0 / tan(fov_rad / 2.0)
    z_scale = -(far) / (far - near)
    depth = - near * far / (far - near)

    return Matrix([
        [x_scale, 0.0, 0.0, 0.0],
        [0.0, y_scale, 0.0, 0.0],
        [0.0, 0.0, z_scale, -1.0],
        [0.0, 0.0, depth, 0.0]
    ])


if __name__ == "__main__":
    # Create the projection matrix in the matrix_display folder (proj file)
    proj = projection(80.0, 1.0, 0.1, 10000.0)
    proj_str = str(proj).replace('[', '').replace(']', '').replace(
        'Matrix ', '').replace('(', '').replace(')', '').replace('\t', '')

    # Write the projection matrix to the proj file
    with open("./matrix_display/proj", "w") as f:
        f.write(proj_str)

    print(f"Projection matrix:\n{proj_str}")

    # Execute the display binary
    os.chdir("./matrix_display")
    os.system("./display")
