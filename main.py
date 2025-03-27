# main.py
from agc_utils import main as utils_main
from agc_executive import AGCExecutive
from agc_interpreter import AGCInterpreter
from agc_pinball import AGCPinball
from agc_downlink import AGCDownlink
from agc_orbital import AGCOrbital
from agc_averageg import AGCAverageG
from agc_kalman import AGCKalman
from agc_reentry import AGCReentry
from agc_servicer import AGCServicer
from agc_rcs import AGCRCS
from agc_imu_tests import AGCIMUTests
from agc_t6rupt import AGCT6Rupt
from agc_restarts import AGCRestarts
from agc_freshstart import AGCFreshStart
from agc_checkequals import AGCCheckEquals
from agc_alarm_abort import AGCAlarmAbort
from agc_io_control import AGCIOControl
from agc_dsky import AGCDsky
from agc_interrupts import AGCInterrupts
from agc_t4rupt import AGCT4Rupt
from agc_t3rupt import AGCT3Rupt
from agc_phasetable import AGCPhaseTable
from agc_imu_comp import AGCIMUComp
from agc_rtb_opcodes import AGCRTBOpCodes
from agc_sp_subroutines import AGCSPSroutines
from agc_imu_modes import AGCIMUModes
from agc_groundtrack import AGCGroundTrack
from agc_p20_p25 import AGCP20P25
from agc_p30_p37 import AGCP30P37
from agc_p40_p47 import AGCP40P47
from agc_p60_p67 import AGCP60P67
from agc_p70_p71 import AGCP70P71
from agc_prelaunch import AGCPrelaunch
from agc_rendezvous import AGCRendezvous
from agc_integration_init import AGCIntegrationInit
from agc_down_telemetry import AGCDownTelemetry
from agc_interbank import AGCInterBank
from agc_interp_constants import AGCInterpConstants
from agc_dp_subroutines import AGCDPSubroutines
from agc_erasable import AGCErasable
from agc_restart_tables import AGCRestartTables
from agc_fresh_restart import AGCFreshRestart
from agc_t4rupt_service import AGCT4RuptService
from agc_keyrupt_uprupt import AGCKeyruptUprupt
from agc_self_check import AGCSelfCheck
from agc_imu_tests_2 import AGCIMUTests2
from agc_optics_test import AGCOpticsTest
from agc_extended_verbs import AGCExtendedVerbs
from agc_radar_test import AGCRadarTest
from agc_lunar_landmark import AGCLunarLandmark
from agc_block_two_self_check import AGCBlockTwoSelfCheck
from agc_imu_calib_align import AGCIMUCalibAlign
from agc_orbital_140 import AGCOrbital140
from agc_p76 import AGCP76
from agc_radar_leadin import AGCRadarLeadin
from agc_rcs_failure_monitor import AGCRCSFailureMonitor
from agc_descent_guidance import AGCDescentGuidance
from agc_landing_analog_displays import AGCLandingAnalogDisplays
from agc_find_vac import AGCFindVac
from agc_dap_interface import AGCDAPInterface
from agc_imu_fine_align import AGCIMUFineAlign
from agc_orbital_int_subroutines import AGCOrbitalIntSubroutines
from agc_p12 import AGCP12
from agc_radar_sampler import AGCRadarSampler
from agc_servicer206 import AGCServicer206
from agc_trim_gimbal import AGCTrimGimbal
from agc_kalman_subroutines import AGCKalmanSubroutines
from agc_p20_p25_subroutines import AGCP20P25Subroutines
from agc_p32_p35_p72_p75 import AGCP32P35P72P75
from agc_rcs_dap_exec import AGCRCSDAPExec

