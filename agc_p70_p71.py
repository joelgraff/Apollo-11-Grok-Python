# agc_p70_p71.py
from agc_utils import mask_15bit, store_to_memory, double_precision_add

class AGCP70P71:
    def __init__(self):
        self.memory = {
            "DELTAV": (0, 100),  # Abort delta-V (m/s, double precision)
            "THRUST": 0,         # DPS thrust in N
            "MASSC": 4000,       # Current mass in kg (post-descent)
            "TIG": 0,            # Time of ignition (seconds)
            "BURNTIME": 0        # Calculated burn time (seconds)
        }

    def p70_abort(self, tig, thrust):
        """Simulate P70: DPS abort burn to reach orbit."""
        # Set ignition time and thrust
        store_to_memory("TIG", mask_15bit(tig), self.memory)
        store_to_memory("THRUST", mask_15bit(thrust), self.memory)

        # Calculate burn time: time = (delta-V * mass) / thrust
        dv_high, dv_low = self.memory["DELTAV"]
        mass = self.memory["MASSC"]
        delta_v = dv_low  # Simplified to low word
        accel = thrust / mass  # Acceleration in m/s^2
        burn_time = mask_15bit(int(delta_v / accel))  # Time in seconds
        store_to_memory("BURNTIME", burn_time, self.memory)

        return self.memory["TIG"], burn_time

    def main(self):
        """Sanity check for AGCP70P71."""
        print(f"Initial: DELTAV={self.memory['DELTAV']}, MASSC={self.memory['MASSC']}, TIG={self.memory['TIG']}")
        # Run P70 with 1500N thrust at t=700s
        tig, burn_time = self.p70_abort(700, 1500)
        print(f"P70 Abort: TIG={tig}, BURNTIME={burn_time}, THRUST={self.memory['THRUST']}")

if __name__ == "__main__":
    p70_p71 = AGCP70P71()
    p70_p71.main()