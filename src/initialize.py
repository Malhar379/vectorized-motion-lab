import numpy as np

def initialize_particles(N):

    positions = np.random.uniform(
        low=0,
        high=100,
        size=(N,2)
    )

    velocities = np.random.uniform(
        low=-1,
        high=1,
        size=(N,2)
    )

    return positions, velocities