def main():
    print("Running AGC Utils Test:")
    utils_main()
    print("\nRunning AGC Executive Test:")
    AGCExecutive().main()
    print("\nRunning AGC Interpreter Test:")
    AGCInterpreter().main()
    print("\nRunning AGC Pinball Test:")
    AGCPinball().main()
    print("\nRunning AGC Downlink Test:")
    AGCDownlink().main()
    print("\nRunning AGC Orbital Test:")
    AGCOrbital().main()
    print("\nRunning AGC AverageG Test:")
    AGCAverageG().main()
    print("\nRunning AGC Kalman Test:")
    AGCKalman().main()
    print("\nRunning AGC Reentry Test:")
    AGCReentry().main()
    print("\nRunning AGC Servicer Test:")
    AGCServicer().main()
    print("\nRunning AGC RCS Test:")
    AGCRCS().main()
    print("\nRunning AGC IMU Tests:")
    AGCIMUTests().main()
    print("\nRunning AGC T6 Interrupt Test:")
    AGCT6Rupt().main()
    print("\nRunning AGC Restarts Test:")
    AGCRestarts().main()
    print("\nRunning AGC Fresh Start Test:")
    AGCFreshStart().main()
    print("\nRunning AGC Check Equals Test:")
    AGCCheckEquals().main()
    print("\nRunning AGC Alarm and Abort Test:")
    AGCAlarmAbort().main()
    print("\nRunning AGC I/O Control Test:")
    AGCIOControl().main()
    print("\nRunning AGC DSKY Test:")
    AGCDsky().main()
    print("\nRunning AGC Interrupts Test:")
    AGCInterrupts().main()
    print("\nRunning AGC T4 Interrupt Test:")
    AGCT4Rupt().main()
    print("\nRunning AGC T3 Interrupt Test:")
    AGCT3Rupt().main()
    print("\nRunning AGC Phase Table Test:")
    AGCPhaseTable().main()
    print("\nRunning AGC IMU Compensation Test:")
    AGCIMUComp().main()
    print("\nRunning AGC RTB Opcodes Test:")
    AGCRTBOpCodes().main()
    print("\nRunning AGC Single Precision Subroutines Test:")
    AGCSPSroutines().main()
    print("\nRunning AGC IMU Mode Switching Test:")
    AGCIMUModes().main()
    print("\nRunning AGC Ground Track Test:")
    AGCGroundTrack().main()
    print("\nRunning AGC P20-P25 Test:")
    AGCP20P25().main()
    print("\nRunning AGC P30-P37 Test:")
    AGCP30P37().main()
    print("\nRunning AGC P40-P47 Test:")
    AGCP40P47().main()
    print("\nRunning AGC P60-P67 Test:")
    AGCP60P67().main()
    print("\nRunning AGC P70-P71 Test:")
    AGCP70P71().main()
    print("\nRunning AGC Prelaunch Alignment Test:")
    AGCPrelaunch().main()
    print("\nRunning AGC Rendezvous Guidance Test:")
    AGCRendezvous().main()
    print("\nRunning AGC Integration Initialization Test:")
    AGCIntegrationInit().main()
    print("\nRunning AGC Down Telemetry Test:")
    AGCDownTelemetry().main()
    print("\nRunning AGC Inter-Bank Communication Test:")
    AGCInterBank().main()
    print("\nRunning AGC Interpretive Constants Test:")
    AGCInterpConstants().main()
    print("\nRunning AGC Double Precision Subroutines Test:")
    AGCDPSubroutines().main()
    print("\nRunning AGC Erasable Assignments Test:")
    AGCErasable().main()
    print("\nRunning AGC Restart Tables Test:")
    AGCRestartTables().main()
    print("\nRunning AGC Fresh Start and Restart Test:")
    AGCFreshRestart().main()
    print("\nRunning AGC T4 Rupt Service Test:")
    AGCT4RuptService().main()
    print("\nRunning AGC KEYRUPT and UPRUPT Test:")
    AGCKeyruptUprupt().main()
    print("\nRunning AGC Self Check Test:")
    AGCSelfCheck().main()
    print("\nRunning AGC IMU Performance Tests 2 Test:")
    AGCIMUTests2().main()
    print("\nRunning AGC Optics Test:")
    AGCOpticsTest().main()
    print("\nRunning AGC Extended Verbs Test:")
    AGCExtendedVerbs().main()
    print("\nRunning AGC Radar Test:")
    AGCRadarTest().main()
    print("\nRunning AGC Lunar Landmark Test:")
    AGCLunarLandmark().main()
    print("\nRunning AGC Block Two Self Check Test:")
    AGCBlockTwoSelfCheck().main()
    print("\nRunning AGC IMU Calibration and Alignment Test:")
    AGCIMUCalibAlign().main()
    print("\nRunning AGC Orbital Integration for 140 Test:")
    AGCOrbital140().main()
    print("\nRunning AGC P76 Test:")
    AGCP76().main()
    print("\nRunning AGC Radar Leadin Test:")
    AGCRadarLeadin().main()
    print("\nRunning AGC RCS Failure Monitor Test:")
    AGCRCSFailureMonitor().main()
    print("\nRunning AGC Descent Guidance Test:")
    AGCDescentGuidance().main()
    print("\nRunning AGC Landing Analog Displays Test:")
    AGCLandingAnalogDisplays().main()
    print("\nRunning AGC Find Vac Test:")
    AGCFindVac().main()
    print("\nRunning AGC DAP Interface Test:")
    AGCDAPInterface().main()
    print("\nRunning AGC IMU Fine Alignment Test:")
    AGCIMUFineAlign().main()
    print("\nRunning AGC Orbital Integration Subroutines Test:")
    AGCOrbitalIntSubroutines().main()
    print("\nRunning AGC P12 Test:")
    AGCP12().main()
    print("\nRunning AGC Radar Sampler Test:")
    AGCRadarSampler().main()
    print("\nRunning AGC Servicer 206 Test:")
    AGCServicer206().main()
    print("\nRunning AGC Trim Gimbal Test:")
    AGCTrimGimbal().main()
    print("\nRunning AGC Kalman Subroutines Test:")
    AGCKalmanSubroutines().main()
    print("\nRunning AGC P20-P25 Subroutines Test:")
    AGCP20P25Subroutines().main()
    print("\nRunning AGC P32-P35 P72-P75 Test:")
    AGCP32P35P72P75().main()
    print("\nRunning AGC RCS DAP Executive Test:")
    AGCRCSDAPExec().main()

if __name__ == "__main__":
    main()