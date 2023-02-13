import matplotlib.pyplot as plt
import numpy as np
import math

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

def simple_fish():
    x = [1, 2 ,3, 4, 5, 6, 7]
    y = [2, 4, 7, 11, 16, 19, 20]
    plt.plot(x, y)
    plt.ylabel('Goldfish')
    plt.xlabel('Generation')
    plt.tight_layout()
    plt.savefig('static/simple_fish.png', transparent=True)

def gre_curve():
    def fun(x):
        result = 0
        if 0 <= x <= 2:
            result = (3 / 2) * math.sqrt(4 - x**2)
        if 2 < x <= 4:
            result = -math.sqrt(1 - (x - 3)**2)
        return result
    vfun = np.vectorize(fun)
    x = np.linspace(0, 4, 100)
    y = vfun(x)
    plt.plot(x, y)
    plt.ylabel('y')
    plt.xlabel('x')
    plt.tight_layout()
    plt.savefig('static/gre_curve.png', transparent=True)


def log_map_example():
    x = [0, 1, 2 ,3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
    y = [2, 2.54, 3.21, 4.01, 4.97, 6.01, 7.37, 8.76, 10.24,
         11.74, 13.19, 14.54, 15.74, 16.74, 17.56, 18.2,18.69, 19.06]
    plt.plot(x, y)
    plt.ylabel('P_t')
    plt.xlabel('t')
    plt.tight_layout()
    plt.savefig('static/log_map_example.png', transparent=True)


def log_map_example_2():
    x = [0, 1, 2 ,3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
    y = [2/20, 2.54/20, 3.21/20, 4.01/20, 4.97/20, 6.01/20, 7.37/20, 8.76/20, 10.24/20,
         11.74/20, 13.19/20, 14.54/20, 15.74/20, 16.74/20, 17.56/20, 18.2/20,18.69/20, 19.06/20]
    plt.plot(x, y)
    plt.ylabel('x_t')
    plt.xlabel('t')
    plt.tight_layout()
    plt.savefig('static/log_map_example_2.png', transparent=True)

log_map_example_2()