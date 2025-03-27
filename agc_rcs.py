# agc_rcs.py
from agc_utils import (
    mask_15bit, store_to_memory, double_precision_add,
    double_precision_subtract, double_precision_multiply
)

class AGCRCS:
    def __init__(self):
        self.memory = {
            "ROLL": 0,       # Current roll angle
            "ROLLCMD": 0,    # Desired roll angle
            "THRUST": 0      # Thruster command (positive/negative for direction)
        }

    def set_attitude(self, roll, roll_cmd):
        """Set current and commanded roll angles."""
        store_to_memory("ROLL", roll, self.memory)
        store_to_memory("ROLLCMD", roll_cmd, self.memory)

    def compute_error(self):
        """Calculate roll error."""
        roll = self.memory["ROLL"]
        roll_cmd = self.memory["ROLLCMD"]
        error_high, error_low = double_precision_subtract(roll_cmd, 0, roll)
        return error_low  # Simplified to low word for demo

    def fire_thrusters(self, error):
        """Compute thruster command based on error."""
        # Simple proportional control: thrust = K * error
        K = 2  # Proportional gain (arbitrary)
        thrust_high, thrust = double_precision_multiply(0, error, K)
        thrust = mask_15bit(thrust) if error >= 0 else -mask_15bit(thrust)
        store_to_memory("THRUST", thrust, self.memory)
        # Update roll based on thrust (simplified dynamics)
        roll_change = thrust // 10  # Arbitrary scaling
        new_roll = double_precision_add(self.memory["ROLL"], 0, roll_change)[1]
        store_to_memory("ROLL", new_roll, self.memory)
        return thrust, new_roll

    def main(self):
        """Sanity check for AGCRCS."""
        self.set_attitude(50, 100)  # Current roll 50, target 100
        print(f"Initial: Roll={self.memory['ROLL']}, RollCmd={self.memory['ROLLCMD']}")
        error = self.compute_error()
        print(f"Roll Error: {error}")
        thrust, new_roll = self.fire_thrusters(error)
        print(f"Thrust: {thrust}, New Roll: {new_roll}")

if __name__ == "__main__":
    rcs = AGCRCS()
    rcs.main()