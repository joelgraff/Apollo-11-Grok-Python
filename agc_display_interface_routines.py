# agc_display_interface_routines.py
from agc_utils import mask_15bit, store_to_memory, AGCMemory, DSKYMock

class AGCDisplayInterfaceRoutines:
    def __init__(self):
        self.memory = AGCMemory()
        self.dsky = DSKYMock()

    def display_data(self, noun, value):
        store_to_memory(f"NOUN_{noun}", mask_15bit(value), self.memory.erasable)
        self.dsky.show(f"N{noun}: {value}")

    def main(self):
        self.display_data(1, 1234)
        self.display_data(2, 5678)