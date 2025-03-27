# agc_phasetable.py
from agc_utils import mask_15bit, store_to_memory

class AGCPhaseTable:
    def __init__(self):
        self.memory = {
            "PHASE1": 0,    # Phase for Program 1
            "PHASE2": 0,    # Phase for Program 2
            "ACTIVE": 0     # Currently active phase
        }

    def update_phase(self, phase_num, value):
        """Update a phase table entry."""
        if phase_num == 1:
            store_to_memory("PHASE1", value, self.memory)
        elif phase_num == 2:
            store_to_memory("PHASE2", value, self.memory)
        else:
            return False
        return True

    def set_active_phase(self, phase_num):
        """Set the active phase for restart tracking."""
        if phase_num in [1, 2]:
            store_to_memory("ACTIVE", phase_num, self.memory)
            return True
        return False

    def get_phase(self, phase_num):
        """Retrieve a phase value."""
        if phase_num == 1:
            return self.memory["PHASE1"]
        elif phase_num == 2:
            return self.memory["PHASE2"]
        return None

    def main(self):
        """Sanity check for AGCPhaseTable."""
        # Update phases
        self.update_phase(1, 10)  # Program 1 in phase 10
        self.update_phase(2, 20)  # Program 2 in phase 20
        print(f"Phases Set: PHASE1={self.memory['PHASE1']}, PHASE2={self.memory['PHASE2']}")
        # Set active phase
        self.set_active_phase(1)
        print(f"Active Phase: ACTIVE={self.memory['ACTIVE']}")
        # Retrieve and verify
        phase1 = self.get_phase(1)
        phase2 = self.get_phase(2)
        print(f"Retrieved: PHASE1={phase1}, PHASE2={phase2}")

if __name__ == "__main__":
    phasetable = AGCPhaseTable()
    phasetable.main()