# Add to main.py
from agc_phase_table_maintenance import AGCPhaseTableMaintenance
from agc_imu_mode_switching_routines import AGCIMUModeSwitchingRoutines
from agc_aotmark import AGCAOTMark
from agc_radar_test_programs import AGCRadarTestPrograms
from agc_extended_verbs import AGCExtendedVerbs

def main():
    # Existing 108 calls...
    print("\nRunning AGC Phase Table Maintenance Test:")
    AGCPhaseTableMaintenance().main()
    print("\nRunning AGC IMU Mode Switching Routines Test:")
    AGCIMUModeSwitchingRoutines().main()
    print("\nRunning AGC AOT Mark Test:")
    AGCAOTMark().main()
    print("\nRunning AGC Radar Test Programs Test:")
    AGCRadarTestPrograms().main()
    print("\nRunning AGC Extended Verbs Test:")
    AGCExtendedVerbs().main()