# Exercise IV: Free energies

- [Link to notebook PDF](./[Jayadevan]-Ex04-Free_Energy.pdf)

## Background
In the lecture we discussed the free energy landscape $\Delta F(r) = -k_{B} T\ \ln g(r)$ with the radial distribution function (RDF) $g(r)$. The RDF is an important observable to evaluate the internal ordering of particles within gaseous, liquid, solid, or amorphous phases, respectively. It can be calculated from MD simulations and experimentally measured by, e.g., X-ray or neutron scattering.

## Task I: simulation

- Create a 2D box with the dimensions $10 \text{nm} \times 10 \text{nm}$ with periodic boundary conditions.
- Create $100$ spherical particle with radius $r = 0.2$ nm (either at random positions or on an regular grid) and mass $m = 2$ g / mol.
- Assign a velocity $v$ with $|v|=0.5$ nm/ns and random direction to each particle.
- For collisions, use the "hard spheres" collision method from the first exercise.
- Carry out a simulation of $5000$ steps with a time step length $\Delta t = 0.1$ nm per step.

## Task II: radial distribution function
The RDF displays the average number of particles dn that can be found for each particle at a distance $r$ within the sphere shell (in 3D) or the ring area (in 2D) between $r$ and $r+dr$. Use a $dr$ of ca. $0.01$ nm.

- What is the maximal distance $r$ for which you can evaluate the RDF?
- Calculate and display the time- and particle-averaged 2D RDF $g(r) = \dfrac{1}{2\pi r\rho}\dfrac{d n(r)}{dr}$ with the distance $r$ and the number density $\rho$ of the simulated box.
- *Hint I*: as for the case with the time step: in data evaluation, infinitesimally small intervals need to be approximated by suitably small finite intervals.
- *Hint II*: remember that you deal here with periodic boundary conditions, i.e., you need to calculate distances over the borders, as well.
- *Hint III*: In the system setup as used by us, the mass is not of importance for the system's dynamics, but you will need it to calculate the temperature in hindsight.

## Task III: potential of mean force

- You first need to determine the system temperature from the mean kinetic energy per particle. Remember that we simulate in 2D, so the particles exhibit 2 degrees of freedom.
- What is the temperature in the simulated box?
- Calculate and plot the two-particle $\Delta F(r)$. Remember: Minima in $\Delta F(r)$ correspond to stable states.
- The value of $\Delta F(r)$ may appear odd at first glance. Why is that so?