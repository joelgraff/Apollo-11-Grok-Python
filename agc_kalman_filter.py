# agc_kalman_filter.py
from agc_utils import mask_15bit, store_to_memory

class AGCKalmanFilter:
    def __init__(self):
        self.memory = {
            "KF_STATE": 0,    # Kalman filter state (scaled)
            "KF_UPDATE": 0    # Updated state (scaled)
        }

    def apply_kalman(self, measurement):
        """Simulate Kalman filter update."""
        store_to_memory("KF_STATE", mask_15bit(measurement), self.memory)
        update = mask_15bit(measurement + 2)  # Simplified update
        store_to_memory("KF_UPDATE", update, self.memory)
        return update

    def main(self):
        """Sanity check for AGCKalmanFilter."""
        print(f"Initial: KF_STATE={self.memory['KF_STATE']}, KF_UPDATE={self.memory['KF_UPDATE']}")
        update = self.apply_kalman(50)
        print(f"Kalman Update: KF_STATE={self.memory['KF_STATE']}, KF_UPDATE={update}")

if __name__ == "__main__":
    kalman = AGCKalmanFilter()
    kalman.main()