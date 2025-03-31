# agc_luminary.py
from agc_utils import mask_15bit, store_to_memory

class AGCLuminary:
    def __init__(self):
        self.memory = {
            "LUM_VER": 0,    # Luminary version (scaled)
            "LUM_STATE": 0   # System state (0=off, 1=on)
        }

    def set_luminary(self, version):
        """Simulate Luminary system initialization."""
        store_to_memory("LUM_VER", mask_15bit(version), self.memory)
        store_to_memory("LUM_STATE", 1, self.memory)
        return self.memory["LUM_VER"]

    def main(self):
        """Sanity check for AGCLuminary."""
        print(f"Initial: LUM_VER={self.memory['LUM_VER']}, LUM_STATE={self.memory['LUM_STATE']}")
        version = self.set_luminary(99)  # Luminary 99
        print(f"Luminary Set: LUM_VER={version}, LUM_STATE={self.memory['LUM_STATE']}")

if __name__ == "__main__":
    luminary = AGCLuminary()
    luminary.main()