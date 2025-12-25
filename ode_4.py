#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Solve d^2x/dt^2 = -ω^2x by Verlet method
import math
import numpy as np
import matplotlib.pyplot as plt

# Parameters
ω  = 1.0
Δt = 0.1 * (1/ω)
T0 = 2.0 * math.pi
T  = 2.0 * T0
N  = int(T/Δt+0.5)

# Initialization
t  = 0.0
x  = 1.0  
y  = 0.0  # v/ω

ts = [t]
xs = [x]
ys = [y]

#print(f"{0*Δt:4.1f} {x:12g} {y:12g}")
x_new = x + y*Δt + (-ω*x)*Δt*Δt/2

for i in range(1,N):
    (x_old, x) = (x, x_new)
    x_new = 2*x - x_old + (-ω*x)*Δt*Δt
    y     = (x_new - x_old)/(2*Δt) / ω
    #print(f"{i*Δt:4.1f} {x:12g} {y:12g}")
    t = t + Δt
    ts.append(t)
    xs.append(x)
    ys.append(y)

    
(x_old, x) = (x, x_new)
y = ((x - x_old)/Δt + (-ω*x)*Δt/2) / ω
#print(f"{N*Δt:4.1f} {x:12g} {y:12g}")
t = t + Δt
ts.append(t)
xs.append(x)
ys.append(y)

ts = np.array(ts)
xs = np.array(xs)
ys = np.array(ys)

# Output
#for t,x in zip(ts,xs):
#    print(t, x)
    
fig = plt.figure()
ax  = fig.add_subplot(311)
ax.grid()
plt.xlabel("t")
plt.ylabel("x,y")
ax.plot(ts, xs, label="x")
ax.plot(ts, ys, label="y")
plt.legend()
ax  = fig.add_subplot(312)
plt.xlabel("x")
plt.ylabel("y")
plt.axis("equal")
ax.plot(xs, ys)
ax  = fig.add_subplot(313)
plt.xlabel("t")
plt.ylabel("x*x+y*y-1")
ax.plot(ts, xs**2+ys**2-1)
plt.show()
