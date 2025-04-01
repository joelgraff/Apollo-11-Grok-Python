# agc_tuning_parameters.py
from agc_utils import mask_15bit, store_to_memory, AGCMemory

class AGCTuningParameters:
    def __init__(self):
        self.memory = AGCMemory()

    def set_tuning(self, t1, t2):
        store_to_memory("TUNE1", mask_15bit(t1), self.memory.erasable)
        store_to_memory("TUNE2", mask_15bit(t2), self.memory.erasable)
        print(f"Tuning Set: T1={t1}, T2={t2}")

    def main(self):
        print("Testing Tuning Parameters")
        self.set_tuning(10, 20)