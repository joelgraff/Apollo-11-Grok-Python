# agc_pinball_noun_tables.py
from agc_utils import mask_15bit, store_to_memory, AGCMemory, DSKYMock

class AGCPinballNounTables:
    def __init__(self):
        self.memory = AGCMemory()
        self.dsky = DSKYMock()
        self.nouns = {1: "Altitude", 2: "Velocity"}

    def set_noun(self, noun, value):
        store_to_memory(f"NOUN_{noun}", mask_15bit(value), self.memory.erasable)
        self.dsky.show(f"{self.nouns.get(noun, 'Unknown')}: {value}")

    def main(self):
        print("Testing Pinball Noun Tables")
        self.set_noun(1, 1234)
        self.set_noun(2, 567)