# agc_reentry.py
from agc_utils import (
    mask_15bit, store_to_memory, double_precision_add,
    double_precision_subtract, double_precision_multiply
)

class AGCReentry:
    def __init__(self):
        self.memory = {
            "ROLL": 0,      # Roll angle
            "LIFT": 0,      # Lift force
            "DRAG": 0,      # Drag force
            "VEL": 0        # Velocity
        }

    def set_conditions(self, roll, lift, drag, vel):
        """Set initial reentry conditions."""
        store_to_memory("ROLL", roll, self.memory)
        store_to_memory("LIFT", lift, self.memory)
        store_to_memory("DRAG", drag, self.memory)
        store_to_memory("VEL", vel, self.memory)

    def adjust_roll(self, target_roll):
        """Adjust roll to target value."""
        current_roll = self.memory["ROLL"]
        diff = double_precision_subtract(target_roll, 0, current_roll)[1]  # Simplified
        if diff > 0:
            roll_adjust = min(diff, 100)  # Max adjustment rate
        else:
            roll_adjust = max(diff, -100)
        new_roll = double_precision_add(current_roll, 0, roll_adjust)[1]
        store_to_memory("ROLL", new_roll, self.memory)
        return new_roll

    def update_velocity(self, dt):
        """Update velocity based on drag."""
        vel = self.memory["VEL"]
        drag = self.memory["DRAG"]
        vel_change = double_precision_multiply(0, drag, dt)[1]  # Simplified
        new_vel = double_precision_subtract(vel, 0, vel_change)[1]
        store_to_memory("VEL", new_vel, self.memory)
        return new_vel

    def main(self):
        """Sanity check for AGCReentry."""
        self.set_conditions(0, 500, 200, 10000)  # Initial values
        print(f"Initial: Roll={self.memory['ROLL']}, Vel={self.memory['VEL']}")
        # Adjust roll toward 300
        new_roll = self.adjust_roll(300)
        print(f"Adjusted Roll: {new_roll}")
        # Update velocity over 2 time units
        new_vel = self.update_velocity(2)
        print(f"Updated Velocity: {new_vel}")

if __name__ == "__main__":
    reentry = AGCReentry()
    reentry.main()