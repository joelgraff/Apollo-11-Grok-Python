# agc_servicer.py
import time
from agc_utils import mask_15bit, store_to_memory, AGCMemory

class AGCServicer:
    def __init__(self):
        self.memory = AGCMemory()

    def run_service(self, value):
        store_to_memory("SERV_VAL", mask_15bit(value), self.memory.erasable)
        print(f"Servicing: {value}")
        time.sleep(0.2)  # Simulate background task
        print("Service Done")

    def main(self):
        print("Starting Servicer")
        self.run_service(400)