# agc_lunar_landmark.py
from agc_utils import mask_15bit, store_to_memory

class AGCLunarLandmark:
    def __init__(self):
        self.memory = {
            "LANDID": 0,    # Landmark ID
            "LAT": 0        # Latitude (degrees, scaled)
        }
        # Simplified landmark table: {ID: latitude}
        self.landmark_table = {1: 10, 2: 20, 3: 30}

    def get_landmark(self, land_id):
        """Retrieve latitude for a lunar landmark."""
        store_to_memory("LANDID", mask_15bit(land_id), self.memory)
        latitude = self.landmark_table.get(land_id, 0)
        store_to_memory("LAT", mask_15bit(latitude), self.memory)
        return self.memory["LAT"]

    def main(self):
        """Sanity check for AGCLunarLandmark."""
        print(f"Initial: LANDID={self.memory['LANDID']}, LAT={self.memory['LAT']}")
        lat = self.get_landmark(2)
        print(f"Landmark 2: LANDID={self.memory['LANDID']}, LAT={lat}")

if __name__ == "__main__":
    lunar_landmark = AGCLunarLandmark()
    lunar_landmark.main()