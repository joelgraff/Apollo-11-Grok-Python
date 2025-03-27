# agc_p60_p67.py
from agc_utils import mask_15bit, store_to_memory, double_precision_subtract

class AGCP60P67:
    def __init__(self):
        self.memory = {
            "VEL": (0, 500),    # Current velocity (m/s, double precision)
            "THRUST": 0,        # Thrust in N
            "MASSC": 5000,      # Current mass in kg
            "TIG": 0,           # Time of ignition (seconds)
            "DELTAT": 0         # Time to reduce velocity (seconds)
        }

    def p63_braking(self, tig, thrust, target_vel_low):
        """Simulate P63: Braking phase to reduce velocity."""
        # Set ignition time and thrust
        store_to_memory("TIG", mask_15bit(tig), self.memory)
        store_to_memory("THRUST", mask_15bit(thrust), self.memory)

        # Calculate deceleration: a = thrust / mass
        accel = thrust / self.memory["MASSC"]  # m/s^2
        vel_high, vel_low = self.memory["VEL"]
        delta_v = vel_low - target_vel_low  # Desired velocity reduction
        delta_t = mask_15bit(int(delta_v / accel))  # Time in seconds
        store_to_memory("DELTAT", delta_t, self.memory)

        # Update velocity (simplified subtraction)
        new_vel_high, new_vel_low = double_precision_subtract(vel_high, vel_low, delta_v)
        self.memory["VEL"] = (new_vel_high, new_vel_low)

        return self.memory["VEL"], delta_t

    def main(self):
        """Sanity check for AGCP60P67."""
        print(f"Initial: VEL={self.memory['VEL']}, TIG={self.memory['TIG']}")
        # Run P63 with 1000N thrust to reduce velocity to 400 m/s at t=600s
        new_vel, delta_t = self.p63_braking(600, 1000, 400)
        print(f"P63 Braking: VEL={new_vel}, DELTAT={delta_t}, THRUST={self.memory['THRUST']}")

if __name__ == "__main__":
    p60_p67 = AGCP60P67()
    p60_p67.main()