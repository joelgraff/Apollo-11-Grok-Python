# agc_p60_p67.py
import time
from agc_utils import mask_15bit, store_to_memory, AGCMemory, DSKYMock

class AGCP60P67:
    def __init__(self):
        self.memory = AGCMemory()
        self.dsky = DSKYMock()
        self.altitude = 0
        self.velocity = 0

    def guide_landing(self, alt, vel):
        self.altitude = alt
        self.velocity = vel
        store_to_memory("P60_ALT", mask_15bit(alt), self.memory.erasable)
        store_to_memory("P60_VEL", mask_15bit(vel), self.memory.erasable)
        # Adjusted descent: ensure velocity decreases to stop
        while self.altitude > 0 and self.velocity > 0:
            self.altitude -= max(1, self.velocity // 5)  # Faster altitude drop
            self.velocity -= 2  # Stronger deceleration
            if self.altitude < 0: self.altitude = 0
            self.dsky.show(f"Alt: {self.altitude}, Vel: {self.velocity}")
            time.sleep(0.1)
        print("Landing Complete")

    def main(self):
        print("Starting P60-P67 Landing")
        self.guide_landing(2000, 50)