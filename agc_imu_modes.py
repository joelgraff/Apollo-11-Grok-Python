# agc_imu_modes.py
from agc_utils import mask_15bit, store_to_memory

class AGCIMUModes:
    def __init__(self):
        self.memory = {
            "IMUSTATE": 0,    # IMU mode: 0=off, 1=caged, 2=coarse, 3=fine
            "GYROCMD": 0      # Gyro command value
        }
        self.modes = {0: "OFF", 1: "CAGED", 2: "COARSE", 3: "FINE"}

    def set_mode(self, mode):
        """Set IMU mode."""
        if mode in self.modes:
            store_to_memory("IMUSTATE", mode, self.memory)
            # Simulate gyro command for coarse/fine modes
            if mode == 2:  # Coarse align
                store_to_memory("GYROCMD", 100, self.memory)
            elif mode == 3:  # Fine align
                store_to_memory("GYROCMD", 10, self.memory)
            else:  # Off or caged
                store_to_memory("GYROCMD", 0, self.memory)
            return True
        return False

    def get_mode(self):
        """Retrieve current IMU mode."""
        return self.modes.get(self.memory["IMUSTATE"], "UNKNOWN")

    def main(self):
        """Sanity check for AGCIMUModes."""
        # Start off
        print(f"Initial: Mode={self.get_mode()}, GYROCMD={self.memory['GYROCMD']}")
        # Switch to caged
        self.set_mode(1)
        print(f"Caged: Mode={self.get_mode()}, GYROCMD={self.memory['GYROCMD']}")
        # Switch to coarse align
        self.set_mode(2)
        print(f"Coarse: Mode={self.get_mode()}, GYROCMD={self.memory['GYROCMD']}")
        # Switch to fine align
        self.set_mode(3)
        print(f"Fine: Mode={self.get_mode()}, GYROCMD={self.memory['GYROCMD']}")

if __name__ == "__main__":
    imu_modes = AGCIMUModes()
    imu_modes.main()