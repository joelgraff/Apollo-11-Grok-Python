# agc_cm_entry_and_return.py
from agc_utils import mask_15bit, store_to_memory

class AGCCMEntryAndReturn:
    def __init__(self):
        self.memory = {
            "VEL": 0,       # Velocity (m/s, scaled)
            "ALT": 0,       # Altitude (meters, scaled)
            "PHASE": 0      # Entry phase (0=pre-entry, 1=entry)
        }

    def entry_phase(self, velocity, altitude):
        """Simulate CM entry phase transition."""
        store_to_memory("VEL", mask_15bit(velocity), self.memory)
        store_to_memory("ALT", mask_15bit(altitude), self.memory)
        phase = 1 if altitude < 10000 else 0  # Simplified threshold
        store_to_memory("PHASE", phase, self.memory)
        return phase

    def main(self):
        """Sanity check for AGCCMEntryAndReturn."""
        print(f"Initial: VEL={self.memory['VEL']}, ALT={self.memory['ALT']}, PHASE={self.memory['PHASE']}")
        phase = self.entry_phase(8000, 5000)  # 8000 m/s, 5000m
        print(f"Entry: VEL={self.memory['VEL']}, ALT={self.memory['ALT']}, PHASE={phase}")

if __name__ == "__main__":
    entry = AGCCMEntryAndReturn()
    entry.main()