import turtle
import math

class SolarSystemBody(turtle.Turtle):
    min_display_size = 20
    display_log_base = 1.1
    
    def __init__(
            self,
            solar_system,
            mass,
            position = (0, 0),
            velocity = (0, 0),
            ):
        super().__init__()
        self.mass = mass
        self.setposition(position) #Draws the object at the position.
        self.velocity = velocity
        self.display_size = max(
            math.log(self.mass, self.display_log_base),
            self.min_display_size,
            )
        
        self.penup() 
        self.hideturtle()
        
        solar_system.add_body(self) #Links the SolarSystemBody to the SolarSystem
        
    def draw(self):
        self.dot(self.display_size) #Draws a dot of teh required size
        
        
    
class Sun(SolarSystemBody):
    def __init__(
            self,
            solar_system,
            mass,
            position = (0, 0),
            velocity = (0, 0),
            ):
        super().__init__(solar_system, mass, position, velocity)
        self.color("yellow")
        

class Planet(SolarSystemBody):
    ...

class SolarSystem:
    def __init__(self, width, height):
        self.solar_system = turtle.Screen()
        self.solar_system.tracer(0) #This function is used to turn turtle animation on or off.
        self.solar_system.setup(width, height) #sets the size of the main window.
        self.solar_system.bgcolor("black") #sets the background color to black.
        
        self.bodies = []
        
    def add_bodies(self, body):
        self.bodies.append(body)
    
    def remove_body(self, body):
        self.bodies.remove(body)
        
solar_system = SolarSystem(width = 1400, height = 900)
sun = Sun(solar_system, mass = 10_000)
sun.draw() 
        
    