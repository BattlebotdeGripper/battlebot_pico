from movement import Movement
import time

class Drive(Movement):
    def __init__(self):
        super().__init__(pins=[20, 21])
        # GP_PIN_20 = Links (geel)
        # GP_PIN_21 = Rechts (groen)
        

    def moveForward(self, left_wheel, right_wheel):
        self.move([left_wheel, right_wheel]) 
        print("Moving forward")

    def moveBackwards(self, left_wheel, right_wheel):
        self.move([left_wheel, right_wheel]) 
        print("Moving backwards")

    def turnRight(self, left_wheel, right_wheel):
        self.move([left_wheel, right_wheel]) 
        print("Turning right")

    def turnLeft(self, left_wheel, right_wheel):
        self.move([left_wheel, right_wheel]) 
        print("Turning left")
        
    def trigger_neutral(self):
        self.setup_and_stop_esc()

    def run(self, left_wheel, right_wheel):
        left_wheel = max(min(left_wheel, 2000), 1000)
        right_wheel = max(min(right_wheel, 2000), 1000) 
        print(left_wheel, right_wheel)
        
        if left_wheel > 1500 and right_wheel > 1500:
            self.moveForward(left_wheel, right_wheel)
        elif left_wheel < 1500 and right_wheel < 1500:
            self.moveBackwards(left_wheel, right_wheel)
        elif left_wheel > right_wheel:
            self.turnRight(left_wheel, right_wheel)
        elif left_wheel < right_wheel:
            self.turnLeft(left_wheel, right_wheel)
#         elif left_wheel == 1500 and right_wheel == 1500:
        else:
            self.trigger_neutral()
#             break
