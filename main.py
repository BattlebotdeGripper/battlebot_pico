import time
from drive import Drive
from gripper import Gripper
from receiver_init import Receiver_init

class Control:
    def __init__(self, receiver_init, drive, gripper):
        self.receiver_init = receiver_init
        self.drive = drive
        self.gripper = gripper
        
    def run(self):
        while True:
            serial_data = self.receiver_init.receive()
            if serial_data:
                try:
                    wheel_a, wheel_b, gripper_value = serial_data
                    self.drive.run(wheel_a, wheel_b)
                    self.gripper.run(gripper_value)
                except ValueError:
                    print("Invalid data received")
            time.sleep(0.1)

if __name__ == "__main__":
    receiver_init = Receiver_init()
    drive = Drive()
    gripper = Gripper(18)
    control = Control(receiver_init, drive, gripper)
    
    try:         
        control.run()
    except Exception as e:
        print(f"Error: {e}")