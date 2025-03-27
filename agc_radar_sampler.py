# agc_radar_sampler.py
from agc_utils import mask_15bit, store_to_memory

class AGCRadarSampler:
    def __init__(self):
        self.memory = {
            "RANGE": 0,     # Sampled range (meters, scaled)
            "SAMPTIME": 0   # Sample time (centiseconds)
        }

    def sample_radar(self, range_val, time):
        """Simulate radar sampling."""
        store_to_memory("RANGE", mask_15bit(range_val), self.memory)
        store_to_memory("SAMPTIME", mask_15bit(time), self.memory)
        return self.memory["RANGE"]

    def main(self):
        """Sanity check for AGCRadarSampler."""
        print(f"Initial: RANGE={self.memory['RANGE']}, SAMPTIME={self.memory['SAMPTIME']}")
        range_val = self.sample_radar(1000, 50)  # 1000m at 50cs
        print(f"Radar Sample: RANGE={range_val}, SAMPTIME={self.memory['SAMPTIME']}")

if __name__ == "__main__":
    radar_sampler = AGCRadarSampler()
    radar_sampler.main()