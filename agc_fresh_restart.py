# agc_fresh_restart.py
from agc_utils import mask_15bit, store_to_memory

class AGCFreshRestart:
    def __init__(self):
        self.memory = {
            "A": 0,         # Accumulator
            "PHASE": 0,     # Current phase
            "STATE": 0      # System state flag (0=reset, 1=running)
        }
        self.restart_table = {1: 2000, 2: 2100}  # Simplified phase-to-address table

    def fresh_start(self):
        """Simulate a fresh start: Reset key registers."""
        store_to_memory("A", 0, self.memory)
        store_to_memory("PHASE", 0, self.memory)
        store_to_memory("STATE", 0, self.memory)
        return self.memory["STATE"]

    def restart(self, phase):
        """Simulate a restart: Restore from phase."""
        store_to_memory("PHASE", mask_15bit(phase), self.memory)
        restart_addr = self.restart_table.get(phase, 0)
        store_to_memory("STATE", 1, self.memory)
        return restart_addr

    def main(self):
        """Sanity check for AGCFreshRestart."""
        print(f"Initial: A={self.memory['A']}, PHASE={self.memory['PHASE']}, STATE={self.memory['STATE']}")
        # Perform fresh start
        state = self.fresh_start()
        print(f"Fresh Start: A={self.memory['A']}, PHASE={self.memory['PHASE']}, STATE={state}")
        # Perform restart with phase 1
        addr = self.restart(1)
        print(f"Restart Phase 1: PHASE={self.memory['PHASE']}, STATE={self.memory['STATE']}, ADDR={addr}")

if __name__ == "__main__":
    fresh_restart = AGCFreshRestart()
    fresh_restart.main()