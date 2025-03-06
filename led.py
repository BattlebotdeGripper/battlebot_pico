from machine import Pin
import time
class Led:
        
    def __init__(self):
        self.led = Pin(1, Pin.OUT)

    def set_led_on(self):
        self.led.value(1)
        print(self.led.value())
        
    def set_led_off(self):
        self.led.value(0)
        print(self.led.value())
        
    def run(self):
        while True:
            self.set_led_on()
            time.sleep(1)
            self.set_led_off()
            time.sleep(1)