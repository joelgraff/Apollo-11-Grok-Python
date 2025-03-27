# agc_p20_p25.py
from agc_utils import mask_15bit, store_to_memory, double_precision_add

class AGCP20P25:
    def __init__(self):
        self.memory = {
            "LAT": (0, 0),     # Latitude (double precision)
            "LON": (0, 0),     # Longitude (double precision)
            "VEL": (0, 10),    # Velocity in deg/sec (double precision)
            "TIME": 0,         # Mission time in seconds
            "DISPREG": 0       # DSKY display register
        }

    def p20_update(self, delta_time):
        """Simulate P20: Update position and prepare DSKY display."""
        # Update time
        current_time = self.memory["TIME"]
        new_time = mask_15bit(current_time + delta_time)
        store_to_memory("TIME", new_time, self.memory)

        # Update longitude (eastward motion)
        vel_high, vel_low = self.memory["VEL"]
        lon_high, lon_low = self.memory["LON"]
        delta_lon_high, delta_lon_low = 0, mask_15bit(vel_low * delta_time)
        new_lon_high, new_lon_low = double_precision_add(lon_high, lon_low, delta_lon_low)
        self.memory["LON"] = (new_lon_high, new_lon_low)

        # Display longitude on DSKY (simplified)
        disp_value = mask_15bit(new_lon_low)  # Use low word for display
        store_to_memory("DISPREG", disp_value, self.memory)
        return self.memory["LAT"], self.memory["LON"], disp_value

    def main(self):
        """Sanity check for AGCP20P25."""
        print(f"Initial: LAT={self.memory['LAT']}, LON={self.memory['LON']}, DISPREG={self.memory['DISPREG']}")
        # Run P20 for 10 seconds
        lat, lon, disp = self.p20_update(10)
        print(f"P20 (10s): LAT={lat}, LON={lon}, DISPREG={disp}")

if __name__ == "__main__":
    p20_p25 = AGCP20P25()
    p20_p25.main()