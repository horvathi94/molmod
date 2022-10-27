"""Plot the 12-6 Lennard-Jones potential"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Change style for prettier plots
sns.set_style("whitegrid")
#plt.style.use("seaborn-paper")


def lj_attractive(r, sigma=1., epsilon=1.):
    v = 4. * epsilon * (sigma / r)**12
    return v


def lj_repulsive(r, sigma=1., epsilon=1.):
    v = -4. * epsilon * (sigma / r)**6
    return v



if __name__ == "__main__":

    r = np.linspace(0.1, 4, 100_000)
    sigma = 1.
    epsilon = 1.

    fig = plt.figure()
    ax = fig.add_subplot(111)
    lj_attr = lj_attractive(r, sigma=sigma, epsilon=epsilon)
    lj_rep = lj_repulsive(r, sigma=sigma, epsilon=epsilon)
    lj = lj_attr + lj_rep
    ax.plot(r, lj_attr, "--", label="LJ attractive")
    ax.plot(r, lj_rep, "--", label="LJ repulsive")
    ax.plot(r, lj, label="LJ")
    ax.set_xlim([0, 4])
    ax.set_ylim([-3, 4])

    fig.legend()
    plt.show()
