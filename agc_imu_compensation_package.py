# agc_imu_compensation_package.py
from agc_utils import mask_15bit, store_to_memory

class AGCIMUCompensationPackage:
    def __init__(self):
        self.memory = {
            "IMU_ERROR": 0,    # IMU error (degrees, scaled)
            "COMP_VALUE": 0    # Compensated value (degrees, scaled)
        }

    def compensate_imu(self, error):
        """Simulate IMU error compensation."""
        store_to_memory("IMU_ERROR", mask_15bit(error), self.memory)
        comp = mask_15bit(error * 2)  # Simplified scaling
        store_to_memory("COMP_VALUE", comp, self.memory)
        return comp

    def main(self):
        """Sanity check for AGCIMUCompensationPackage."""
        print(f"Initial: IMU_ERROR={self.memory['IMU_ERROR']}, COMP_VALUE={self.memory['COMP_VALUE']}")
        comp = self.compensate_imu(5)
        print(f"Compensated: IMU_ERROR={self.memory['IMU_ERROR']}, COMP_VALUE={comp}")

if __name__ == "__main__":
    imu_comp = AGCIMUCompensationPackage()
    imu_comp.main()