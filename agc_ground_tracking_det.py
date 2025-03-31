# agc_ground_tracking_det.py
from agc_utils import mask_15bit, store_to_memory

class AGCGroundTrackingDet:
    def __init__(self):
        self.memory = {
            "LONG": 0,       # Longitude (degrees, scaled)
            "VEL": 0,        # Velocity (m/s, scaled)
            "TIME": 0        # Time step (centiseconds)
        }

    def update_ground_track(self, longitude, velocity, time):
        """Simulate ground track update."""
        store_to_memory("LONG", mask_15bit(longitude), self.memory)
        store_to_memory("VEL", mask_15bit(velocity), self.memory)
        store_to_memory("TIME", mask_15bit(time), self.memory)
        # Simplified: dlong = (vel / R_earth) * dt (R_earth ~ 6378 km)
        dlong = (velocity * time // 100) // 6378000  # Rough scaling
        new_long = mask_15bit(longitude + dlong)
        store_to_memory("LONG", new_long, self.memory)
        return new_long

    def main(self):
        """Sanity check for AGCGroundTrackingDet."""
        print(f"Initial: LONG={self.memory['LONG']}, VEL={self.memory['VEL']}, TIME={self.memory['TIME']}")
        long = self.update_ground_track(0, 1000, 100)  # 0 deg, 1000 m/s, 1s
        print(f"Ground Track: LONG={long}, VEL={self.memory['VEL']}, TIME={self.memory['TIME']}")

if __name__ == "__main__":
    ground_tracking_det = AGCGroundTrackingDet()
    ground_tracking_det.main()