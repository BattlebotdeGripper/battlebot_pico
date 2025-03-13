import usb_cdc

class Receiver_init:
    def __init__(self):
        self.usb = usb_cdc.data
    
    def receive(self):
        if self.usb.any():
            raw_data = self.usb.readline().strip()
            try:
                data_str = raw_data.decode("utf-8").strip("()\n\r")
                wheel_a, wheel_b, gripper = map(int, data_str.split(","))
                return (wheel_a, wheel_b, gripper)
            except (ValueError, AttributeError):
                return None
        return None