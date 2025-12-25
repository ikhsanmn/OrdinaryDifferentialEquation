#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Solve dx/dt = -λx by Euler method

import numpy as np
import matplotlib.pyplot as plt

# Parameters
λ  = 1.0
Δt = 0.5 * (1/λ)
T  = 10.0 * (1/λ)
NT = int(T/Δt+0.5)

# Initialization
t  = 0.0
xf = 1.0
xb = 1.0

# MainLoop
ts  = [t]
xfs = [xf]
xbs = [xb]
for i in range(NT):
    xf = (1-λ*Δt)*xf   # Explicit Euler method for dx/dt = -λx
    xb = 1/(1+λ*Δt)*xb # Implicit Euler method for dx/dt = -λx
    t = t + Δt
    ts.append(t)
    xfs.append(xf)
    xbs.append(xb)
ts  = np.array(ts)
xfs = np.array(xfs)
xbs = np.array(xbs)

# Output
#for t,xf,xb in zip(ts,xfs,xbs):
#    print(t, xf, xb)

τs=np.linspace(ts[0],ts[-1],1001)

plt.grid()
plt.xlabel("t")
plt.ylabel("xf,xb")
plt.plot(ts, xfs, marker="o", label="Explicit Euler")
plt.plot(ts, xbs, marker="o", label="Implicit Euler")
#plt.plot(ts, np.exp(-λ*ts),ls="--")
plt.plot(τs, np.exp(-λ*τs),ls="--", label="Exact solution")
plt.legend()
plt.show()
