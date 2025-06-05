import time
from movement import Movement

class Gripper(Movement):
    def __init__(self):
        super().__init__(pins=[22])  

    def gripperOn(self, gripper):
        self.move([gripper])
        print("Gripper on")
        
    def gripperOff(self, gripper):
        self.move([gripper])
        print("Gripper off")
        
    def trigger_neutral(self):
        self.setup_and_stop_esc()

    def run(self, gripper):
        gripper = max(min(gripper, 2000), 1000)
        print(gripper)
        
        if gripper > 1500:
            self.gripperOn(gripper)
        elif gripper < 1500 :
            self.gripperOff(gripper)
        else:
            self.trigger_neutral()