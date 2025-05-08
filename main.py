import time
from machine import SPI, Pin
from mcp2515 import MCP2515 
from drive import Drive  

spi = SPI(0, baudrate=10000000, polarity=0, phase=0, sck=Pin(18), mosi=Pin(19), miso=Pin(16))
cs = Pin(17, Pin.OUT)
can = MCP2515(spi, cs)
can.init_mcp2515()
drive = Drive()

last_heartbeat = time.ticks_ms()
heartbeat_timeout = 1000  # 1 seconde (match met CANEncoder heartbeat-interval)
missed_heartbeats = 0
max_missed = 5
first_heartbeat_received = False  # Alleen True na eerste heartbeat

def decodePwmData(data):
    if len(data) >= 4:  # Only need first two channels (left, right)
        left = (data[0] << 8) | data[1]
        right = (data[2] << 8) | data[3]
        return left, right
    return 1500, 1500  

def setMotors(left_pwm, right_pwm):
    print(f"Set motors: L={left_pwm}, R={right_pwm}")
    drive.run(left_pwm, right_pwm)

try:
    print("Waiting for CAN messages...")
    while True:
        msg = can.receive_can_message()
        if msg:
            can_id, can_data = msg
            print(f"CAN ID: {hex(can_id)}, Data: {can_data}")
            
            if can_id == 0x100:
                left, right = decodePwmData(can_data)
                setMotors(left, right)
            elif can_id == 0x050: 
                last_heartbeat = time.ticks_ms()
                missed_heartbeats = 0  # Reset missed count on heartbeat
                first_heartbeat_received = True  # Activeer timeout-controle
                print("Heartbeat ontvangen")
        
        # Alleen heartbeat-timeout controleren na eerste heartbeat
        if first_heartbeat_received:
            current_time = time.ticks_ms()
            time_since_last_heartbeat = time.ticks_diff(current_time, last_heartbeat)
            print(f"Debug: time_since_last_heartbeat={time_since_last_heartbeat}ms, missed_heartbeats={missed_heartbeats}/{max_missed}")
            
            if time_since_last_heartbeat > heartbeat_timeout:
                missed_heartbeats += 1
                last_heartbeat = current_time  # Reset timer voor volgende check
                print(f"Geen heartbeat ({missed_heartbeats}/{max_missed})")

                if missed_heartbeats >= max_missed:
                    print("GEEN HEARTBEAT - Fail-safe geactiveerd!")
                    setMotors(1500, 1500)
                    break  # Stop de loop (of verwijder break om te blijven luisteren)
            
        time.sleep(0.01)

except KeyboardInterrupt:
    setMotors(1500, 1500)
    print("Stopped.")
except Exception as e:
    setMotors(1500, 1500)
    print(f"Error: {e}")