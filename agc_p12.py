# agc_p12.py
import time
from agc_utils import mask_15bit, store_to_memory, AGCMemory

class AGCP12:
    def __init__(self):
        self.memory = AGCMemory()
        self.alt = 0

    def ascent_guidance(self, alt, vel):
        self.alt = alt
        while self.alt < 10000:  # Simulate ascent to orbit
            self.alt += vel
            store_to_memory("P12_ALT", mask_15bit(self.alt), self.memory.erasable)
            print(f"Ascent: Alt {self.alt}")
            time.sleep(0.1)
        print("Ascent to Orbit Complete")

    def main(self):
        print("Starting P12 Ascent")
        self.ascent_guidance(0, 1000)