# agc_fresh_start_subroutines.py
from agc_utils import mask_15bit, store_to_memory, AGCMemory

class AGCFreshStartSubroutines:
    def __init__(self):
        self.memory = AGCMemory()

    def reset_system(self):
        self.memory.erasable.clear()
        store_to_memory("STATE", mask_15bit(1), self.memory.erasable)
        print("System Reset")

    def main(self):
        self.reset_system()