# agc_imu_comp.py
from agc_utils import mask_15bit, store_to_memory, double_precision_add, double_precision_subtract

class AGCIMUComp:
    def __init__(self):
        self.memory = {
            "GYROX": (0, 0),    # Measured gyro value (double precision)
            "DRIFTX": (0, 0),   # Drift coefficient (double precision)
            "COMPX": (0, 0)     # Compensated gyro value (double precision)
        }

    def set_gyro_data(self, gyro_high, gyro_low, drift_high, drift_low):
        """Set gyro measurement and drift coefficient."""
        self.memory["GYROX"] = (mask_15bit(gyro_high), mask_15bit(gyro_low))
        self.memory["DRIFTX"] = (mask_15bit(drift_high), mask_15bit(drift_low))

    def compensate_gyro(self):
        """Apply drift compensation to gyro reading."""
        gyro_high, gyro_low = self.memory["GYROX"]
        drift_high, drift_low = self.memory["DRIFTX"]
        # Subtract drift from measured value
        comp_high, comp_low = double_precision_subtract(gyro_high, gyro_low, drift_low)
        # Adjust high word if borrow occurred from low word
        if gyro_low < drift_low:
            comp_high = mask_15bit(comp_high - drift_high - 1)
        else:
            comp_high = mask_15bit(comp_high - drift_high)
        self.memory["COMPX"] = (comp_high, comp_low)
        return comp_high, comp_low

    def main(self):
        """Sanity check for AGCIMUComp."""
        # Set gyro data: measured 1000, drift 50
        self.set_gyro_data(0, 1000, 0, 50)
        print(f"Initial: GYROX={self.memory['GYROX']}, DRIFTX={self.memory['DRIFTX']}")
        # Compensate
        comp_high, comp_low = self.compensate_gyro()
        print(f"Compensated: COMPX={self.memory['COMPX']} (Expected: 0, 950)")

if __name__ == "__main__":
    imu_comp = AGCIMUComp()
    imu_comp.main()