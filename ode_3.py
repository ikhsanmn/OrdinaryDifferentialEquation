#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Solve d^2x/dt^2 = -ω^2x by MidPoint method

#%matplotlib inline
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
y  = 0.0

# MainLoop
ts = [t]
xs = [x]
ys = [y]
for i in range(N):
    # MidPoint method for d^2x/dt^2 = -ω^2x
    # dx/dt = +ωy
    # dy/dt = -ωx
    x_mid = x + ω*y    *Δt/2 
    y_mid = y - ω*x    *Δt/2 
    x     = x + ω*y_mid*Δt 
    y     = y - ω*x_mid*Δt 

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
