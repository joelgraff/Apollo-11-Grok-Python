# agc_integration_init.py
from agc_utils import mask_15bit, store_to_memory

class AGCIntegrationInit:
    def __init__(self):
        self.memory = {
            "R_HIGH": 0,      # Position high word (meters)
            "R_LOW": 0,       # Position low word (meters)
            "V_HIGH": 0,      # Velocity high word (m/s)
            "V_LOW": 0,       # Velocity low word (m/s)
            "TIME": 0         # Integration start time (seconds)
        }

    def init_orbit(self, radius, velocity, start_time):
        """Initialize state vector for orbital integration."""
        # Set position (simplified 1D radius)
        store_to_memory("R_HIGH", mask_15bit(radius >> 15), self.memory)  # High 15 bits
        store_to_memory("R_LOW", mask_15bit(radius & 0x7FFF), self.memory)  # Low 15 bits

        # Set velocity (circular orbit, simplified)
        store_to_memory("V_HIGH", mask_15bit(velocity >> 15), self.memory)
        store_to_memory("V_LOW", mask_15bit(velocity & 0x7FFF), self.memory)

        # Set start time
        store_to_memory("TIME", mask_15bit(start_time), self.memory)

        return (self.memory["R_HIGH"], self.memory["R_LOW"]), (self.memory["V_HIGH"], self.memory["V_LOW"])

    def main(self):
        """Sanity check for AGCIntegrationInit."""
        print(f"Initial: R=({self.memory['R_HIGH']}, {self.memory['R_LOW']}), V=({self.memory['V_HIGH']}, {self.memory['V_LOW']}), TIME={self.memory['TIME']}")
        # Initialize orbit: 1737400m radius (lunar radius), 1630 m/s (approx lunar orbit speed), t=0
        r, v = self.init_orbit(1737400, 1630, 0)
        print(f"Initialized: R={r}, V={v}, TIME={self.memory['TIME']}")

if __name__ == "__main__":
    integration_init = AGCIntegrationInit()
    integration_init.main()