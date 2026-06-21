import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def plot_trajectories(history):

    N = history.shape[1]

    for i in range(N):

        x = history[:, i, 0]
        y = history[:, i, 1]

        plt.plot(
            x,
            y,
            alpha=0.05
        )

    plt.xlim(0,100)
    plt.ylim(0,100)

    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Vectorized Motion Lab")

    plt.grid()

    plt.savefig("images/trajectory.png")

    plt.show()

    
def animate(history):

    T = history.shape[0]

    fig, ax = plt.subplots()

    scatter = ax.scatter(
        history[0][:,0],
        history[0][:,1],
        s=15
    )

    ax.set_xlim(0,100)
    ax.set_ylim(0,100)

    ax.set_title("Vectorized Motion Lab")

    def update(frame):

        scatter.set_offsets(
            history[frame]
        )

        return scatter,

    animation = FuncAnimation(
        fig,
        update,
        frames=T,
        interval=20,
        blit=True
    )

    animation.save(
        "images/animation.gif",
        writer="pillow"
    )

    plt.show()