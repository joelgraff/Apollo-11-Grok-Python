# agc_kalman_subroutines.py
from agc_utils import mask_15bit, store_to_memory

class AGCKalmanSubroutines:
    def __init__(self):
        self.memory = {
            "STATE": 0,      # Estimated state (e.g., position, scaled)
            "MEASURE": 0,    # Measured value
            "KGAIN": 0,      # Kalman gain (scaled 0-1)
            "NEWSTATE": 0    # Updated state
        }

    def kalman_update(self, state, measure, gain):
        """Simulate Kalman update subroutine."""
        store_to_memory("STATE", mask_15bit(state), self.memory)
        store_to_memory("MEASURE", mask_15bit(measure), self.memory)
        store_to_memory("KGAIN", mask_15bit(gain), self.memory)
        # Simplified: new_state = state + gain * (measure - state)
        error = measure - state
        new_state = mask_15bit(state + (gain * error // 32768))
        store_to_memory("NEWSTATE", new_state, self.memory)
        return new_state

    def main(self):
        """Sanity check for AGCKalmanSubroutines."""
        print(f"Initial: STATE={self.memory['STATE']}, MEASURE={self.memory['MEASURE']}, KGAIN={self.memory['KGAIN']}")
        state = self.kalman_update(1000, 1050, 16384)  # 1000, 1050, gain=0.5
        print(f"Kalman Update: STATE={self.memory['STATE']}, MEASURE={self.memory['MEASURE']}, NEWSTATE={state}")

if __name__ == "__main__":
    kalman_subroutines = AGCKalmanSubroutines()
    kalman_subroutines.main()