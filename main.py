import time
from machine import SPI, Pin
from mcp2515 import MCP2515
from led import Led

spi = SPI(0, baudrate=10000000, polarity=0, phase=0, sck=Pin(18), mosi=Pin(19), miso=Pin(16))
cs = Pin(17, Pin.OUT)

can = MCP2515(spi, cs)
can.init_mcp2515()

while True:
    message = can.receive_can_message()
    print(message)
    if message:
        can_id, data = message
        
        if can_id == 0x200:
            led = Led()
            if data[0] == 0x01:
                led.set_led_on()
            elif data[0] == 0x00:
                led.set_led_off()
            
    time.sleep(0.1)
