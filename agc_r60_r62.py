# agc_r60_r62.py
import time
from agc_utils import mask_15bit, store_to_memory, AGCMemory

class AGCR60R62:
    def __init__(self):
        self.memory = AGCMemory()
        self.att_error = 0

    def perform_maneuver(self, error):
        self.att_error = error
        cmd = mask_15bit(error * 4)
        store_to_memory("MANEUVER", cmd, self.memory.erasable)
        print(f"Maneuver Command: {cmd}")
        return cmd

    def main(self):
        print("Testing R60-R62 Maneuver")
        self.perform_maneuver(15)
        time.sleep(0.1)  # Added for consistency