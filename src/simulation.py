import numpy as np

def simulate(positions, velocities, T):

    N = len(positions)

    history = []

    for t in range(T):

        noise = np.random.normal(
            loc=0,
            scale=0.02,
            size=(N,2)
        )

        velocities += noise

        positions += velocities

        velocities[positions[:,0] > 100,0] *= -1
        velocities[positions[:,0] < 0,0] *= -1

        velocities[positions[:,1] > 100,1] *= -1
        velocities[positions[:,1] < 0,1] *= -1

        history.append(positions.copy())

    return np.array(history)