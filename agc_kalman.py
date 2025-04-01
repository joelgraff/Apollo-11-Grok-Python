# agc_kalman_filter.py
import time
from agc_utils import mask_15bit, store_to_memory, AGCMemory

class AGCKalmanFilter:
    def __init__(self):
        self.memory = AGCMemory()
        self.state = 0

    def update(self, measurement):
        pred = self.state + 1
        gain = 0.5
        self.state = int(pred + gain * (measurement - pred))
        store_to_memory("KF_STATE", mask_15bit(self.state), self.memory.erasable)
        return self.state

    def main(self):
        print("Starting Kalman Filter")
        measurements = [10, 12, 15]
        for m in measurements:
            state = self.update(m)
            print(f"Updated State: {state}")
            time.sleep(0.1)