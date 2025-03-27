# agc_executive.py
from agc_utils import mask_15bit, double_precision_add, transfer_control, store_to_memory

class AGCExecutive:
    def __init__(self):
        # Simulated AGC memory (simplified subset of registers)
        self.memory = {
            "MPAC": 0,      # Multi-purpose accumulator
            "MPAC+1": 0,    # Second word
            "BUF": 0,       # Buffer
            "NEWJOB": -1,   # Address of new job (-1 = none)
            "LOC": 0,       # Current instruction location
            "PRIORITY": 0   # Current job priority
        }
        self.jobs = []      # List of (address, priority) tuples
        self.max_jobs = 7   # AGC typically supports up to 7 jobs

    def novac(self, job_address, priority=12):
        """Add a non-vacant job (NOVAC routine)."""
        if len(self.jobs) >= self.max_jobs:
            return False  # No vacant slots
        store_to_memory("PRIORITY", priority, self.memory)
        self.jobs.append((job_address, priority))
        return True

    def findvac(self, job_address, priority=12):
        """Find a vacant job slot (FINDVAC routine)."""
        if len(self.jobs) < self.max_jobs:
            store_to_memory("PRIORITY", priority, self.memory)
            self.jobs.append((job_address, priority))
            return True
        return False

    def execute_next_job(self):
        """Execute the highest-priority job."""
        if not self.jobs:
            return None
        # Sort by priority (higher values = higher priority)
        self.jobs.sort(key=lambda x: x[1], reverse=True)
        job_address, priority = self.jobs.pop(0)
        store_to_memory("LOC", job_address, self.memory)
        return transfer_control(job_address, self.memory)

    def load_buffer(self, value):
        """Load a value into BUF."""
        store_to_memory("BUF", value, self.memory)

    def add_buffer_to_accumulator(self):
        """Add BUF to MPAC (example of math operation)."""
        high, low = double_precision_add(
            self.memory["MPAC"], self.memory["MPAC+1"], self.memory["BUF"]
        )
        store_to_memory("MPAC", high, self.memory)
        store_to_memory("MPAC+1", low, self.memory)
        return high, low

    def main(self):
        """Sanity check for AGCExecutive."""
        self.novac(100, priority=12)  # Schedule a job
        self.load_buffer(500)
        result = self.add_buffer_to_accumulator()
        print(f"Addition result: {result}")  # Should print (0, 500)
        job_result = self.execute_next_job()
        print(f"Job executed: {job_result}")  # Simulated job output

if __name__ == "__main__":
    exec = AGCExecutive()
    exec.main()