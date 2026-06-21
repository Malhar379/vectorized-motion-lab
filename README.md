# Vectorized Motion Lab

A vectorized particle universe built with NumPy and Matplotlib.

## Overview

Vectorized Motion Lab simulates particles evolving inside a bounded environment under stochastic perturbations. The system records the complete history of particle motion and provides both trajectory visualizations and real-time animations.

## Features

- Vectorized particle updates using NumPy
- Random perturbations (Brownian-like motion)
- Boundary collisions
- Full state history recording
- Static trajectory visualization
- Real-time particle animation
- Modular code organization

## Tech Stack

- Python
- NumPy
- Matplotlib

## Project Structure

```text
vectorized-motion-lab/

├── images/
│     trajectory.png
│     animation.gif
│
├── src/
│     initialize.py
│     simulation.py
│     visualization.py
│
├── main.py
├── requirements.txt
└── README.md
```

## Trajectory Visualization

![Trajectory](images/trajectory.png)

## Animation

![Animation](images/animation.gif)

## Concepts Demonstrated

- State representation
- Time evolution
- Vectorized computation
- Stochastic dynamics
- Boundary constraints
- History recording
- Data visualization
- Modular code design

## Run Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Run:

```bash
python main.py
```

## Motivation

This project was built as part of a larger effort to understand systems through state, rules, and evolution over time. It serves as a foundation for more complex simulations and learning-based systems.
