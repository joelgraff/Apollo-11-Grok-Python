# agc_orbital_140.py
from agc_utils import mask_15bit, store_to_memory

class AGCOrbital140:
    def __init__(self):
        self.memory = {
            "POS": 0,       # Position (meters, scaled)
            "VEL": 0,       # Velocity (m/s, scaled)
            "DELTAT": 0     # Time step (centiseconds)
        }

    def integrate_step(self, velocity, delta_t):
        """Simulate orbital integration step: Update position."""
        store_to_memory("VEL", mask_15bit(velocity), self.memory)
        store_to_memory("DELTAT", mask_15bit(delta_t), self.memory)
        # Position update: pos += vel * dt (dt in seconds)
        pos_update = mask_15bit(self.memory["POS"] + (velocity * delta_t // 100))
        store_to_memory("POS", pos_update, self.memory)
        return self.memory["POS"]

    def main(self):
        """Sanity check for AGCOrbital140."""
        print(f"Initial: POS={self.memory['POS']}, VEL={self.memory['VEL']}, DELTAT={self.memory['DELTAT']}")
        pos = self.integrate_step(100, 200)  # 100 m/s, 2 seconds
        print(f"Integration: POS={pos}, VEL={self.memory['VEL']}, DELTAT={self.memory['DELTAT']}")

if __name__ == "__main__":
    orbital_140 = AGCOrbital140()
    orbital_140.main()