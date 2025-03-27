# agc_radar_leadin.py
from agc_utils import mask_15bit, store_to_memory

class AGCRadarLeadin:
    def __init__(self):
        self.memory = {
            "RANGERATE": 0,  # Radar range rate (m/s, scaled)
            "INITFLAG": 0    # Initialization flag (0=not set, 1=set)
        }

    def radar_init(self, range_rate):
        """Simulate radar lead-in: Set initial range rate."""
        store_to_memory("RANGERATE", mask_15bit(range_rate), self.memory)
        store_to_memory("INITFLAG", 1, self.memory)
        return self.memory["RANGERATE"]

    def main(self):
        """Sanity check for AGCRadarLeadin."""
        print(f"Initial: RANGERATE={self.memory['RANGERATE']}, INITFLAG={self.memory['INITFLAG']}")
        rate = self.radar_init(20)  # 20 m/s range rate
        print(f"Radar Init: RANGERATE={rate}, INITFLAG={self.memory['INITFLAG']}")

if __name__ == "__main__":
    radar_leadin = AGCRadarLeadin()
    radar_leadin.main()