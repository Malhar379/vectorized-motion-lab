from src.initialize import initialize_particles
from src.simulation import simulate
from src.visualization import (
    plot_trajectories,
    animate
)

N = 100
T = 1000

positions, velocities = initialize_particles(N)

history = simulate(
    positions,
    velocities,
    T
)

plot_trajectories(history)

animate(history)