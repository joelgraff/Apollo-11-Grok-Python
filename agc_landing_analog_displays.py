# agc_landing_analog_displays.py
from agc_utils import mask_15bit, store_to_memory, AGCMemory, DSKYMock

class AGCLandingAnalogDisplays:
    def __init__(self):
        self.memory = AGCMemory()
        self.dsky = DSKYMock()

    def update_displays(self, alt, vel):
        store_to_memory("ALT_DISP", mask_15bit(alt), self.memory.erasable)
        store_to_memory("VEL_DISP", mask_15bit(vel), self.memory.erasable)
        self.dsky.show(f"Alt: {alt}, Vel: {vel}")

    def main(self):
        print("Testing Landing Analog Displays")
        self.update_displays(1000, 20)