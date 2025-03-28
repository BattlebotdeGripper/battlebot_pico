import time
from machine import SPI, Pin
from mcp2515 import MCP2515
from drive import Drive
from gripper import Gripper


def decode_can_data(data):
    values = []

    for i in range(0, len(data), 2):
        high = data[i]           # eerst high byte
        low = data[i + 1]        # dan low byte
        value = (high << 8) | low
        values.append(value)

    return values



spi = SPI(0, baudrate=10000000, polarity=0, phase=0, sck=Pin(18), mosi=Pin(19), miso=Pin(16))
cs = Pin(17, Pin.OUT)

can = MCP2515(spi, cs)
can.init_mcp2515()

while True:
    message = can.receive_can_message()

    if message:
                
        drive = Drive()
        gripper = Gripper()
 
        can_id, data = message
        decoded = decode_can_data(data)
        
        # left_wheel = wiel_A
        left_wheel = decoded[0]
        
        # right_wheel = wiel_B
        right_wheel = decoded[1]
        
        
        gripper = decoded[2]
        
        try:
            drive.run(left_wheel, right_wheel)
#             gripper.run(gripper)
        except Exception as e:
            print(e)
        print(f" DEC: left_wheel: {decoded[0]}, right_wheel: {decoded[1]}")

    time.sleep(0.1)  # zo laag mogelijk houden (0.1)
    
