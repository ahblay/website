import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['text.color'] = "white"
plt.rcParams['axes.labelcolor'] = "white"
plt.rcParams['axes.labelsize'] = 18
plt.rcParams['axes.labelpad'] = 10
plt.rcParams['axes.labelweight'] = "bold"
plt.rcParams['axes.linewidth'] = 2
plt.rcParams['axes.edgecolor'] = "white"
plt.rcParams['xtick.color'] = "white"
plt.rcParams['ytick.color'] = "white"
plt.rcParams['xtick.labelsize'] = 15
plt.rcParams['ytick.labelsize'] = 15
plt.rcParams['lines.linewidth'] = 2

def simple_car():
    x = np.linspace(0, 10, 100)
    y = x**2
    plt.plot(x, y)
    plt.ylabel('Distance (s)')
    plt.xlabel('Time (t)')
    plt.tight_layout()
    plt.savefig('static/simple_car.png', transparent=True)

simple_car()