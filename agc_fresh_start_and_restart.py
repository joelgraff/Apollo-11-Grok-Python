# agc_fresh_start_and_restart.py
from agc_utils import mask_15bit, store_to_memory

class AGCFreshStartAndRestart:
    def __init__(self):
        self.memory = {
            "STATE": 0,    # System state (0=normal, 1=fresh start)
            "RESET": 0     # Reset flag (0=off, 1=on)
        }

    def fresh_start(self):
        """Simulate a fresh start."""
        store_to_memory("STATE", 1, self.memory)
        store_to_memory("RESET", 1, self.memory)
        return self.memory["STATE"]

    def main(self):
        """Sanity check for AGCFreshStartAndRestart."""
        print(f"Initial: STATE={self.memory['STATE']}, RESET={self.memory['RESET']}")
        state = self.fresh_start()
        print(f"Fresh Start: STATE={state}, RESET={self.memory['RESET']}")

if __name__ == "__main__":
    fresh = AGCFreshStartAndRestart()
    fresh.main()