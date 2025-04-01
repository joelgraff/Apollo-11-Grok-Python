# agc_p20_p25.py
import time
from agc_utils import mask_15bit, store_to_memory, AGCMemory, DSKYMock

class AGCP20P25:
    def __init__(self):
        self.memory = AGCMemory()
        self.dsky = DSKYMock()

    def rendezvous_navigation(self, range_val):
        store_to_memory("P20_RANGE", mask_15bit(range_val), self.memory.erasable)
        self.dsky.show(f"Range: {range_val}")
        for _ in range(3):  # Simulate tracking updates
            range_val -= 100
            self.dsky.show(f"Range: {range_val}")
            time.sleep(0.1)
        print("Rendezvous Tracking Complete")

    def main(self):
        print("Starting P20-P25 Rendezvous")
        self.rendezvous_navigation(10000)