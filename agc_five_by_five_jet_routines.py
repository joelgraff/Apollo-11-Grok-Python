# agc_five_by_five_jet_routines.py
from agc_utils import mask_15bit, store_to_memory

class AGCFiveByFiveJetRoutines:
    def __init__(self):
        self.memory = {
            "JET_CMD": 0,    # Jet command bitfield (5x5 jets)
            "JET_STATE": 0   # Jet firing state (0=off, 1=on)
        }

    def fire_jets(self, jet_pattern):
        """Simulate firing 5x5 jet configuration."""
        store_to_memory("JET_CMD", mask_15bit(jet_pattern), self.memory)
        store_to_memory("JET_STATE", 1, self.memory)
        return self.memory["JET_CMD"]

    def main(self):
        """Sanity check for AGCFiveByFiveJetRoutines."""
        print(f"Initial: JET_CMD={self.memory['JET_CMD']}, JET_STATE={self.memory['JET_STATE']}")
        cmd = self.fire_jets(0x001F)  # Fire first 5 jets
        print(f"Jet Firing: JET_CMD={cmd}, JET_STATE={self.memory['JET_STATE']}")

if __name__ == "__main__":
    jets = AGCFiveByFiveJetRoutines()
    jets.main()