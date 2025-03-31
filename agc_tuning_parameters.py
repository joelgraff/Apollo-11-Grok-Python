# agc_tuning_parameters.py
from agc_utils import mask_15bit, store_to_memory

class AGCTuningParameters:
    def __init__(self):
        self.memory = {
            "K_PARAM": 0,    # Tuning constant (scaled)
            "ADJUST": 0      # Adjusted parameter value
        }

    def set_tuning(self, param_value):
        """Set a tuning parameter with scaling."""
        store_to_memory("K_PARAM", mask_15bit(param_value), self.memory)
        adjusted = mask_15bit(param_value * 2)  # Example scaling
        store_to_memory("ADJUST", adjusted, self.memory)
        return adjusted

    def main(self):
        """Sanity check for AGCTuningParameters."""
        print(f"Initial: K_PARAM={self.memory['K_PARAM']}, ADJUST={self.memory['ADJUST']}")
        result = self.set_tuning(100)
        print(f"Tuned: K_PARAM={self.memory['K_PARAM']}, ADJUST={result}")

if __name__ == "__main__":
    tuning_params = AGCTuningParameters()
    tuning_params.main()