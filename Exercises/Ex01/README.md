## Background:

Irrespective of the start conditions, velocity distributions in multi-particle systems with collisions between particles converge to a Maxwell-Boltzmann distribution. You will investigate this effect by creating your own simulation of a multi-particle systems of hard spheres in a 2D-box.

## Task I: implementation
- Start with the code for a single particle moving in a box provided to you before.
- Add a “periodic boundary condition” algorithm: if a particle leaves one side of the box, it re-enters the box on the other side. Hint: use a "modulo" operator.
- Extend the code to allow the calculation of a trajectory of a multi-particle system.
- Implement an algorithm to take into account elastic collisions of hard spheres.
- Implement a function that checks if such a collision is happening ("nearest neighbor search") after a jump in time.

## Task II: simulation
- Create a 2D box with the dimensions $20\times 20$ nm$^2$.
- Create 50 spherical particles with radius $r = 0.5$ nm (either at random positions or on a regular grid). All particles have the same mass, and therefore the absolute mass can be ignored (why?).
- Assign a velocity $v$ with $|v|=0.5$ nm per numerical iteration step and random direction to each particle.
- Use the same Euler integrator scheme as in the 1st exercise.
- Take into account periodic boundary conditions
- At particle contact, the particles shall be reflected upon impact in the form of an elastic collision (no loss of kinetic energy). The interparticle collision momentum and kinetic energy exchange itself shall be modeled based on the collision of two "hard spheres".
    - Hint I: think about how to calculate the correct reflection angle for interparticle collisions.
    - Hint II: with finite simulations steps as usually employed in numerical simulations, it is practically not possible to perform hard sphere collisions exactly when spheres are in contact with each other. You can either approximate the collisions as taking place with a small overlap of spheres, you can come up with a way to set particles back to a surface contact (intermediate), or you can tune the step size in such a way that a collision is taken into account exactly at the right time.
- Carry out a simulation of 2000 steps.

### Task III: Analysis of velocity distributions

- Check the probability of velocities for the trajectory at the beginning (the first 10% of the trajectory) and at the end (the last 10% of the trajectory) of the simulation
    - along the $x$-axis,
    - along the $y$-axis,
    - and for norms of vectors $|(x,y)|$.
- How do the respective distributions look like? How do they relate to a Maxwell-Boltzmann distribution?
- Repeat the simulations with an initial velocity $|v|=1.0$ nm/step. How do the distributions change?