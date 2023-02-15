import numpy as np



def indices_of_B(rho, a):
    """Returns the indices of points at which rho >= a."""
    pass





def read_cube_file(file):
    """Read volumetric data from a cube file and return in numpy array."""

    volumetric_data = []

    with open(file) as ed_file:
        lines = ed_file.readlines()

        for index, line in enumerate(lines):

            # Skip the first two lines as they are just comments:
            # Remember: indexing in Python starts from 0!
            if index < 2:
                pass

            # Read the number of atoms, in cube files this is always given by
            # the first column of the third line:
            elif index == 2:

                # Split the string at whitespaces:
                splitted_line = line.split()

                # Select first element from the list:
                N_atoms = splitted_line[0]

                # Cast N_atoms to integer:
                N_atoms = int(N_atoms)


            # Lines 4, 5 and 6 describe the box, the first columns define the 
            # number of cells
            elif index == 3:
                splitted_line = line.split()
                nx = int(splitted_line[0])

            elif index == 4:
                splitted_line = line.split()
                ny = int(splitted_line[0])

            elif index == 5:
                splitted_line = line.split()
                nz = int(splitted_line[0])

            # Lines 7, 8, ..., 7+N_atoms describe the atoms
            # Here we skip reading these...
            elif 5 < index < 6+N_atoms:
                pass

            else:
                # Read the volumetric data line-by-line and append to the 
                # `volumetric_data` list
                splitted_line = line.split()
                for item in splitted_line:
                    volumetric_data.append(float(item))

    # Create numpy array from the volumetric_data list:
    volumetric_data = np.asarray(volumetric_data)

    # The volumetric data is still one-dimensional
    # Reshape the array
    volumetric_data = volumetric_data.reshape(nx, ny, nz)

    # Print some info
    print(f"The shape of the volumetric data read: {volumetric_data.shape}\n")

    return volumetric_data


def test(rho, a):
    """Return indices where rho >= a."""
    indices = np.where(rho >= a)
    indices = np.asarray(indices).T
    return indices


def verify_results(indices):
    """Compares your results to the reference."""
    reference_indices = test(rho, a)
    n_reference = len(reference_indices)

    if type(indices) is not np.ndarray:
        print("Error: The function must return a numpy array.")
        exit(1)

    n = len(indices)

    print(f"Number of voxels (or points) in the molecular body: {n_reference}")
    print(f"Number of points selected: {n}")
    print(f"Selected the correct number of points: {n == n_reference}\n")

    # Sorting your results to compare them to the reference
    indices = indices[indices[:, 2].argsort()]
    indices = indices[indices[:, 1].argsort(kind="mergesort")]
    indices = indices[indices[:, 0].argsort(kind="mergesort")]
    is_equal = np.array_equal(reference_indices, indices)
    print(f"The points you selected are the same as the reference: {is_equal}")




if __name__ == "__main__":

    a = 0.1
    rho = read_cube_file("ethanol.ed.cube")

    indices = indices_of_B(rho, a)

    verify_results(indices)
