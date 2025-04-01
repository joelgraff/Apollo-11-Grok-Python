# agc_average_g_integrator.py
from agc_utils import mask_15bit, store_to_memory, AGCMemory, time

class AGCAverageGIntegrator:
    def __init__(self):
        self.memory = AGCMemory()
        self.g_sum = 0
        self.count = 0

    def integrate_g(self, g_value):
        self.g_sum += g_value
        self.count += 1
        avg_g = self.g_sum / self.count
        store_to_memory("AVG_G", mask_15bit(int(avg_g * 100)), self.memory.erasable)
        print(f"Average G: {avg_g}")
        return avg_g

    def main(self):
        print("Testing Average G Integrator")
        for g in [9.8, 9.7, 9.9]:
            self.integrate_g(g)
            time.sleep(0.1)