import matplotlib.pyplot as plt
import numpy as np


# y = x + rx(1 - x)
def logistic(init, r, output, depth):
    out = init + r*init*(1 - init)
    output.append(out)
    depth -= 1
    if depth == 0:
        return
    else:
        logistic(out, r, output, depth)
        return output


# y = sx(1 - x) where s is a function of x
def logistic_complex(init, s, output, depth):
    r = s - (1/(1-init**2))
    out = init + r * init * (1 - init)
    output.append(out)
    depth -= 1
    if depth == 0:
        return
    else:
        logistic_complex(out, s, output, depth)
        return output


def bifurcation(init, depth):
    vals = []
    for r in np.linspace(0, 4, 1000):
        log = logistic(init, r, [], depth)[-5:]
        vals.extend(log)
    print(vals)
    x = np.linspace(0, 4, 5000)
    y = vals
    plt.scatter(x, y, s=.75)
    plt.ylabel('limit')
    plt.xlabel('r-value')
    plt.show()

pop_size = 2
carrying_capacity = 20
init = pop_size/carrying_capacity
depth = 100

#bifurcation(init, depth)

log = logistic(0.5, 3, [], 10)
print(log)

'''
r = 3
s = r + (1/(1 - (pop_size/carrying_capacity)))
depth = 100

print("r: " + str(r))
#print("s: " + str(s))

r_logistic = logistic(init, r, [], depth)[-15:]
s_logistic = logistic(init, s, [], depth)[-15:]

print("last 15 (r): " + str(r_logistic))
#print("last 5 (s): " + str(s_logistic))

x_r = range(len(r_logistic))
y_r = r_logistic
x_s = range(len(s_logistic))
y_s = s_logistic
plt.plot(x_r, y_r)
#plt.plot(x_s, y_s)
plt.ylabel('Generation')
plt.xlabel('Population')
plt.show()
'''