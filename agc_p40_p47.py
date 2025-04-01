# agc_p40_p47.py
import time
from agc_utils import mask_15bit, store_to_memory, AGCMemory

class AGCP40P47:
    def __init__(self):
        self.memory = AGCMemory()
        self.thrust = 0

    def engine_control(self, thrust):
        self.thrust = thrust
        cmd = mask_15bit(thrust)
        store_to_memory("P40_THRUST", cmd, self.memory.erasable)
        print(f"Engine Thrust: {thrust}")
        time.sleep(0.2)  # Simulate burn
        print("Engine Burn Complete")

    def main(self):
        print("Starting P40-P47 Engine Control")
        self.engine_control(500)