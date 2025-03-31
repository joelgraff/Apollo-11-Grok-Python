# agc_ground_tracking_determination_program.py
from agc_utils import mask_15bit, store_to_memory

class AGCGroundTrackingDeterminationProgram:
    def __init__(self):
        self.memory = {
            "TRACK_ALT": 0,   # Altitude for tracking (meters, scaled)
            "TRACK_POS": 0    # Position update (scaled)
        }

    def update_tracking(self, altitude):
        """Simulate ground tracking determination."""
        store_to_memory("TRACK_ALT", mask_15bit(altitude), self.memory)
        pos = mask_15bit(altitude // 2)  # Simplified position calc
        store_to_memory("TRACK_POS", pos, self.memory)
        return pos

    def main(self):
        """Sanity check for AGCGroundTrackingDeterminationProgram."""
        print(f"Initial: TRACK_ALT={self.memory['TRACK_ALT']}, TRACK_POS={self.memory['TRACK_POS']}")
        pos = self.update_tracking(1000)
        print(f"Tracking: TRACK_ALT={self.memory['TRACK_ALT']}, TRACK_POS={pos}")

if __name__ == "__main__":
    ground_track = AGCGroundTrackingDeterminationProgram()
    ground_track.main()