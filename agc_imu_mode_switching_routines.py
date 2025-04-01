# agc_imu_mode_switching_routines.py
from agc_utils import mask_15bit, store_to_memory, AGCMemory

class AGCIMUModeSwitchingRoutines:
    def __init__(self):
        self.memory = AGCMemory()
        self.mode = 0  # 0=off, 1=coarse, 2=fine

    def switch_mode(self, mode):
        self.mode = mode
        store_to_memory("IMU_MODE", mask_15bit(mode), self.memory.erasable)
        modes = {0: "Off", 1: "Coarse Align", 2: "Fine Align"}
        print(f"IMU Mode: {modes.get(mode, 'Unknown')}")

    def main(self):
        print("Testing IMU Mode Switching")
        self.switch_mode(1)
        self.switch_mode(2)