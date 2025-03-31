# agc_aostask_and_aosjob.py
from agc_utils import mask_15bit, store_to_memory

class AGCAOSTaskAndAOSJob:
    def __init__(self):
        self.memory = {
            "AOS_VAL": 0,    # AOS value (scaled)
            "AOS_FLAG": 0    # AOS task flag (0=pending, 1=done)
        }

    def run_aos(self, value):
        """Simulate AOS task/job execution."""
        store_to_memory("AOS_VAL", mask_15bit(value), self.memory)
        store_to_memory("AOS_FLAG", 1, self.memory)
        return self.memory["AOS_VAL"]

    def main(self):
        """Sanity check for AGCAOSTaskAndAOSJob."""
        print(f"Initial: AOS_VAL={self.memory['AOS_VAL']}, AOS_FLAG={self.memory['AOS_FLAG']}")
        val = self.run_aos(300)
        print(f"AOS Ran: AOS_VAL={val}, AOS_FLAG={self.memory['AOS_FLAG']}")

if __name__ == "__main__":
    aos = AGCAOSTaskAndAOSJob()
    aos.main()