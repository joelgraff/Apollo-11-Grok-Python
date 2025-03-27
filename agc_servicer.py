# agc_servicer.py
from agc_utils import (
    mask_15bit, store_to_memory, fetch_double_precision,
    double_precision_add, double_precision_subtract,
    double_precision_multiply
)

class AGCServicer:
    def __init__(self):
        self.memory = {
            "ACCX": (0, 0),  # X-axis acceleration (double-precision)
            "VELX": (0, 0),  # X-axis velocity
            "THRUST": 0      # Thrust command
        }

    def read_accs(self, acc_high, acc_low):
        """Simulate reading accelerometers."""
        self.memory["ACCX"] = (mask_15bit(acc_high), mask_15bit(acc_low))
        return self.memory["ACCX"]

    def update_velocity(self, dt):
        """Update velocity based on acceleration and thrust."""
        acc_high, acc_low = self.memory["ACCX"]
        vel_high, vel_low = self.memory["VELX"]
        # Add acceleration * dt to velocity
        dv_high, dv_low = double_precision_multiply(acc_high, acc_low, dt)
        vel_high, vel_low = double_precision_add(vel_high, vel_low, dv_low)
        vel_high = mask_15bit(vel_high + dv_high)
        # Add thrust effect (simplified)
        thrust_effect = self.memory["THRUST"] // 10  # Arbitrary scaling
        vel_high, vel_low = double_precision_add(vel_high, vel_low, thrust_effect)
        self.memory["VELX"] = (vel_high, vel_low)
        return vel_high, vel_low

    def set_thrust(self, thrust):
        """Set thrust command."""
        store_to_memory("THRUST", thrust, self.memory)

    def main(self):
        """Sanity check for AGCServicer."""
        # Simulate accelerometer reading
        self.read_accs(0, 50)
        print(f"Initial ACCX: {self.memory['ACCX']}, VELX: {self.memory['VELX']}")
        # Set some thrust
        self.set_thrust(200)
        # Update velocity over 3 time units
        vel_high, vel_low = self.update_velocity(3)
        print(f"Updated VELX with thrust: {vel_high}, {vel_low}")

if __name__ == "__main__":
    servicer = AGCServicer()
    servicer.main()