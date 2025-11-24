# Bonus Exercise: Agent simulation on contagion spread
Lecture Classical Complex Systems WS23/24 Exercises
Distributed: Friday, 2023-12-22

## Background
Simple particle simulations can be used in a wide range of modelling approaches, even the modelization of behavior or crowds of humans. In this case, each particle is called an "agent". As a bonus "Christmas task", we will use the hard spheres simulations from earlier exercises to check the effect of vaccinations and the compliance of the people with it.

# Task I: Implementation

Add the following parameters to your hard spheres simulation code:
- Give the hard spheres three new properties: "healthy", "infected" and "immunized".
- At the start of a simulation, one particle is "infected", a given percentage (corresponding to the percentage of vaccinated people) is "immunized", all others are "healthy".
- At each collision of an infected particle with a healthy particle, the healthy particle becomes infected, as well.
- At each collision of an infected particle with an "immunized" particle, the immunized particle becomes infected with a 20% chance - this would be a "breakthrough" infection then. (Nota bene: I took this number out of my head - it does not reflect any real-world data. Feel free to adjust in case you know, e.g., the vaccination protection strength against current Covid variants.)
- After 500 steps, an infected particle becomes "immunized".
- Under these rules re-infections can occur, too.

# Task II: Simulation

- Create a 2D box with the dimensions 50x50 nm2. and without periodic boundary conditions.
- Create 50 hard sphere particles with radius r = 0.5 nm (either at random positions or on a regular grid).
- Assign a velocity v with |v|=0.5 nm/step and random direction to each particle.
- At the box borders AND at particle contact, the particles shall be reflected upon impact in the form of an elastic collision (no loss of kinetic energy).
- The interparticle collision momentum and kinetic energy exchange itself shall be modeled based on the collision of two "hard spheres".
- Carry out a simulation of 10000 steps.
- Run the simulations once with all particles moving, and once each where 20%, 50%, 80% and 90% are vaccinated, i.e., immunized.

# Task III: Data Evaluation of positions

- Compare the number of "infected" particles in the four simulations over time.
- Interpret the results in the scope of how efficient a vaccination campaign depending on the percentage of vaccinated population is:
    - How well does the vaccine help to flatten the curve of infected people over time?
    - Is the virus eradicated at some point, or is there always a basin of infected people remaining ("endemic situation")?
- If you want to: vary the 20% chance of "breakthrough" infections up and down. See what is the outcome.