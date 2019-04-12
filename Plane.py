import random

class Plane:
    MAX_CORRECTION = 5
    MAX_TURBULENCE = 15

    def __init__(self):
        self.angle = 0
        
    
    def simulate_flight(self):
        while True:
            self.do_iteration()
            

    def do_iteration(self):
        self.do_turbulence()
        self.tilt_correction()
        print("Angle is: " + str(self.angle))


    def do_turbulence(self):
        self.angle += random.randrange(-15.0, 15.0)


    def tilt_correction(self):
        correction = self.calculate_correction()
        if self.angle < 0:
            self.angle += correction
        else:
            self.angle -= correction

    
    def calculate_correction(self):
        if abs(self.angle) > Plane.MAX_CORRECTION:
            return Plane.MAX_CORRECTION

        return self.angle