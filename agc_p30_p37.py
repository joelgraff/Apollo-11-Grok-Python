# agc_p30_p37.py
from agc_utils import mask_15bit, store_to_memory, double_precision_add

class AGCP30P37:
    def __init__(self):
        self.memory = {
            "VEL_CURRENT": (0, 100),  # Current velocity (m/s, double precision)
            "VEL_TARGET": (0, 150),   # Target velocity (m/s, double precision)
            "DELTAV": (0, 0),         # Delta-V for maneuver (double precision)
            "TIG": 0                  # Time of ignition (seconds)
        }

    def p30_maneuver(self, tig):
        """Simulate P30: Calculate delta-V for a maneuver."""
        # Set ignition time
        store_to_memory("TIG", mask_15bit(tig), self.memory)

        # Calculate delta-V (target - current)
        curr_high, curr_low = self.memory["VEL_CURRENT"]
        targ_high, targ_low = self.memory["VEL_TARGET"]
        delta_high, delta_low = double_precision_add(targ_high, targ_low, -curr_low)
        if curr_low > targ_low:  # Adjust high word for borrow
            delta_high = mask_15bit(delta_high - 1)
        self.memory["DELTAV"] = (delta_high, delta_low)

        return self.memory["DELTAV"], self.memory["TIG"]

    def main(self):
        """Sanity check for AGCP30P37."""
        print(f"Initial: VEL_CURRENT={self.memory['VEL_CURRENT']}, VEL_TARGET={self.memory['VEL_TARGET']}, TIG={self.memory['TIG']}")
        # Calculate maneuver at t=300s
        deltav, tig = self.p30_maneuver(300)
        print(f"P30 Maneuver: DELTAV={deltav}, TIG={tig}")

if __name__ == "__main__":
    p30_p37 = AGCP30P37()
    p30_p37.main()