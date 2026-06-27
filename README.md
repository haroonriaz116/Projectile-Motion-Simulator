# Projectile Motion Simulator

A Pygame-based simulator that animates a projectile's flight path and calculates its landing range from user-supplied launch velocity, angle, and height.

## How it works

* The player enters a launch velocity in meters per second, a launch angle in degrees, and a launch height in meters through console prompts that are mirrored as text on the simulation window.
* The launch angle is converted to radians and decomposed into horizontal and vertical velocity components, which are used together with the launch height to compute the projectile's total horizontal range using the standard projectile motion range equation.
* The calculated range is printed to the console before the animation begins.
* A red circle representing the projectile is animated frame by frame from its starting position, with its horizontal position advancing at a constant rate and its vertical position following gravitational acceleration, until it returns to its original height and the animation stops.
* Once the projectile lands, the player is asked whether they would like to run another calculation with new inputs.
* Invalid numeric input at any prompt triggers an on-screen error message before the prompt is shown again.

## Tech stack

The simulator is written in Python and relies on the Pygame library for windowing, rendering, event handling, and timing, along with the standard math module for trigonometric and range calculations.

## Project structure

```
projectile-motion-simulator/
└── Projectile-Motion-Simulator.py
```

## Running it locally

Clone the repository, install Pygame, and run the script directly:

```
git clone https://github.com/your-username/projectile-motion-simulator.git
cd projectile-motion-simulator
pip install pygame
python Projectile-Motion-Simulator.py
```

## Design notes

The projectile's position is recalculated each frame from elapsed time rather than incrementally updated, so the trajectory stays accurate to the underlying kinematic equations regardless of frame rate. Landing is detected by comparing the projectile's current height against its original launch height, allowing the same logic to handle launches from ground level as well as from an elevated starting point.

## Contact

Haroon Riaz — haroonriaz116@gmail.com
