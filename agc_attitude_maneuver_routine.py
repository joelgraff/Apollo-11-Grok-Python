# agc_attitude_maneuver_routine.py
from agc_utils import mask_15bit, store_to_memory

class AGCAttitudeManeuverRoutine:
    def __init__(self):
        self.memory = {
            "CURRENT_ATT": 0,   # Current attitude (degrees, scaled)
            "TARGET_ATT": 0     # Target attitude (degrees, scaled)
        }

    def maneuver(self, target):
        """Perform an attitude maneuver."""
        store_to_memory("TARGET_ATT", mask_15bit(target), self.memory)
        new_att = mask_15bit(self.memory["CURRENT_ATT"] + (target - self.memory["CURRENT_ATT"]) // 2)  # Simplified step
        store_to_memory("CURRENT_ATT", new_att, self.memory)
        return new_att

    def main(self):
        """Sanity check for AGCAttitudeManeuverRoutine."""
        print(f"Initial: CURRENT_ATT={self.memory['CURRENT_ATT']}, TARGET_ATT={self.memory['TARGET_ATT']}")
        att = self.maneuver(90)
        print(f"Maneuvered: CURRENT_ATT={att}, TARGET_ATT={self.memory['TARGET_ATT']}")

if __name__ == "__main__":
    maneuver = AGCAttitudeManeuverRoutine()
    maneuver.main() # agc_aotmark.py
from agc_utils import mask_15bit, store_to_memory

class AGCAOTMark:
    def __init__(self):
        self.memory = {
            "MARKX": 0,   # X-axis mark (degrees, scaled)
            "MARKY": 0    # Y-axis mark (degrees, scaled)
        }

    def record_mark(self, x_mark, y_mark):
        """Record an AOT (Alignment Optical Telescope) mark."""
        store_to_memory("MARKX", mask_15bit(x_mark), self.memory)
        store_to_memory("MARKY", mask_15bit(y_mark), self.memory)
        return self.memory["MARKX"], self.memory["MARKY"]

    def main(self):
        """Sanity check for AGCAOTMark."""
        print(f"Initial: MARKX={self.memory['MARKX']}, MARKY={self.memory['MARKY']}")
        x, y = self.record_mark(30, 45)
        print(f"AOT Mark: MARKX={x}, MARKY={y}")

if __name__ == "__main__":
    aot = AGCAOTMark()
    aot.main()