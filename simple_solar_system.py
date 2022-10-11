from Planets_Motion import SolarSystem, Sun

solar_system = SolarSystem(width = 1400, height = 900)
sun = Sun(solar_system, mass = 10_000, velocity = (0.25, 0.25))

while True:
    solar_system.update_all()