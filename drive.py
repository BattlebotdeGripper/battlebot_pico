from movement import Movement

class Drive(Movement):
    def __init__(self):
        super().__init__(pins=[16, 17])
        
    def moveForward(self, wheel_a, wheel_b):
        self.move(wheel_a, wheel_b)
        print("Moving forward")

    def moveBackwards(self, wheel_a, wheel_b):
        self.move(wheel_a, wheel_b)
        print("Moving backwards")

    def turnRight(self, wheel_a, wheel_b):
        self.move(wheel_a, wheel_b)
        print("Turning right")

    def turnLeft(self, wheel_a, wheel_b):
        self.move(wheel_a, wheel_b)
        print("Turning left")

    def run(self, wheel_a, wheel_b):
        wheel_a = max(min(wheel_a, 2000), 1000)
        wheel_b = max(min(wheel_b, 2000), 1000)

        if wheel_a > 1500 and wheel_b > 1500:
            self.moveForward(wheel_a, wheel_b)
        elif wheel_a < 1500 and wheel_b < 1500:
            self.moveBackwards(wheel_a, wheel_b)
        elif wheel_a > wheel_b:
            self.turnRight(wheel_a, wheel_b)
        elif wheel_a < wheel_b:
            self.turnLeft(wheel_a, wheel_b)