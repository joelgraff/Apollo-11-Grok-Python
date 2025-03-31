# agc_lunar_landmark_selection_for_lm.py
from agc_utils import mask_15bit, store_to_memory

class AGCLunarLandmarkSelectionForLM:
    def __init__(self):
        self.memory = {
            "LANDMARK_ID": 0,   # Landmark identifier
            "LANDMARK_POS": 0   # Landmark position (scaled)
        }

    def select_landmark(self, landmark, pos):
        """Simulate lunar landmark selection."""
        store_to_memory("LANDMARK_ID", mask_15bit(landmark), self.memory)
        store_to_memory("LANDMARK_POS", mask_15bit(pos), self.memory)
        return self.memory["LANDMARK_ID"], self.memory["LANDMARK_POS"]

    def main(self):
        """Sanity check for AGCLunarLandmarkSelectionForLM."""
        print(f"Initial: LANDMARK_ID={self.memory['LANDMARK_ID']}, LANDMARK_POS={self.memory['LANDMARK_POS']}")
        lid, pos = self.select_landmark(1, 500)
        print(f"Landmark Selected: LANDMARK_ID={lid}, LANDMARK_POS={pos}")

if __name__ == "__main__":
    landmark = AGCLunarLandmarkSelectionForLM()
    landmark.main()