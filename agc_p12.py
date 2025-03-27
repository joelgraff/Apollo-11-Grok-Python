# agc_p12.py
from agc_utils import mask_15bit, store_to_memory

class AGCP12:
    def __init__(self):
        self.memory = {
            "ALT": 0,       # Altitude (meters, scaled)
            "THRUST": 0,    # Thrust command (N)
            "MASSC": 5000   # Mass (kg)
        }

    def ascent_guidance(self, altitude):
        """Simulate P12 ascent guidance: Set thrust based on altitude."""
        store_to_memory("ALT", mask_15bit(altitude), self.memory)
        # Simplified: thrust increases with altitude (arbitrary scaling)
        thrust = mask_15bit(1000 + (altitude // 10))
        store_to_memory("THRUST", thrust, self.memory)
        return thrust

    def main(self):
        """Sanity check for AGCP12."""
        print(f"Initial: ALT={self.memory['ALT']}, THRUST={self.memory['THRUST']}, MASSC={self.memory['MASSC']}")
        thrust = self.ascent_guidance(500)  # 500m altitude
        print(f"Ascent: ALT={self.memory['ALT']}, THRUST={thrust}")

if __name__ == "__main__":
    p12 = AGCP12()
    p12.main()