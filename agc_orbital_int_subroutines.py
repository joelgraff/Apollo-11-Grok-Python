# agc_orbital_int_subroutines.py
from agc_utils import mask_15bit, store_to_memory

class AGCOrbitalIntSubroutines:
    def __init__(self):
        self.memory = {
            "VEL": 0,       # Velocity (m/s, scaled)
            "ACCEL": 0,     # Acceleration (m/s^2, scaled)
            "DELTAT": 0     # Time step (centiseconds)
        }

    def vel_update(self, velocity, accel, delta_t):
        """Simulate velocity update subroutine."""
        store_to_memory("VEL", mask_15bit(velocity), self.memory)
        store_to_memory("ACCEL", mask_15bit(accel), self.memory)
        store_to_memory("DELTAT", mask_15bit(delta_t), self.memory)
        # v = v0 + a * dt (dt in seconds)
        new_vel = mask_15bit(velocity + (accel * delta_t // 100))
        store_to_memory("VEL", new_vel, self.memory)
        return new_vel

    def main(self):
        """Sanity check for AGCOrbitalIntSubroutines."""
        print(f"Initial: VEL={self.memory['VEL']}, ACCEL={self.memory['ACCEL']}, DELTAT={self.memory['DELTAT']}")
        vel = self.vel_update(100, 2, 100)  # 100 m/s, 2 m/s^2, 1s
        print(f"Vel Update: VEL={vel}, ACCEL={self.memory['ACCEL']}, DELTAT={self.memory['DELTAT']}")

if __name__ == "__main__":
    orbital_int_subroutines = AGCOrbitalIntSubroutines()
    orbital_int_subroutines.main()