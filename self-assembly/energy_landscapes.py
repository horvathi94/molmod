"""Calculate and plot the dsiconnectivity graph of LJ13 cluster using
basin hopping.
"""

# Do this to make sure that matplotlib can plot the graph
import matplotlib
matplotlib.use('Agg')

import random
import numpy as np
from pele.systems import LJCluster
from pele.landscape import ConnectManager
from pele.utils.disconnectivity_graph import DisconnectivityGraph,\
    database2graph
import matplotlib.pyplot as plt

# Set random seed for reproducibility
random.seed(42)
np.random.seed(42)


# Define parameters and system
n_atoms = 13
n_basin_hopping = 2000
system = LJCluster(n_atoms)

# Create the databse 
database = system.create_database("lj{:d}.sqlite".format(n_atoms))
bh = system.get_basinhopping(database)
bh.run(n_basin_hopping)

# Connect the minima of the energy landscape
manager = ConnectManager(database, strategy="gmin")
for i in xrange(database.number_of_minima()-1):
    min1, min2 = manager.get_connect_job()
    connect = system.get_double_ended_connect(min1, min2, database)
    connect.connect()




# Convert the database to a networkx graph
graph = database2graph(database)
dg = DisconnectivityGraph(graph, nlevels=3, center_gmin=True)
dg.calculate()
dg.plot()

# Save image
plt.savefig("disconnectivity-graph-LJ{:d}.png".format(n_atoms))
