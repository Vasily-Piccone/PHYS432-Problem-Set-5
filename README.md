# PHYS432-Problem-Set-5
 This contains the code for two numerical methods problems; solving the advection equation, and solving the advection-diffusion equation.

### NAME: 
Vasily Piccone

### VERSION OF PYTHON:
3.x

### LIBRARIES USED:
Matplotlib, Numpy

### .py FILES 
#### advection.py 
This file solves the advection equation using two numerical methods schemes; Lax-Friedrich's method and the Forward-Time Central Space (FTCS) scheme. The results are then plotted in the form of a 2D animation.

#### diffadvect.py 
This file solves the advection-diffusion coefficient by means of operator-splitting, where the advection part is solved via the Lax-Friedrich method, and the diffusion part is solved via an implicit scheme. The Advection-Diffusion equation is solved for two different diffusion coefficients. The "no-slip" boundary conditions are imposed on the diffusion part of the solution. As in the "advection.py" file, the resulting solutions are then plotted in form of a 2D animation.
