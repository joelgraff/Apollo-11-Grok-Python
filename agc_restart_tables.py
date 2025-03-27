# agc_restart_tables.py
from agc_utils import mask_15bit, store_to_memory

class AGCRestartTables:
    def __init__(self):
        self.memory = {
            "PHASE": 0,      # Current phase code
            "RESTART_ADDR": 0  # Restart address
        }
        # Simplified restart table: {phase: address}
        self.restart_table = {
            1: 2000,  # Phase 1 -> Address 2000
            2: 2100,  # Phase 2 -> Address 2100
            3: 2200   # Phase 3 -> Address 2200
        }

    def lookup_restart(self, phase):
        """Look up restart address for a given phase."""
        store_to_memory("PHASE", mask_15bit(phase), self.memory)
        restart_addr = self.restart_table.get(phase, 0)  # Default to 0 if not found
        store_to_memory("RESTART_ADDR", mask_15bit(restart_addr), self.memory)
        return self.memory["RESTART_ADDR"]

    def main(self):
        """Sanity check for AGCRestartTables."""
        print(f"Initial: PHASE={self.memory['PHASE']}, RESTART_ADDR={self.memory['RESTART_ADDR']}")
        # Lookup restart address for phase 2
        addr = self.lookup_restart(2)
        print(f"Phase 2 Restart: PHASE={self.memory['PHASE']}, RESTART_ADDR={addr}")

if __name__ == "__main__":
    restart_tables = AGCRestartTables()
    restart_tables.main()