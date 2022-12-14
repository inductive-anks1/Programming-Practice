import sys
sys.path.append("G:\Python Programming")

import math
import matplotlib.pyplot as plt 
from Vectors import Vector

class SolarSystem:
    
    def __init__(self, size):
        self.size = size
        self.bodies = []
        
        self.fig, self.ax = plt.subplots(1, 1,
                                         subplot_kw = {"projection":"3d"},
                                         figsize = (self.size/50, self.size/50),)
        self.fig.tight_layout()
        
    def add_body(self, body):
        self.bodies.append(body)

class SolarSystemBody:
    min_display_size = 10
    display_log_base = 1.3
    
    def __init__(
            self,
            solar_system,
            mass,
            position = (0, 0, 0),
            velocity = (0, 0, 0),
            ):
        self.solar_system = solar_system
        self.mass = mass
        self.position = position
        self.velocity = Vector(*velocity)
        self.display_size = max(
            math.log(self.mass, self.display_log_base),
            self.min_display_size,
            )
        self.colour = "black"
        
        self.solar_system.add_body(self)
        
    def move(self):
        self.position = (
            self.position[0] + self.velocity[0],
            self.position[1] + self.velocity[1],
            self.position[2] + self.velocity[2],
            )
    
    def draw(self):
        self.solar_system.ax.plot(
            *self.position,
            marker = "o",
            markersize = self.display_size,
            colour = self.colour)
        
solar_system = SolarSystem(400)
plt.show()

body = SolarSystemBody(solar_system, mass = 100, position = (0, 0, 0), velocity=(1, 1, 1))
body.draw()
body.show()
body.draw()


        
        










        