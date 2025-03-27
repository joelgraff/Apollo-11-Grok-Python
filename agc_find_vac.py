# agc_find_vac.py
from agc_utils import mask_15bit, store_to_memory

class AGCFindVac:
    def __init__(self):
        self.memory = {
            "VACSTART": 0,  # Start address of vacant area
            "VACSIZE": 0    # Size of vacant area (words)
        }
        self.vac_table = {0: 100, 1: 0}  # Simplified: {busy flag: address}

    def find_vacant(self, size):
        """Simulate finding a vacant memory block."""
        store_to_memory("VACSIZE", mask_15bit(size), self.memory)
        # Find first non-busy slot (simplified)
        vac_addr = self.vac_table.get(0, 0)
        store_to_memory("VACSTART", mask_15bit(vac_addr), self.memory)
        return vac_addr

    def main(self):
        """Sanity check for AGCFindVac."""
        print(f"Initial: VACSTART={self.memory['VACSTART']}, VACSIZE={self.memory['VACSIZE']}")
        addr = self.find_vacant(10)  # Request 10 words
        print(f"Find Vacant: VACSTART={addr}, VACSIZE={self.memory['VACSIZE']}")

if __name__ == "__main__":
    find_vac = AGCFindVac()
    find_vac.main()