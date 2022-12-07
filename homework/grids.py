import numpy as np
import matplotlib.pyplot as plt


def ep_grid(n, q):
    """Returns the grid with values of the potential energy
    created by a particle with charge `q` in the center of the grid."""
    grid = np.zeros(shape=(n,n))

    # Calculate electrostatic potential at each point

    return grid


def sin_grid(n):
    """Rturns a grid with sin wave."""

    # Create a numpy array with `n` values that are evenly spaced 
    # between -10 and +10
    points = np.linspace(-10, 10, n)

    # Initialize a n x n numpy array with 0 values
    grid = np.zeros(shape=(n,n))

    # Calculate the value of the sin function at each point of the grid

    # Loop for row indices
    for i in range(n):

        # x marks the current row
        x = points[i]

        # Loop for column indices
        for j in range(n):

            # y marks the current column
            y = points[j]

            # Calculate the distance from the origin
            r = np.sqrt(x**2 + y**2)

            # Put the value of the sin(r) function into the grid
            grid[i,j] = np.sin(r)

    return grid




if __name__ == "__main__":

    n = 100
    # Compute grids
    sin_wave = sin_grid(n)
    ep = ep_grid(n)

    # Initialize matplotlib figure object
    fig = plt.figure()

    # Add the first subplot
    ax1 = fig.add_subplot(121)

    # Plot the grid on the first subplot
    im1 = ax1.imshow(sin_wave)

    # Plot the colorbar on the first subplot
    plt.colorbar(im1)

    # Add the second subfigure
    ax2 = fig.add_subplot(122)

    # Plot the grid on the second subplot
    im2 = ax2.imshow(ep)

    # Plot the colorbar for the second subplot
    plt.colorbar(im2)

    # Show the figure
    plt.show()
