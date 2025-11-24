# Classical Complex Systems (Selected Exercises Archive)

Archive of a few of the selected graded exercises I completed from the course "Classical Complex Systems" I completed during the winter semester 2023 at the University of Freiburg.

## Highlights

- Final grade for course (evaluated from the [final project](./Final_Project/)): **1.3** (1.0 being the best and 4.0 the lowest)
- [Final project](./Final_Project/): PCA Analysis on protein simulation data
- Average grade from all completed (10) exercises: 75%

## Instructions

The exercises were solved using Python, documented as Jupyter notebooks. 

To run the notebooks, a virtual environment with the packages described in [the requirements file](./requirements.txt) is recommended. 

If you use [uv](https://docs.astral.sh/uv/) for package management, download the [TOML file](./pyproject.toml) file into your project folder and run:

```bash
uv sync
```

to set up the right package versions.

# Course Description:
([source](https://www.physik.uni-freiburg.de/studium/vorlesungsverzeichnis/kmvrlw23.htm#Classical_Complex_Systems))

Classical Complex Systems

**Lecturer**: Prof. Dr. G. Stock

9 ECTS

Start: 16.10.2023

Complex systems are composed of many interacting or reacting elements with stochastic components and are found essentially everywhere, ranging, for example, from dense liquids in condensed matter physics to molecular reactions in chemistry and biology, up to macroscopic predator-prey populations, pandemic spreading and markets in economics. This lecture introduces selected statistical tools and numerical approaches to study and describe the physics of the complex phenomena in classical (non-quantum) many-body systems, with a particular focus on the mesoscale modeling of macromolecular liquids, their structure-property relations, diffusive processes and kinetics, and applications to molecular reactions and nonlinear systems. After an introduction to the statistical mechanics of interacting systems and stochastic processes, generally applicable statistical theories such as Langevin and Master equation approaches as well as basic computational strategies such as Monte-Carlo (MC) and Brownian Dynamics (BD) simulations will be discussed. The lessons are accompanied by analytical as well as numerical exercises. The latter provide a hands- on implementation of the stochastic (MC and particle-based reaction-diffusion) simulation methods, with applications to structure and dynamics of interacting systems as well as (molecular) reaction kinetics.
