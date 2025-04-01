# agc_p51_p53.py
from agc_utils import mask_15bit, store_to_memory, AGCMemory

class AGCP51P53:
    def __init__(self):
        self.memory = AGCMemory()

    def align_imu(self, angle):
        store_to_memory("P51_ANGLE", mask_15bit(angle), self.memory.erasable)
        print(f"IMU Aligned to {angle} degrees")
        return angle

    def main(self):
        print("Testing P51-P53 IMU Alignment")
        self.align_imu(45)