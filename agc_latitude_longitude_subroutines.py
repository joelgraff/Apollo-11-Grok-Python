# agc_latitude_longitude_subroutines.py
from agc_utils import mask_15bit, store_to_memory

class AGCLatitudeLongitudeSubroutines:
    def __init__(self):
        self.memory = {
            "LAT": 0,    # Latitude (degrees, scaled)
            "LON": 0     # Longitude (degrees, scaled)
        }

    def set_lat_lon(self, lat, lon):
        """Simulate setting latitude and longitude."""
        store_to_memory("LAT", mask_15bit(lat), self.memory)
        store_to_memory("LON", mask_15bit(lon), self.memory)
        return self.memory["LAT"], self.memory["LON"]

    def main(self):
        """Sanity check for AGCLatitudeLongitudeSubroutines."""
        print(f"Initial: LAT={self.memory['LAT']}, LON={self.memory['LON']}")
        lat, lon = self.set_lat_lon(30, 45)
        print(f"Lat/Lon Set: LAT={lat}, LON={lon}")

if __name__ == "__main__":
    lat_lon = AGCLatitudeLongitudeSubroutines()
    lat_lon.main()