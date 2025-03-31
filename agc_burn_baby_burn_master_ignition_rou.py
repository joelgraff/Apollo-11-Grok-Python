# agc_burn_baby_burn_master_ignition_routine.py
from agc_utils import mask_15bit, store_to_memory

class AGCBurnBabyBurnMasterIgnitionRoutine:
    def __init__(self):
        self.memory = {
            "TIG": 0,       # Time of ignition (seconds, scaled)
            "THRUST": 0,    # Thrust level (N, scaled)
            "IGNITION": 0   # Ignition status (0=off, 1=on)
        }

    def ignite(self, tig, thrust):
        """Simulate master ignition routine."""
        store_to_memory("TIG", mask_15bit(tig), self.memory)
        store_to_memory("THRUST", mask_15bit(thrust), self.memory)
        store_to_memory("IGNITION", 1, self.memory)
        return self.memory["IGNITION"]

    def main(self):
        """Sanity check for AGCBurnBabyBurnMasterIgnitionRoutine."""
        print(f"Initial: TIG={self.memory['TIG']}, THRUST={self.memory['THRUST']}, IGNITION={self.memory['IGNITION']}")
        status = self.ignite(300, 5000)  # Ignite at 300s with 5000N
        print(f"Ignition: TIG={self.memory['TIG']}, THRUST={self.memory['THRUST']}, IGNITION={status}")

if __name__ == "__main__":
    burn = AGCBurnBabyBurnMasterIgnitionRoutine()
    burn.main()