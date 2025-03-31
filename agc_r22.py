# agc_r22.py
from agc_utils import mask_15bit, store_to_memory

class AGCR22:
    def __init__(self):
        self.memory = {
            "R22_RANGE": 0,   # Radar range (meters, scaled)
            "R22_VEL": 0      # Radar velocity (m/s, scaled)
        }

    def process_r22(self, range_val, velocity):
        """Simulate R22 rendezvous radar processing."""
        store_to_memory("R22_RANGE", mask_15bit(range_val), self.memory)
        store_to_memory("R22_VEL", mask_15bit(velocity), self.memory)
        return self.memory["R22_RANGE"], self.memory["R22_VEL"]

    def main(self):
        """Sanity check for AGCR22."""
        print(f"Initial: R22_RANGE={self.memory['R22_RANGE']}, R22_VEL={self.memory['R22_VEL']}")
        range_val, vel = self.process_r22(5000, 100)
        print(f"R22 Processed: R22_RANGE={range_val}, R22_VEL={vel}")

if __name__ == "__main__":
    r22 = AGCR22()
    r22.main()