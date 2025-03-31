# agc_radar_leadin_routines.py
from agc_utils import mask_15bit, store_to_memory

class AGCRadarLeadinRoutines:
    def __init__(self):
        self.memory = {
            "RADAR_RANGE": 0,   # Radar range (meters, scaled)
            "RADAR_VEL": 0      # Radar velocity (m/s, scaled)
        }

    def update_radar(self, range_val, velocity):
        """Simulate radar lead-in data update."""
        store_to_memory("RADAR_RANGE", mask_15bit(range_val), self.memory)
        store_to_memory("RADAR_VEL", mask_15bit(velocity), self.memory)
        return self.memory["RADAR_RANGE"], self.memory["RADAR_VEL"]

    def main(self):
        """Sanity check for AGCRadarLeadinRoutines."""
        print(f"Initial: RADAR_RANGE={self.memory['RADAR_RANGE']}, RADAR_VEL={self.memory['RADAR_VEL']}")
        range_val, vel = self.update_radar(5000, 100)
        print(f"Radar Update: RADAR_RANGE={range_val}, RADAR_VEL={vel}")

if __name__ == "__main__":
    radar = AGCRadarLeadinRoutines()
    radar.main()