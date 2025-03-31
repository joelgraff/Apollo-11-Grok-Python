# agc_phase_table_maintenance.py
from agc_utils import mask_15bit, store_to_memory

class AGCPhaseTableMaintenance:
    def __init__(self):
        self.memory = {
            "PHASE_NUM": 0,   # Phase number
            "PHASE_STATE": 0  # Phase state (0=inactive, 1=active)
        }

    def update_phase(self, phase, state):
        """Simulate phase table update."""
        store_to_memory("PHASE_NUM", mask_15bit(phase), self.memory)
        store_to_memory("PHASE_STATE", mask_15bit(state), self.memory)
        return self.memory["PHASE_NUM"], self.memory["PHASE_STATE"]

    def main(self):
        """Sanity check for AGCPhaseTableMaintenance."""
        print(f"Initial: PHASE_NUM={self.memory['PHASE_NUM']}, PHASE_STATE={self.memory['PHASE_STATE']}")
        phase, state = self.update_phase(3, 1)  # Phase 3, active
        print(f"Phase Update: PHASE_NUM={phase}, PHASE_STATE={state}")

if __name__ == "__main__":
    phase_table = AGCPhaseTableMaintenance()
    phase_table.main()