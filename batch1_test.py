# batch1_test.py
import time
from agc_executive import AGCExecutive
from agc_waitlist import AGCWaitlist
from agc_display_interface_routines import AGCDisplayInterfaceRoutines
from agc_t6rupt import AGCT6Rupt
from agc_keyrupt_uprupt import AGCKeyruptUprupt
from agc_fresh_start_subroutines import AGCFreshStartSubroutines
from agc_find_vac import AGCFindVac
from agc_interrupt_lead_ins import AGCInterruptLeadIns
from agc_t3rupt import AGCT3Rupt
from agc_utils import InterruptManager

def test_batch1():
    interrupts = InterruptManager()
    print("\nTesting Batch 1:")
    print("AGC Executive:"); AGCExecutive().main()
    print("AGC Waitlist:"); AGCWaitlist().main()
    print("AGC Display Interface:"); AGCDisplayInterfaceRoutines().main()
    print("AGC T6Rupt:"); AGCT6Rupt(interrupts).main()
    print("AGC Keyrupt Uprupt:"); AGCKeyruptUprupt(interrupts).main()
    print("AGC Fresh Start:"); AGCFreshStartSubroutines().main()
    print("AGC Find Vac:"); AGCFindVac().main()
    print("AGC Interrupt Lead Ins:"); AGCInterruptLeadIns().main()
    print("AGC T3Rupt:"); AGCT3Rupt(interrupts).main()

if __name__ == "__main__":
    test_batch1()