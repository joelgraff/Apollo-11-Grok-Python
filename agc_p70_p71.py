# agc_p70_p71.py
import time
from agc_utils import mask_15bit, store_to_memory, AGCMemory

class AGCP70P71:
    def __init__(self):
        self.memory = AGCMemory()
        self.thrust = 0

    def abort_maneuver(self, thrust):
        self.thrust = thrust
        store_to_memory("P70_THRUST", mask_15bit(thrust), self.memory.erasable)
        print(f"Abort Thrust: {thrust}")
        for _ in range(3):  # Simulate ascent
            print("Ascending...")
            time.sleep(0.1)
        print("Abort Complete")

    def main(self):
        print("Starting P70-P71 Abort")
        self.abort_maneuver(600)