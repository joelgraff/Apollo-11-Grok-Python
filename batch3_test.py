# batch3_test.py
import time
from agc_p70_p71 import AGCP70P71
from agc_servicer import AGCServicer
from agc_imu_compensation_package import AGCIMUCompensationPackage
from agc_p12 import AGCP12
from agc_p51_p53 import AGCP51P53
from agc_radar_sampler import AGCRadarSampler
from agc_t4rupt import AGCT4Rupt
from agc_pinball_noun_tables import AGCPinballNounTables
from agc_landing_analog_displays import AGCLandingAnalogDisplays
from agc_p30_p37 import AGCP30P37
from agc_utils import InterruptManager

def test_batch3():
    interrupts = InterruptManager()
    print("\nTesting Batch 3:")
    print("AGC P70-P71:"); AGCP70P71().main()
    print("AGC Servicer:"); AGCServicer().main()
    print("AGC IMU Compensation:"); AGCIMUCompensationPackage().main()
    print("AGC P12:"); AGCP12().main()
    print("AGC P51-P53:"); AGCP51P53().main()
    print("AGC Radar Sampler:"); AGCRadarSampler().main()
    print("AGC T4Rupt:"); AGCT4Rupt(interrupts).main()
    print("AGC Pinball Noun Tables:"); AGCPinballNounTables().main()
    print("AGC Landing Analog Displays:"); AGCLandingAnalogDisplays().main()
    print("AGC P30-P37:"); AGCP30P37().main()

if __name__ == "__main__":
    test_batch3()