from movement import Movement

class Gripper(Movement):
    def __init__(self):
        super().__init__(pins=[18])  

    def run(self, gripper_value):
        gripper_value = max(min(gripper_value, 2000), 1000)
        self.move([gripper_value]) 
        print(f"Gripper state: {gripper_value}")
