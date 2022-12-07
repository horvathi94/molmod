import numpy as np


def test(r1, r2):
    """Function to compare your resutls to."""
    r1 = np.asarray(r1)
    r2 = np.asarray(r2)
    return np.linalg.norm(r1 - r2)



def distance(p1, p2):
    """Compute distance between two points in 3D space."""
    pass


if __name__ == "__main__":

    r1 = (1, 1, 0)
    r2 = (0, 0, 0)

    d_reference = test(r1, r2)
    d = distance(r1, r2)

    print(f"Reference: {d_reference}")
    print(f"Result from `distance` function: {d}")
    print(f"The two values are equal: {d_reference == d}")
