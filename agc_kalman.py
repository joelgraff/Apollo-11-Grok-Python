# agc_kalman.py
from agc_utils import (
    mask_15bit, store_to_memory, fetch_double_precision,
    double_precision_add, double_precision_multiply,
    double_precision_subtract
)

class AGCKalman:
    def __init__(self):
        self.memory = {
            "STATE": (0, 0),  # Estimated state (e.g., position, simplified)
            "ERROR": (0, 0)   # Error covariance
        }

    def update_state(self, measurement_high, measurement_low):
        """Simplified Kalman update step."""
        state_high, state_low = self.memory["STATE"]
        error_high, error_low = self.memory["ERROR"]
        # Gain (simplified, AGC uses complex matrix ops)
        gain = 1  # Placeholder for actual Kalman gain
        # Update state: STATE = STATE + GAIN * (MEASUREMENT - STATE)
        diff_high, diff_low = double_precision_subtract(
            measurement_high, measurement_low, state_low
        )
        diff_high = mask_15bit(diff_high - state_high)
        correction_high, correction_low = double_precision_multiply(diff_high, diff_low, gain)
        state_high, state_low = double_precision_add(
            state_high, state_low, correction_low
        )
        state_high = mask_15bit(state_high + correction_high)
        self.memory["STATE"] = (state_high, state_low)
        return state_high, state_low

    def main(self):
        """Sanity check for AGCKalman."""
        self.memory["STATE"] = (0, 1000)  # Initial state
        print(f"Initial State: {self.memory['STATE']}")
        # Simulate measurement
        updated_high, updated_low = self.update_state(0, 1200)
        print(f"Updated State after 1200 measurement: {updated_high}, {updated_low}")
        # Another update
        updated_high, updated_low = self.update_state(0, 1100)
        print(f"Updated State after 1100 measurement: {updated_high}, {updated_low}")

if __name__ == "__main__":
    kalman = AGCKalman()
    kalman.main()