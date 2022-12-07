import numpy as np
import matplotlib.pyplot as plt

# Change the style of plots to make them look prettier
plt.style.context("seaborn-v0_8-dark-palette")


def example_plot():
    """Plots and shows the sinus wave."""

    # Use the `linspace` function from the numpy package to create an array 
    # of 10.000 numbers that are evenly spaced between -10 and +10.
    x = np.linspace(-10, 10, 10000)

    # Compute the sin of each number in the array x
    y = np.sin(x)

    # Define Figure object (from matplotlib) 
    fig = plt.figure()

    # Add a subplot to the figure
    ax = fig.add_subplot(111)

    # Plot the y value for each x
    ax.plot(x, y)

    # Show the image
    plt.show()

    # Save the image to `sinus.png`
    # Imprtant! The figure is cleared after calling `plt.show()`.
    # So if you would like to save your results to a file, comment out or
    # remove the line 28: plt.show()
    plt.savefig("sinus.png")



def plot():
    pass


if __name__ == "__main__":

    example_plot()
    plot()
