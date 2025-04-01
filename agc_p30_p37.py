# agc_p30_p37.py
import time
from agc_utils import mask_15bit, store_to_memory, AGCMemory

class AGCP30P37:
    def __init__(self):
        self.memory = AGCMemory()

    def plan_maneuver(self, dv):
        time_ign = dv * 2  # Simplified ignition time
        store_to_memory("P30_DV", mask_15bit(dv), self.memory.erasable)
        store_to_memory("P30_TIME", mask_15bit(time_ign), self.memory.erasable)
        print(f"Maneuver: DV {dv}, Ignition Time {time_ign}")
        time.sleep(0.1)

    def main(self):
        print("Testing P30-P37 Maneuver Planning")
        self.plan_maneuver(300)