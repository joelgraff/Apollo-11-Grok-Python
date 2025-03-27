# agc_prelaunch.py
from agc_utils import mask_15bit, store_to_memory

class AGCPrelaunch:
    def __init__(self):
        self.memory = {
            "IMUSTATE": 0,    # IMU mode: 0=off, 1=caged, 2=coarse, 3=fine
            "ORIENT": 0,      # Orientation angle (degrees, simplified)
            "ALIGNFLAG": 0    # Alignment status flag
        }

    def p51_align(self):
        """Simulate P51: Coarse IMU alignment."""
        # Set IMU to coarse align mode
        store_to_memory("IMUSTATE", 2, self.memory)
        # Simulate orientation from star sighting or gravity (arbitrary 45°)
        store_to_memory("ORIENT", mask_15bit(45), self.memory)
        # Mark alignment complete
        store_to_memory("ALIGNFLAG", 1, self.memory)
        return self.memory["ORIENT"], self.memory["ALIGNFLAG"]

    def main(self):
        """Sanity check for AGCPrelaunch."""
        print(f"Initial: IMUSTATE={self.memory['IMUSTATE']}, ORIENT={self.memory['ORIENT']}, ALIGNFLAG={self.memory['ALIGNFLAG']}")
        # Run P51 alignment
        orient, flag = self.p51_align()
        print(f"P51 Align: IMUSTATE={self.memory['IMUSTATE']}, ORIENT={orient}, ALIGNFLAG={flag}")

if __name__ == "__main__":
    prelaunch = AGCPrelaunch()
    prelaunch.main()