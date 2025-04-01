# agc_throttle_control_routines.py
from agc_utils import mask_15bit, store_to_memory, AGCMemory

class AGCThrottleControlRoutines:
    def __init__(self):
        self.memory = AGCMemory()
        self.throttle = 0

    def set_throttle(self, percent):
        self.throttle = min(100, max(0, percent))
        cmd = mask_15bit(self.throttle * 10)  # Scale to AGC range
        store_to_memory("THROT_CMD", cmd, self.memory.erasable)
        print(f"Throttle Set: {self.throttle}%")
        return cmd

    def main(self):
        print("Testing Throttle Control")
        self.set_throttle(75)
        self.set_throttle(50)