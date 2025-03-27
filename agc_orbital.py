# agc_orbital.py
from agc_utils import (
    mask_15bit, store_to_memory, fetch_double_precision,
    double_precision_add, double_precision_multiply, sine_approx
)

class AGCOrbital:
    def __init__(self):
        self.memory = {
            "R": (0, 0),    # Position (double-precision)
            "V": (0, 0),    # Velocity
            "T": 0          # Time
        }

    def set_state(self, r_high, r_low, v_high, v_low, t):
        """Set initial orbital state."""
        self.memory["R"] = (mask_15bit(r_high), mask_15bit(r_low))
        self.memory["V"] = (mask_15bit(v_high), mask_15bit(v_low))
        store_to_memory("T", t, self.memory)

    def integrate_step(self, dt):
        """Perform one integration step (simplified)."""
        # AGC uses Keplerian integration; this is a basic Euler step
        r_high, r_low = self.memory["R"]
        v_high, v_low = self.memory["V"]
        # Update position: R = R + V * dt
        dr_high, dr_low = double_precision_multiply(v_high, v_low, dt)
        r_high, r_low = double_precision_add(r_high, r_low, dr_low)
        r_high = mask_15bit(r_high + dr_high)  # Handle carry
        # Update velocity (placeholder: no acceleration yet)
        self.memory["R"] = (r_high, r_low)
        store_to_memory("T", self.memory["T"] + dt, self.memory)
        return r_high, r_low

    def main(self):
        """Sanity check for AGCOrbital."""
        # Set initial state: R = 1000, V = 10, T = 0
        self.set_state(0, 1000, 0, 10, 0)
        print(f"Initial R: {self.memory['R']}, V: {self.memory['V']}, T: {self.memory['T']}")
        # Integrate 5 steps
        for _ in range(5):
            r_high, r_low = self.integrate_step(2)
            print(f"Step R: {r_high}, {r_low}, T: {self.memory['T']}")
        # Test sine (unrelated, just for util check)
        sine_val = sine_approx(0x2000)
        print(f"Sine(pi/4): {sine_val}")

if __name__ == "__main__":
    orbital = AGCOrbital()
    orbital.main()