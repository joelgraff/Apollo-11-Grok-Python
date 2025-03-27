# agc_p32_p35_p72_p75.py
from agc_utils import mask_15bit, store_to_memory

class AGCP32P35P72P75:
    def __init__(self):
        self.memory = {
            "VELCUR": 0,     # Current velocity (m/s, scaled)
            "VELTGT": 0,     # Target velocity
            "DELTAV": 0      # Delta-V required
        }

    def calc_deltav(self, current_vel, target_vel):
        """Simulate delta-V calculation for targeting."""
        store_to_memory("VELCUR", mask_15bit(current_vel), self.memory)
        store_to_memory("VELTGT", mask_15bit(target_vel), self.memory)
        deltav = mask_15bit(target_vel - current_vel)
        store_to_memory("DELTAV", deltav, self.memory)
        return deltav

    def main(self):
        """Sanity check for AGCP32P35P72P75."""
        print(f"Initial: VELCUR={self.memory['VELCUR']}, VELTGT={self.memory['VELTGT']}, DELTAV={self.memory['DELTAV']}")
        dv = self.calc_deltav(500, 600)  # 500 m/s to 600 m/s
        print(f"Delta-V: VELCUR={self.memory['VELCUR']}, VELTGT={self.memory['VELTGT']}, DELTAV={dv}")

if __name__ == "__main__":
    p32_p35_p72_p75 = AGCP32P35P72P75()
    p32_p35_p72_p75.main()