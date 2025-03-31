# agc_tvcstroketest.py
from agc_utils import mask_15bit, store_to_memory

class AGCTVCStrokeTest:
    def __init__(self):
        self.memory = {
            "STROKE": 0,    # Stroke position (scaled)
            "TESTRES": 0    # Test result (0=fail, 1=pass)
        }

    def run_stroke_test(self, stroke_val):
        """Run TVC stroke test."""
        store_to_memory("STROKE", mask_15bit(stroke_val), self.memory)
        result = 1 if stroke_val > 0 else 0  # Simplified pass condition
        store_to_memory("TESTRES", result, self.memory)
        return result

    def main(self):
        """Sanity check for AGCTVCStrokeTest."""
        print(f"Initial: STROKE={self.memory['STROKE']}, TESTRES={self.memory['TESTRES']}")
        test_result = self.run_stroke_test(25)
        print(f"Stroke Test: STROKE={self.memory['STROKE']}, TESTRES={test_result}")

if __name__ == "__main__":
    tvc_stroke = AGCTVCStrokeTest()
    tvc_stroke.main()