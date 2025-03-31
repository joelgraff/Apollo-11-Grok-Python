# agc_r29.py
from agc_utils import mask_15bit, store_to_memory

class AGCR29:
    def __init__(self):
        self.memory = {
            "R29_STATE": 0,   # R29 state (0=off, 1=on)
            "R29_DATA": 0     # R29 radar data (scaled)
        }

    def run_r29(self, data):
        """Simulate R29 radar designation."""
        store_to_memory("R29_STATE", 1, self.memory)
        store_to_memory("R29_DATA", mask_15bit(data), self.memory)
        return self.memory["R29_DATA"]

    def main(self):
        """Sanity check for AGCR29."""
        print(f"Initial: R29_STATE={self.memory['R29_STATE']}, R29_DATA={self.memory['R29_DATA']}")
        data = self.run_r29(3000)
        print(f"R29 Ran: R29_STATE={self.memory['R29_STATE']}, R29_DATA={data}")

if __name__ == "__main__":
    r29 = AGCR29()
    r29.main()