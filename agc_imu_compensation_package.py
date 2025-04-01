# agc_imu_compensation_package.py
from agc_utils import mask_15bit, store_to_memory, AGCMemory

class AGCIMUCompensationPackage:
    def __init__(self):
        self.memory = AGCMemory()
        self.drift = 0

    def compensate_imu(self, drift):
        self.drift = drift
        comp = mask_15bit(-drift)  # Simplified compensation
        store_to_memory("IMU_COMP", comp, self.memory.erasable)
        print(f"IMU Compensated: {comp}")
        return comp

    def main(self):
        print("Testing IMU Compensation")
        self.compensate_imu(5)