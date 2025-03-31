# agc_controller_and_meter_routines.py
from agc_utils import mask_15bit, store_to_memory

class AGCControllerAndMeterRoutines:
    def __init__(self):
        self.memory = {
            "INPUT": 0,    # Controller input (scaled)
            "METER": 0     # Meter output (scaled)
        }

    def update_meter(self, input_value):
        """Update meter based on controller input."""
        store_to_memory("INPUT", mask_15bit(input_value), self.memory)
        meter_val = mask_15bit(input_value * 5)  # Simplified scaling
        store_to_memory("METER", meter_val, self.memory)
        return meter_val

    def main(self):
        """Sanity check for AGCControllerAndMeterRoutines."""
        print(f"Initial: INPUT={self.memory['INPUT']}, METER={self.memory['METER']}")
        meter = self.update_meter(10)
        print(f"Meter Update: INPUT={self.memory['INPUT']}, METER={meter}")

if __name__ == "__main__":
    controller = AGCControllerAndMeterRoutines()
    controller.main()