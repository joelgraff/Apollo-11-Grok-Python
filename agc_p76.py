# agc_p76.py
from agc_utils import mask_15bit, store_to_memory

class AGCP76:
    def __init__(self):
        self.memory = {
            "VEL": 0,       # Current velocity (m/s, scaled)
            "CORR": 0,      # Velocity correction (m/s)
            "NEWVEL": 0     # Updated velocity
        }

    def update_state(self, velocity, correction):
        """Simulate P76: Update velocity with correction."""
        store_to_memory("VEL", mask_15bit(velocity), self.memory)
        store_to_memory("CORR", mask_15bit(correction), self.memory)
        new_vel = mask_15bit(velocity + correction)
        store_to_memory("NEWVEL", new_vel, self.memory)
        return new_vel

    def main(self):
        """Sanity check for AGCP76."""
        print(f"Initial: VEL={self.memory['VEL']}, CORR={self.memory['CORR']}, NEWVEL={self.memory['NEWVEL']}")
        vel = self.update_state(500, 50)  # 500 m/s + 50 m/s correction
        print(f"P76 Update: VEL={self.memory['VEL']}, CORR={self.memory['CORR']}, NEWVEL={vel}")

if __name__ == "__main__":
    p76 = AGCP76()
    p76.main()