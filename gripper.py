from movement import Movement

class Gripper(Movement):
    def __init__(self):
        super().__init__(pins=[10])  


    def run(self, gripper):
        gripper_value = max(min(gripper, 2000), 1000)
        self.move([gripper_value]) 
        print(f"{gripper_value}")
