# Tesla class

This project is based on Python 3. It consist of [1 class](https://github.com/ovidijusku/sftwengineering/blob/main/Tesla/tesla.py#L1).

### Installation

> git clone https://github.com/ovidijusku/sftwengineering.git

### Access

> from tesla import Tesla

### Creating object

> new_car = Tesla("3","silver")

At least two arguments are expected: model and color.

### Methods

> .color - return color of the car

> .autopilot(obstacle: str) - if autopilot mode is on, returns string "Tesla model {model} avoids {obstacle}"

> .seatscount - returns number of seats in the car

> .unlock() - unlocks the car
