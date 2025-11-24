# Exercise 2: Random walk

- [Link to notebook PDF](./[Jayadevan]-Ex02.pdf
)

In this exercise, numerical calculations are done to show how a Gaussian distribution emerges from
a random walk, and how the distribution’s first three moments depend on the number of both steps
and independent walks.

## Background

In the lecture, you were introduced to the "random walk" as simple model for e.g. diffusion processes, and how it results in a Gaussian probability distribution concerning its endpoints. 
In this exercise, you will:

1. perform numerical calculations to show how a Gaussian distribution emerges from a random walk, and how the distribution’s first three moments depend on the number of both steps and independent walks.
2. (THEORY EXERCISE) show analytically that a random walk is a solution to the diffusion equation.

## Task I: implementation
- Generate a function that produces a random walk in one dimension $x$:
    - For step $N = 0$, Start at $x = 0$
    - Draw a number r from a uniform distribution between 0 and 1
    - If $r \geq 0.5$ add $1$ to $x$, else add $-1$ to $x$
- Organize the output such that the full random walk is written out.

## Task II: simulation and evaluation
- Run $n = 10000$ random walks of $N = 20000$ steps each (that should only take ca. 2 minutes calculation time)
- Plot histograms of the distribution of $x$ for all $n = 10000$ random walks for $N = 100$, $1000$, $10000$ and $20000$.
- For $N = 100$, $1000$, $10000$ and $20000$, check the convergence of all walks check in dependence of $n$ for
    - the first moment, i.e. the mean $\langle x \rangle$,
    - the second moment, i.e. the variance $\langle(x - \langle x \rangle)^2 \rangle$ and
    - the third moment, giving the skewness $\langle(x - \langle x \rangle)^3\rangle$.

## Task III: random walks and the diffusion equation (THEORY EXERCISE)

Usually, random walks are not rationalized in the form of number of steps $N$, but in form of the time increment ("step") $\Delta t$ an individual step takes and the walk time $t = N \Delta t$. In the limit of long length and time scales (i.e., a large number of steps), the evolution of random walks is described by the *diffusion equation*

$$ \dfrac{\partial P}{\partial t} = D \dfrac{\partial^2 P}{\partial x^2} $$

with the evolving probability density $P(x, t)$ to find the "walker" at a $x$ of choice at time $t$ and the diffusion constant $D$.

Using the probability density of a random walk 

$$ P(x) = (2\pi N)^{-1/2} \exp \left( - \dfrac{x^2}{2N} \right), $$

show that a random walk is a solution to the diffusion equation with

$$ D = \dfrac{x_0^2}{2\Delta t} $$

with step size $x_0^2$.

*Hint*: bear in mind that $P(x)$ then turns into a time-dependent distribution $P(x,t)$.