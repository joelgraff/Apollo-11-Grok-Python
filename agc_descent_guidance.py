# agc_descent_guidance.py
from agc_utils import mask_15bit, store_to_memory

class AGCDescentGuidance:
    def __init__(self):
        self.memory = {
            "VEL": 0,       # Vertical velocity (m/s, scaled)
            "THRUST": 0,    # Thrust command (N)
            "MASSC": 5000   # Mass (kg)
        }

    def descent_adjust(self, velocity, thrust):
        """Simulate descent guidance: Adjust velocity with thrust."""
        store_to_memory("VEL", mask_15bit(velocity), self.memory)
        store_to_memory("THRUST", mask_15bit(thrust), self.memory)
        # Simplified: dv = (thrust / mass) * dt (dt=1s)
        dv = thrust // self.memory["MASSC"]
        new_vel = mask_15bit(velocity - dv)
        store_to_memory("VEL", new_vel, self.memory)
        return new_vel

    def main(self):
        """Sanity check for AGCDescentGuidance."""
        print(f"Initial: VEL={self.memory['VEL']}, THRUST={self.memory['THRUST']}, MASSC={self.memory['MASSC']}")
        vel = self.descent_adjust(100, 1000)  # 100 m/s, 1000N thrust
        print(f"Descent: VEL={vel}, THRUST={self.memory['THRUST']}")

if __name__ == "__main__":
    descent_guidance = AGCDescentGuidance()
    descent_guidance.main()