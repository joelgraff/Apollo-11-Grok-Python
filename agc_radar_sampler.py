# agc_radar_sampler.py
import time
from agc_utils import mask_15bit, store_to_memory, AGCMemory

class AGCRadarSampler:
    def __init__(self):
        self.memory = AGCMemory()

    def sample_radar(self, range):
        store_to_memory("RADAR_RANGE", mask_15bit(range), self.memory.erasable)
        print(f"Radar Sample: Range {range}")
        time.sleep(0.1)
        return range

    def main(self):
        print("Testing Radar Sampler")
        self.sample_radar(5000)