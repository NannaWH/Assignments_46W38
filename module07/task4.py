#################################################################################################
# TASK 4: Optimizing Rotor Diameter ############################################################
#################################################################################################

import numpy as np
from scipy.optimize import minimize, LinearConstraint, NonlinearConstraint

### Setting up equations and parameters

# Constants 
rho = 1.225
C = 0.45
V_in = 3
V_out = 25
hours_pr_year = 8760
P_rated = 10 # This is the desired rated power
hub_height = 100


# Objective function to minimize 
def wind_rated(D):
    V_rated = (P_rated/(1/2 * rho * np.pi * (D/2)**2 * C))**(1/3)
    return -V_rated

# Linear contraint - The rotor radius must not be greater than 80% of the hub height
A = [[1]]
lb = [0]  # diameter must be positive
ub = [2 * 0.8 * hub_height]
linear_con = LinearConstraint(A, lb, ub)
    
#Initial guess
D0 = [40]

res_local = minimize(wind_rated, D0, method='trust-constr', constraints=[linear_con])

print(res_local)


# Non-linear Constraint - The rated power must not exceed 10 MW
# def nonlinear_fun(x):
#    return 1/2 * rho * np.pi * (D/2)**2 * C * V_rated
# nonlinear_con = NonlinearConstraint(nonlinear_fun, 0, 10)

"""
if V < V_in:
    P = 0
elif V_in <= V <= V_rated:
    P = P_rated*((V-V_in)/(V_rated-V_in))
elif V_rated <= V <= V_out:
    P = P_rated
elif V >= V_out:
    P = 0


AEP = hours_pr_year * np.trapezoid(P*PDF, V)
"""