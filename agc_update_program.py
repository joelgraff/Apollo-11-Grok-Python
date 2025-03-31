# agc_update_program.py
from agc_utils import mask_15bit, store_to_memory

class AGCUpdateProgram:
    def __init__(self):
        self.memory = {
            "POS": 0,    # Position (meters, scaled)
            "VEL": 0     # Velocity (m/s, scaled)
        }

    def update_state(self, pos_delta, vel_delta):
        """Update state vector with deltas."""
        current_pos = self.memory["POS"]
        current_vel = self.memory["VEL"]
        new_pos = mask_15bit(current_pos + pos_delta)
        new_vel = mask_15bit(current_vel + vel_delta)
        store_to_memory("POS", new_pos, self.memory)
        store_to_memory("VEL", new_vel, self.memory)
        return new_pos, new_vel

    def main(self):
        """Sanity check for AGCUpdateProgram."""
        print(f"Initial: POS={self.memory['POS']}, VEL={self.memory['VEL']}")
        pos, vel = self.update_state(1000, 50)
        print(f"Updated: POS={pos}, VEL={vel}")

if __name__ == "__main__":
    update_program = AGCUpdateProgram()
    update_program.main()
