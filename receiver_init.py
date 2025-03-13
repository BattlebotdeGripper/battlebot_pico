import sys

class Receiver_init:
    def __init__(self):
        pass
    
    
    def receive(self):
        while True:
            data = sys.stdin.readline().strip()
            if data:                
                return data
            