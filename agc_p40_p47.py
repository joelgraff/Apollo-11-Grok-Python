# agc_p40_p47.py
from agc_utils import mask_15bit, store_to_memory, double_precision_add

class AGCP40P47:
    def __init__(self):
        self.memory = {
            "DELTAV": (0, 50),   # Required delta-V (m/s, double precision)
            "THRUST": 0,         # Thrust in N (simplified)
            "MASSC": 5000,       # Current mass in kg
            "TIG": 0,            # Time of ignition (seconds)
            "BURNTIME": 0        # Calculated burn time (seconds)
        }

    def p40_burn(self, tig, thrust):
        """Simulate P40: Calculate burn time for DPS maneuver."""
        # Set ignition time and thrust
        store_to_memory("TIG", mask_15bit(tig), self.memory)
        store_to_memory("THRUST", mask_15bit(thrust), self.memory)

        # Calculate burn time: delta-V = (thrust / mass) * time => time = (delta-V * mass) / thrust
        dv_high, dv_low = self.memory["DELTAV"]
        mass = self.memory["MASSC"]
        delta_v = dv_low  # Simplified to low word for single precision calc
        accel = thrust / mass  # Acceleration in m/s^2
        burn_time = mask_15bit(int(delta_v / accel))  # Time in seconds
        store_to_memory("BURNTIME", burn_time, self.memory)

        return self.memory["TIG"], burn_time

    def main(self):
        """Sanity check for AGCP40P47."""
        print(f"Initial: DELTAV={self.memory['DELTAV']}, MASSC={self.memory['MASSC']}, TIG={self.memory['TIG']}")
        # Run P40 with 1000N thrust at t=500s
        tig, burn_time = self.p40_burn(500, 1000)
        print(f"P40 Burn: TIG={tig}, BURNTIME={burn_time}, THRUST={self.memory['THRUST']}")

if __name__ == "__main__":
    p40_p47 = AGCP40P47()
    p40_p47.main()