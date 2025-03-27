# agc_groundtrack.py
from agc_utils import mask_15bit, store_to_memory, double_precision_add

class AGCGroundTrack:
    def __init__(self):
        self.memory = {
            "LAT": (0, 0),    # Latitude (double precision)
            "LON": (0, 0),    # Longitude (double precision)
            "VEL": (0, 10),   # Velocity in deg/sec (simplified)
            "TIME": 0         # Time in seconds
        }

    def update_position(self, delta_time):
        """Update ground track position based on time and velocity."""
        # Increment time
        current_time = self.memory["TIME"]
        new_time = mask_15bit(current_time + delta_time)
        store_to_memory("TIME", new_time, self.memory)

        # Update longitude (assuming constant velocity eastward)
        vel_high, vel_low = self.memory["VEL"]
        lon_high, lon_low = self.memory["LON"]
        # Multiply velocity by delta_time (simplified to single step)
        delta_lon_high, delta_lon_low = 0, mask_15bit(vel_low * delta_time)
        new_lon_high, new_lon_low = double_precision_add(lon_high, lon_low, delta_lon_low)
        self.memory["LON"] = (new_lon_high, new_lon_low)

        # Latitude remains constant for simplicity
        self.memory["LAT"] = (0, 0)
        return self.memory["LAT"], self.memory["LON"]

    def main(self):
        """Sanity check for AGCGroundTrack."""
        print(f"Initial: LAT={self.memory['LAT']}, LON={self.memory['LON']}, TIME={self.memory['TIME']}")
        # Update position after 5 seconds
        lat, lon = self.update_position(5)
        print(f"After 5s: LAT={lat}, LON={lon}, TIME={self.memory['TIME']}")

if __name__ == "__main__":
    groundtrack = AGCGroundTrack()
    groundtrack.main()