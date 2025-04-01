# batch2_test.py
import time
from agc_p60_p67 import AGCP60P67
from agc_kalman_filter import AGCKalmanFilter
from agc_throttle_control_routines import AGCThrottleControlRoutines
from agc_descent_guidance import AGCDescentGuidance
from agc_p_axis_rcs_autopilot import AGCPAxisRCSAutopilot
from agc_q_r_axes_rcs_autopilot import AGCQRaxesRCSAutopilot
from agc_orbital_integration_for_lm import AGCOrbitalIntegrationForLM
from agc_lm_state_vector_extrapolation import AGCLMStateVectorExtrapolation
from agc_average_g_integrator import AGCAverageGIntegrator
from agc_r60_r62 import AGCR60R62

def test_batch2():
    print("\nTesting Batch 2:")
    print("AGC P60-P67:"); AGCP60P67().main()
    print("AGC Kalman Filter:"); AGCKalmanFilter().main()
    print("AGC Throttle Control:"); AGCThrottleControlRoutines().main()
    print("AGC Descent Guidance:"); AGCDescentGuidance().main()
    print("AGC P-Axis RCS:"); AGCPAxisRCSAutopilot().main()
    print("AGC QR-Axes RCS:"); AGCQRaxesRCSAutopilot().main()
    print("AGC Orbital Integration:"); AGCOrbitalIntegrationForLM().main()
    print("AGC State Vector Extrapolation:"); AGCLMStateVectorExtrapolation().main()
    print("AGC Average G Integrator:"); AGCAverageGIntegrator().main()
    print("AGC R60-R62:"); AGCR60R62().main()

if __name__ == "__main__":
    test_batch2()