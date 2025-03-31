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
from agc_rtb_op_codes import AGCRTBOpCodes
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
from agc_tuning_parameters import AGCTuningParameters
from agc_tvcexecutive import AGCTVCExecutive
from agc_tvcmaddaps import AGCTVCMaddaps
from agc_tvcstroketest import AGCTVCStrokeTest
from agc_tvcdaps import AGCTVCDaps
from agc_update_program import AGCUpdateProgram
from agc_upper_stage_dap import AGCUpperStageDAP
from agc_utility_routines import AGCUtilityRoutines
from agc_vhf_ranging import AGCVHFRanging
from agc_yul_system_routines import AGCYulSystemRoutines
from agc_contract_and_approvals import AGCContractAndApprovals
from agc_aotmark import AGCAOTMark
from agc_attitude_maneuver_routine import AGCAttitudeManeuverRoutine
from agc_bankcall import AGCBankCall
from agc_burn_baby_burn_master_ignition_rou import AGCBurnBabyBurnMasterIgnitionRoutine
from agc_calcga import AGCCalcGA
from agc_cm_entry_and_return import AGCCMEntryAndReturn
from agc_cm_body_attitude import AGCCMBodyAttitude
from agc_controller_and_meter_routines import AGCControllerAndMeterRoutines
from agc_csm_docked_dap import AGCCSMDockedDAP
from agc_dapa_and_dapb_data import AGCDAPAandDAPBData
from agc_dap_interface_subroutines import AGCDAPInterfaceSubroutines
from agc_dapidler import AGCDAPIdler
from agc_display_interface_routines import AGCDisplayInterfaceRoutines
from agc_down_telemetry_program import AGCDownTelemetryProgram
from agc_extended_verb_routines import AGCExtendedVerbRoutines
from agc_find_cdu_desired import AGCFindCDUDesired
from agc_five_by_five_jet_routines import AGCFiveByFiveJetRoutines
from agc_gimbal_lock_avoidance import AGCGimbalLockAvoidance
from agc_input_output_control import AGCInputOutputControl
from agc_erasable_assignments import AGCErasableAssignments
from agc_interrupt_lead_ins import AGCInterruptLeadIns
from agc_t4rupt_program import AGCT4RuptProgram
from agc_radar_leadin_routines import AGCRadarLeadinRoutines
from agc_mode_switching_and_mark_routines import AGCModeSwitchingAndMarkRoutines
from agc_restarts_routine import AGCRestartsRoutine
from agc_fresh_start_and_restart import AGCFreshStartAndRestart
from agc_imu_compensation_package import AGCIMUCompensationPackage
from agc_rcs_control_mode_package import AGCRCSControlModePackage
from agc_rr_leadin_and_trysw import AGCRRLeadinAndTrysw
from agc_phase_table_maintenance import AGCPhaseTableMaintenance
from agc_imu_mode_switching_routines import AGCIMUModeSwitchingRoutines
from agc_aotmark import AGCAOTMark
from agc_radar_test_programs import AGCRadarTestPrograms
from agc_extended_verbs import AGCExtendedVerbs
from agc_pinball_noun_tables import AGCPinballNounTables
from agc_pinball_game_buttons_and_lights import AGCPinballGameButtonsAndLights
from agc_alarm_and_abort import AGCAlarmAndAbort
from agc_downlink_lists import AGCDownlinkLists
from agc_fresh_start_subroutines import AGCFreshStartSubroutines
from agc_interbank import AGCInterBank
from agc_interpreter import AGCInterpreter
from agc_interpretive_constants import AGCInterpretiveConstants
from agc_single_precision_subroutines import AGCSinglePrecisionSubroutines
from agc_executive import AGCExecutive
from agc_rtb_op_codes import AGCRTBOpCodes
from agc_lem_flight_control_system_test import AGCLemFlightControlSystemTest
from agc_imu_performance_tests_1 import AGCIMUPerformanceTests1
from agc_imu_performance_tests_2 import AGCIMUPerformanceTests2
from agc_imu_performance_tests_3 import AGCIMUPerformanceTests3
from agc_imu_performance_tests_4 import AGCIMUPerformanceTests4
from agc_ground_tracking_determination_prog import AGCGroundTrackingDeterminationProgram
from agc_orbital_integration_for_lm import AGCOrbitalIntegrationForLM
from agc_lm_state_vector_extrapolation import AGCLMStateVectorExtrapolation
from agc_latitude_longitude_subroutines import AGCLatitudeLongitudeSubroutines
from agc_r22 import AGCR22
from agc_r29 import AGCR29
from agc_r31 import AGCR31
from agc_p_axis_rcs_autopilot import AGCPAxisRCSAutopilot
from agc_q_r_axes_rcs_autopilot import AGCQRaxesRCSAutopilot
from agc_kalman_filter import AGCKalmanFilter
from agc_landing_analog_displays import AGCLandingAnalogDisplays
from agc_throttle_control_routines import AGCThrottleControlRoutines
from agc_lunar_landmark_selection_for_lm import AGCLunarLandmarkSelectionForLM
from agc_r60_r62 import AGCR60R62
from agc_p12 import AGCP12
from agc_p20_p25 import AGCP20P25
from agc_p30_p37 import AGCP30P37
from agc_p32_p35_p72_p75 import AGCP32P35P72P75
from agc_p40_p47 import AGCP40P47
from agc_p51_p53 import AGCP51P53
from agc_p60_p67 import AGCP60P67
from agc_p70_p71 import AGCP70P71
from agc_servicer import AGCServicer
from agc_tuning_parameters import AGCTuningParameters
from agc_aostask_and_aosjob import AGCAOSTaskAndAOSJob
from agc_abort_guidance_system import AGCAbortGuidanceSystem
from agc_trim_gimbal_control_system import AGCTrimGimbalControlSystem
from agc_average_g_integrator import AGCAverageGIntegrator
from agc_assembly_and_operation_information import AGCAssemblyAndOperationInformation
from agc_luminary import AGCLuminary

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
    print("\nRunning AGC Tuning Parameters Test:")
    AGCTuningParameters().main()
    print("\nRunning AGC TVC Executive Test:")
    AGCTVCExecutive().main()
    print("\nRunning AGC TVC Maddaps Test:")
    AGCTVCMaddaps().main()
    print("\nRunning AGC TVC Stroke Test:")
    AGCTVCStrokeTest().main()
    print("\nRunning AGC TVC Daps Test:")
    AGCTVCDaps().main()
    print("\nRunning AGC Update Program Test:")
    AGCUpdateProgram().main()
    print("\nRunning AGC Upper Stage DAP Test:")
    AGCUpperStageDAP().main()
    print("\nRunning AGC Utility Routines Test:")
    AGCUtilityRoutines().main()
    print("\nRunning AGC VHF Ranging Test:")
    AGCVHFRanging().main()
    print("\nRunning AGC YUL System Routines Test:")
    AGCYulSystemRoutines().main()
    print("\nRunning AGC Contract and Approvals Test:")
    AGCContractAndApprovals().main()
    print("\nRunning AGC AOT Mark Test:")
    AGCAOTMark().main()
    print("\nRunning AGC Attitude Maneuver Routine Test:")
    AGCAttitudeManeuverRoutine().main()
    print("\nRunning AGC Bank Call Test:")
    AGCBankCall().main()
    print("\nRunning AGC Burn Baby Burn Master Ignition Routine Test:")
    AGCBurnBabyBurnMasterIgnitionRoutine().main()
    print("\nRunning AGC Calc GA Test:")
    AGCCalcGA().main()
    print("\nRunning AGC CM Entry and Return Test:")
    AGCCMEntryAndReturn().main()
    print("\nRunning AGC CM Body Attitude Test:")
    AGCCMBodyAttitude().main()
    print("\nRunning AGC Controller and Meter Routines Test:")
    AGCControllerAndMeterRoutines().main()
    print("\nRunning AGC CSM Docked DAP Test:")
    AGCCSMDockedDAP().main()
    print("\nRunning AGC DAP A and DAP B Data Test:")
    AGCDAPAandDAPBData().main()
    print("\nRunning AGC DAP Interface Subroutines Test:")
    AGCDAPInterfaceSubroutines().main()
    print("\nRunning AGC DAP Idler Test:")
    AGCDAPIdler().main()
    print("\nRunning AGC Display Interface Routines Test:")
    AGCDisplayInterfaceRoutines().main()
    print("\nRunning AGC Down Telemetry Program Test:")
    AGCDownTelemetryProgram().main()
    print("\nRunning AGC Extended Verb Routines Test:")
    AGCExtendedVerbRoutines().main()
    print("\nRunning AGC Find CDU Desired Test:")
    AGCFindCDUDesired().main()
    print("\nRunning AGC Five By Five Jet Routines Test:")
    AGCFiveByFiveJetRoutines().main()
    print("\nRunning AGC Gimbal Lock Avoidance Test:")
    AGCGimbalLockAvoidance().main()
    print("\nRunning AGC Input Output Control Test:")
    AGCInputOutputControl().main()
    print("\nRunning AGC Erasable Assignments Test:")
    AGCErasableAssignments().main()
    print("\nRunning AGC Interrupt Lead Ins Test:")
    AGCInterruptLeadIns().main()
    print("\nRunning AGC T4RUPT Program Test:")
    AGCT4RuptProgram().main()
    print("\nRunning AGC Radar Leadin Routines Test:")
    AGCRadarLeadinRoutines().main()
    print("\nRunning AGC Mode Switching and Mark Routines Test:")
    AGCModeSwitchingAndMarkRoutines().main()
    print("\nRunning AGC Restarts Routine Test:")
    AGCRestartsRoutine().main()
    print("\nRunning AGC Fresh Start and Restart Test:")
    AGCFreshStartAndRestart().main()
    print("\nRunning AGC IMU Compensation Package Test:")
    AGCIMUCompensationPackage().main()
    print("\nRunning AGC RCS Control Mode Package Test:")
    AGCRCSControlModePackage().main()
    print("\nRunning AGC RR Leadin and Trysw Test:")
    AGCRRLeadinAndTrysw().main()
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
    print("\nRunning AGC Pinball Noun Tables Test:")
    AGCPinballNounTables().main()
    print("\nRunning AGC Pinball Game Buttons and Lights Test:")
    AGCPinballGameButtonsAndLights().main()
    print("\nRunning AGC Alarm and Abort Test:")
    AGCAlarmAndAbort().main()
    print("\nRunning AGC Downlink Lists Test:")
    AGCDownlinkLists().main()
    print("\nRunning AGC Fresh Start Subroutines Test:")
    AGCFreshStartSubroutines().main()
    print("\nRunning AGC Inter-Bank Communication Test:")
    AGCInterBank().main()
    print("\nRunning AGC Interpreter Test:")
    AGCInterpreter().main()
    print("\nRunning AGC Interpretive Constants Test:")
    AGCInterpretiveConstants().main()
    print("\nRunning AGC Single Precision Subroutines Test:")
    AGCSinglePrecisionSubroutines().main()
    print("\nRunning AGC Executive Test:")
    AGCExecutive().main()
    print("\nRunning AGC RTB Op Codes Test:")
    AGCRTBOpCodes().main()
    print("\nRunning AGC LEM Flight Control System Test:")
    AGCLemFlightControlSystemTest().main()
    print("\nRunning AGC IMU Performance Tests 1 Test:")
    AGCIMUPerformanceTests1().main()
    print("\nRunning AGC IMU Performance Tests 2 Test:")
    AGCIMUPerformanceTests2().main()
    print("\nRunning AGC IMU Performance Tests 3 Test:")
    AGCIMUPerformanceTests3().main()
    print("\nRunning AGC IMU Performance Tests 4 Test:")
    AGCIMUPerformanceTests4().main()
    print("\nRunning AGC Ground Tracking Determination Program Test:")
    AGCGroundTrackingDeterminationProgram().main()
    print("\nRunning AGC Orbital Integration for LM Test:")
    AGCOrbitalIntegrationForLM().main()
    print("\nRunning AGC LM State Vector Extrapolation Test:")
    AGCLMStateVectorExtrapolation().main()
    print("\nRunning AGC Latitude Longitude Subroutines Test:")
    AGCLatitudeLongitudeSubroutines().main()
    print("\nRunning AGC R22 Test:")
    AGCR22().main()
    print("\nRunning AGC R29 Test:")
    AGCR29().main()
    print("\nRunning AGC R31 Test:")
    AGCR31().main()
    print("\nRunning AGC P-Axis RCS Autopilot Test:")
    AGCPAxisRCSAutopilot().main()
    print("\nRunning AGC Q,R-Axes RCS Autopilot Test:")
    AGCQRaxesRCSAutopilot().main()
    print("\nRunning AGC Kalman Filter Test:")
    AGCKalmanFilter().main()
    print("\nRunning AGC Landing Analog Displays Test:")
    AGCLandingAnalogDisplays().main()
    print("\nRunning AGC Throttle Control Routines Test:")
    AGCThrottleControlRoutines().main()
    print("\nRunning AGC Lunar Landmark Selection for LM Test:")
    AGCLunarLandmarkSelectionForLM().main()
    print("\nRunning AGC R60,R62 Test:")
    AGCR60R62().main()
    print("\nRunning AGC P12 Test:")
    AGCP12().main()
    print("\nRunning AGC P20-P25 Test:")
    AGCP20P25().main()
    print("\nRunning AGC P30,P37 Test:")
    AGCP30P37().main()
    print("\nRunning AGC P32-P35,P72-P75 Test:")
    AGCP32P35P72P75().main()
    print("\nRunning AGC P40-P47 Test:")
    AGCP40P47().main()
    print("\nRunning AGC P51-P53 Test:")
    AGCP51P53().main()
    print("\nRunning AGC P60-P67 Test:")
    AGCP60P67().main()
    print("\nRunning AGC P70-P71 Test:")
    AGCP70P71().main()
    print("\nRunning AGC Servicer Test:")
    AGCServicer().main()
    print("\nRunning AGC Tuning Parameters Test:")
    AGCTuningParameters().main()
    print("\nRunning AGC AOSTask and AOSJob Test:")
    AGCAOSTaskAndAOSJob().main()
    print("\nRunning AGC Abort Guidance System Test:")
    AGCAbortGuidanceSystem().main()
    print("\nRunning AGC Trim Gimbal Control System Test:")
    AGCTrimGimbalControlSystem().main()
    print("\nRunning AGC Average G Integrator Test:")
    AGCAverageGIntegrator().main()
    print("\nRunning AGC Assembly and Operation Information Test:")
    AGCAssemblyAndOperationInformation().main()
    print("\nRunning AGC Luminary Test:")
    AGCLuminary().main()
        
if __name__ == "__main__":
    main()