from machine import Pin, PWM

class Movement:
    def __init__(self, pins):
        self.min_duty = 1000
        self.neutral = 1500
        self.max_duty = 2000
        self.esc = [PWM(Pin(pin)) for pin in pins] 
        self.setup_esc()

    def _us_to_duty(self, us):
        return int((us * 65535) / 20000)  

    def setup_esc(self):
        for esc in self.esc:
            esc.freq(50)
            esc.duty_u16(self._us_to_duty(self.neutral))

    def move(self, duty_cycles):
        for esc, duty in zip(self.esc, duty_cycles):
            if self.min_duty <= duty <= self.max_duty:
                esc.duty_u16(self._us_to_duty(duty))