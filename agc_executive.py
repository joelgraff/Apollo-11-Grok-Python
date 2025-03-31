# agc_executive.py
from agc_utils import mask_15bit, store_to_memory, PriorityQueue, AGCMemory, InterruptManager

class AGCExecutive:
    def __init__(self):
        self.memory = AGCMemory()
        self.queue = PriorityQueue()
        self.interrupts = InterruptManager()
        self.running = False

    def schedule_task(self, task_id, priority):
        self.queue.put((priority, task_id))
        store_to_memory(f"TASK_{task_id}", mask_15bit(task_id), self.memory.erasable)
        return task_id

    def find_vac(self, size):
        return self.memory.allocate_vac(size)

    def run(self):
        self.running = True
        while not self.queue.empty() and self.running:
            pri, task_id = self.queue.get()
            print(f"Executing Task {task_id} (Priority {pri})")
            time.sleep(0.1)  # Simulate execution

    def main(self):
        print("Starting Executive")
        self.schedule_task(1, 2)
        self.schedule_task(2, 1)
        addr = self.find_vac(3)
        print(f"Vacancy at {addr}")
        self.run()