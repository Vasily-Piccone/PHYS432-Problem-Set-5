"""
Advection-Diffusion Example: 1D
@author: Vasily G. Piccone

Date: April 14th, 2021
"""

# Imports
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

# Diffusion coefficients
D1 = 0.2
D2 = 1.0

# Matrix coefficients
beta1 = (D1*dt)/(dx*dx)
beta2 = (D2*dt)/(dx*dx)

# Setting up grid
x = np.arange(Ngrid)*dx
t = np.arange(Nstep)*dt

# Initial Conditions
f1 = np.copy(x)*1./Ngrid  # For D1
f2 = np.copy(x)*1./Ngrid  # For D2

plt.ion()

fig, axes = plt.subplots(1, 2)
axes[0].set_title('D = 0.2')
axes[1].set_title('D = 1')

# Static initial condition plot for reference
print(f1)
axes[0].plot(x, f1, 'k-')
axes[1].plot(x, f2, 'k-')

# Plot of the conditions to be updated
plt1, = axes[0].plot(x, f1, 'ro')
plt2, = axes[1].plot(x, f2, 'ro')
fig.canvas.draw()

# Setting up the graphing region for the animation
for ax in axes:
    ax.set_xlim([-0.1, Ngrid])
    ax.set_ylim([0, 2])

fig.canvas.draw()

# Tri-diagonal Diffusion matrix

# D = 0.2
A1 = np.eye(Ngrid)*(1 + 2*beta1) - beta1*np.eye(Ngrid, k=1) - beta1*np.eye(Ngrid, k=-1)

# D = 1
A2 = np.eye(Ngrid)*(1 + 2*beta2) - beta2*np.eye(Ngrid, k=1) - beta2*np.eye(Ngrid, k=-1)

# No-slip boundary conditions (set at both the right and left edges)
A1[0, :] = np.zeros(Ngrid)
A1[0][0] = 1

A1[Ngrid-1, :] = np.zeros(Ngrid)
A1[Ngrid-1][Ngrid-1] = 1

A2[0, :] = np.zeros(Ngrid)
A2[0][0] = 1

A2[Ngrid-1, :] = np.zeros(Ngrid)
A2[Ngrid-1][Ngrid-1] = 1

# Time Evolution bit
cnt = 0
while cnt < Nstep:

    # Calculate diffusion term
    f1 = np.linalg.solve(A1, f1)
    f2 = np.linalg.solve(A2, f2)


    # Lax-Friedrich
    f1[1:Ngrid - 1] = 1/2*(f1[2:]+f1[:Ngrid - 2]) - alpha*(f1[2:] - f1[:Ngrid-2])
    f2[1:Ngrid - 1] = 1 / 2 * (f2[2:] + f2[:Ngrid - 2]) - alpha * (f2[2:] - f2[:Ngrid - 2])

    plt1.set_ydata(f1)
    plt2.set_ydata(f2)

    fig.canvas.draw()
    plt.pause(0.01)
    cnt += 1
