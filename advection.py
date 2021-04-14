"""
Advection Example: 1D
@author: Vasily G. Piccone

Date: April 5th, 2021
"""

#Imports
from mpl_toolkits.mplot3d import axes3d
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np

# Defining variables
Ngrid = 50
Nstep = 5000
dt = 1
dx = 1

u = -0.1
alpha = u*dt/(2*dx)

# Creating grid
x = np.arange(Ngrid)*dx
t = np.arange(Nstep)*dt

# Initial Conditions
f1 = np.copy(x)*1./Ngrid  # Lax-Friedrichs
f2 = np.copy(x)*1./Ngrid  # FTCS

plt.ion()

fig, axes = plt.subplots(1, 2)
axes[0].set_title('Lax-Friendrichs')
axes[1].set_title('FTCS')

# Static initial condition plot for reference
axes[0].plot(x, f1, 'k-')
axes[1].plot(x, f2, 'k-')

# Plot of the conditions to be updated
plt1, = axes[0].plot(x, x, 'ro')
plt2, = axes[1].plot(x, x, 'ro')
fig.canvas.draw()

# Setting up the graphing region for the animation
for ax in axes:
    ax.set_xlim([-0.1, Ngrid])
    ax.set_ylim([0, 2])

fig.canvas.draw()

# Time Evolution
cnt = 0

while cnt < Nstep:

    # Lax-Friedrich
    f1[1:Ngrid - 1] = 1/2*(f1[2:]+f1[:Ngrid - 2]) - alpha*(f1[2:] - f1[:Ngrid-2])

    # FTCS
    f2[1:Ngrid - 1] = f2[1:Ngrid - 1] - alpha * (f2[2:] - f2[:Ngrid - 2])

    plt1.set_ydata(f1)
    plt2.set_ydata(f2)

    fig.canvas.draw()
    plt.pause(0.01)
    cnt += 1
