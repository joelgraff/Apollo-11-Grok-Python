# agc_descent_guidance.py
import time
from agc_utils import mask_15bit, store_to_memory, AGCMemory

class AGCDescentGuidance:
    def __init__(self):
        self.memory = AGCMemory()
        self.alt = 0
        self.vel = 0

    def guide_descent(self, alt, vel, throttle):
        self.alt = alt
        self.vel = vel
        while self.alt > 0 and self.vel > 0:
            self.alt -= max(1, self.vel * throttle // 100)  # Altitude drop based on throttle
            self.vel -= throttle // 10  # Faster velocity reduction
            if self.alt < 0: self.alt = 0
            store_to_memory("DESC_ALT", mask_15bit(self.alt), self.memory.erasable)
            store_to_memory("DESC_VEL", mask_15bit(self.vel), self.memory.erasable)
            print(f"Descent: Alt {self.alt}, Vel {self.vel}")
            time.sleep(0.1)
        print("Descent Complete")

    def main(self):
        print("Starting Descent Guidance")
        self.guide_descent(3000, 30, 50)