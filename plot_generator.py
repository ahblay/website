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
    x = np.linspace(0, 8, 100)
    y = 8*x**2
    plt.plot(x, y)
    plt.ylabel('Distance (m)')
    plt.xlabel('Time (s)')
    plt.tight_layout()
    plt.savefig('static/simple_car.png', transparent=True)

def photos_car():
    x = np.linspace(0, 8, 100)
    y = 8*x**2
    plt.plot(x, y)
    plt.plot(5, 200, 'ro')
    plt.plot(7, 392, 'ro')
    plt.ylabel('Distance (m)')
    plt.xlabel('Time (s)')
    plt.tight_layout()
    plt.savefig('static/photos_car.png', transparent=True)

def slope_car():
    x = np.linspace(0, 8, 100)
    y = 8*x**2
    plt.plot(x, y)
    plt.plot([5, 7], [200, 392], 'ro-')
    plt.ylabel('Distance (m)')
    plt.xlabel('Time (s)')
    plt.tight_layout()
    plt.savefig('static/slope_car.png', transparent=True)

def multislope_car():
    plt.ylim(150, 450)
    x = np.linspace(4.5, 7.5, 100)
    y = 8*x**2
    plt.plot(x, y, 'w')
    intervals = [2, 1, 0.5, 0.25]
    colors = ['r', 'g', 'c', 'm']
    cp = 5
    for i, j in zip(intervals, colors):
        x_1 = cp
        x_2 = cp + i
        y_1 = 8 * x_1**2
        y_2 = 8 * x_2**2
        m = (y_2 - y_1)/(x_2 - x_1)
        plt.plot(x, m * (x - x_1) + y_1, j + ':')
        plt.plot(x_1, y_1, 'wo')
        plt.plot(x_2, y_2, j + 'o')
    plt.ylabel('Distance (m)')
    plt.xlabel('Time (s)')
    plt.tight_layout()
    plt.savefig('static/multislope_car.png', transparent=True)

def multislope_car_zoom():
    plt.ylim(190, 230)
    x = np.linspace(4.9, 5.3, 100)
    y = 8*x**2
    plt.plot(x, y, 'w')
    intervals = [0.25]
    colors = ['m']
    cp = 5
    for i, j in zip(intervals, colors):
        x_1 = cp
        x_2 = cp + i
        y_1 = 8 * x_1**2
        y_2 = 8 * x_2**2
        m = (y_2 - y_1)/(x_2 - x_1)
        plt.plot(x, m * (x - x_1) + y_1, j + ':')
        plt.plot(x_1, y_1, 'wo')
        plt.plot(x_2, y_2, j + 'o')
    plt.ylabel('Distance (m)')
    plt.xlabel('Time (s)')
    plt.tight_layout()
    plt.savefig('static/multislope_car_zoom.png', transparent=True)

def deltas_car():
    x = np.linspace(0, 8, 100)
    y = 8*x**2
    plt.plot(x, y)
    plt.plot(5, 200, 'ro')
    plt.annotate(s='$t_0$', xy=(5, 200), xytext=(4.3, 200), size=18)
    plt.plot(7, 392, 'ro')
    plt.annotate(s='$t_0 + \Delta t$', xy=(7, 392), xytext=(5.4, 392), size=18)
    plt.ylabel('Distance (m)')
    plt.xlabel('Time (s)')
    plt.tight_layout()
    plt.savefig('static/deltas_car.png', transparent=True)

deltas_car()