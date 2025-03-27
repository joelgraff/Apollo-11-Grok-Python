# agc_servicer206.py
from agc_utils import mask_15bit, store_to_memory

class AGCServicer206:
    def __init__(self):
        self.memory = {
            "POS": 0,       # Position (meters, scaled)
            "VEL": 0,       # Velocity (m/s, scaled)
            "SERVTIME": 0   # Service time (centiseconds)
        }

    def service_update(self, position, velocity, time):
        """Simulate servicer update: Adjust position."""
        store_to_memory("POS", mask_15bit(position), self.memory)
        store_to_memory("VEL", mask_15bit(velocity), self.memory)
        store_to_memory("SERVTIME", mask_15bit(time), self.memory)
        new_pos = mask_15bit(position + (velocity * time // 100))
        store_to_memory("POS", new_pos, self.memory)
        return new_pos

    def main(self):
        """Sanity check for AGCServicer206."""
        print(f"Initial: POS={self.memory['POS']}, VEL={self.memory['VEL']}, SERVTIME={self.memory['SERVTIME']}")
        pos = self.service_update(1000, 50, 200)  # 1000m, 50 m/s, 2s
        print(f"Service Update: POS={pos}, VEL={self.memory['VEL']}, SERVTIME={self.memory['SERVTIME']}")

if __name__ == "__main__":
    servicer206 = AGCServicer206()
    servicer206.main()