# agc_service_routines.py
from agc_utils import mask_15bit, store_to_memory

class AGCServiceRoutines:
    def __init__(self):
        self.memory = {
            "SERV_VAL": 0,    # Service value (scaled)
            "SERV_FLAG": 0    # Service flag (0=pending, 1=done)
        }

    def run_service(self, value):
        """Simulate a service routine execution."""
        store_to_memory("SERV_VAL", mask_15bit(value), self.memory)
        store_to_memory("SERV_FLAG", 1, self.memory)
        return self.memory["SERV_VAL"]

    def main(self):
        """Sanity check for AGCServiceRoutines."""
        print(f"Initial: SERV_VAL={self.memory['SERV_VAL']}, SERV_FLAG={self.memory['SERV_FLAG']}")
        val = self.run_service(300)
        print(f"Serviced: SERV_VAL={val}, SERV_FLAG={self.memory['SERV_FLAG']}")

if __name__ == "__main__":
    service = AGCServiceRoutines()
    service.main()