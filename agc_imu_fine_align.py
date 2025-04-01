# agc_imu_fine_align.py
from agc_utils import mask_15bit, store_to_memory, AGCMemory

class AGCIMUFineAlign:
    def __init__(self):
        self.memory = AGCMemory()

    def fine_align(self, angle):
        adj_angle = angle - 1  # Simplified fine adjustment
        store_to_memory("FINE_ANGLE", mask_15bit(adj_angle), self.memory.erasable)
        print(f"Fine Aligned IMU to {adj_angle} degrees")
        return adj_angle

    def main(self):
        print("Testing IMU Fine Align")
        self.fine_align(45)