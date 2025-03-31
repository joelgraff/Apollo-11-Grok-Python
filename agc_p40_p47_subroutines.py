# agc_p40_p47_subroutines.py
from agc_utils import mask_15bit, store_to_memory

class AGCP40P47Subroutines:
    def __init__(self):
        self.memory = {
            "DELTAV": 0,     # Delta-V required (m/s, scaled)
            "THRUST": 0,     # Thrust (N)
            "DUR": 0         # Thrust duration (centiseconds)
        }

    def calc_thrust_dur(self, deltav, thrust, mass=5000):
        """Simulate thrust duration calculation."""
        store_to_memory("DELTAV", mask_15bit(deltav), self.memory)
        store_to_memory("THRUST", mask_15bit(thrust), self.memory)
        # Simplified: t = (m * dv) / F, scaled to centiseconds
        duration = mask_15bit((mass * deltav * 100) // thrust)
        store_to_memory("DUR", duration, self.memory)
        return duration

    def main(self):
        """Sanity check for AGCP40P47Subroutines."""
        print(f"Initial: DELTAV={self.memory['DELTAV']}, THRUST={self.memory['THRUST']}, DUR={self.memory['DUR']}")
        dur = self.calc_thrust_dur(100, 1000)  # 100 m/s, 1000N
        print(f"Thrust Dur: DELTAV={self.memory['DELTAV']}, THRUST={self.memory['THRUST']}, DUR={dur}")

if __name__ == "__main__":
    p40_p47_subroutines = AGCP40P47Subroutines()
    p40_p47_subroutines.main()