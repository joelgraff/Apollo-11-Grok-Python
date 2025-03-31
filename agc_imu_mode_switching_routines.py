# agc_imu_mode_switching_routines.py
from agc_utils import mask_15bit, store_to_memory

class AGCIMUModeSwitchingRoutines:
    def __init__(self):
        self.memory = {
            "IMU_MODE": 0,    # IMU mode (0=off, 1=on)
            "MODE_CMD": 0     # Mode command (scaled)
        }

    def switch_imu_mode(self, mode):
        """Simulate IMU mode switching."""
        store_to_memory("IMU_MODE", mask_15bit(mode), self.memory)
        store_to_memory("MODE_CMD", mask_15bit(mode * 10), self.memory)  # Simplified scaling
        return self.memory["IMU_MODE"]

    def main(self):
        """Sanity check for AGCIMUModeSwitchingRoutines."""
        print(f"Initial: IMU_MODE={self.memory['IMU_MODE']}, MODE_CMD={self.memory['MODE_CMD']}")
        mode = self.switch_imu_mode(1)  # Switch to on
        print(f"IMU Mode: IMU_MODE={mode}, MODE_CMD={self.memory['MODE_CMD']}")

if __name__ == "__main__":
    imu_modes = AGCIMUModeSwitchingRoutines()
    imu_modes.main()