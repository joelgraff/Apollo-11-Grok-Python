# agc_p30_p37_subroutines.py
from agc_utils import mask_15bit, store_to_memory

class AGCP30P37Subroutines:
    def __init__(self):
        self.memory = {
            "TIGN": 0,       # Ignition time (centiseconds)
            "TNOW": 0,       # Current time (centiseconds)
            "DTMAN": 0       # Time to maneuver
        }

    def calc_dt_man(self, t_ign, t_now):
        """Simulate maneuver time difference calculation."""
        store_to_memory("TIGN", mask_15bit(t_ign), self.memory)
        store_to_memory("TNOW", mask_15bit(t_now), self.memory)
        dt = mask_15bit(t_ign - t_now)
        store_to_memory("DTMAN", dt, self.memory)
        return dt

    def main(self):
        """Sanity check for AGCP30P37Subroutines."""
        print(f"Initial: TIGN={self.memory['TIGN']}, TNOW={self.memory['TNOW']}, DTMAN={self.memory['DTMAN']}")
        dt = self.calc_dt_man(1000, 800)  # 10s ign, 8s now
        print(f"Maneuver DT: TIGN={self.memory['TIGN']}, TNOW={self.memory['TNOW']}, DTMAN={dt}")

if __name__ == "__main__":
    p30_p37_subroutines = AGCP30P37Subroutines()
    p30_p37_subroutines.main()