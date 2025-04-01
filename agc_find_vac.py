# agc_find_vac.py
from agc_utils import mask_15bit, store_to_memory, AGCMemory

class AGCFindVac:
    def __init__(self):
        self.memory = AGCMemory()

    def allocate_vac(self, size):
        addr = self.memory.allocate_vac(size)
        print(f"Allocated VAC at {addr}")
        return addr

    def main(self):
        self.allocate_vac(5)