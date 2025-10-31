################################################################################
# TASK 1: Object Oriented Estimation of Turbine Output #
################################################################################

# importing relevant libraries here:
import numpy as np
import pandas as pd
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

# We dine V a vector of wind speeds
#Wind Speed Vector
v = np.arange(0, 25, 0.5)

class GeneralWindTurbine(object):
 """
 A general wind turbine class
 """
 # write the class here:
 def __init__(self, p_rated=15, v_in = 3, v_ratd = 11, v_out = 25, name = None):
    """We define the function variables:"""
    self.p_rated = p_rated
    self.v_in = v_in
    self.v_ratd = v_ratd
    self.v_out = v_out
    self.name = name if name else "NoName"
    
    # We check for error in user input 
    inputs = {'p_rated': p_rated, 'v_in': v_in, 'v_ratd': v_ratd, 'v_out': v_out}

    for name, value in inputs.items():
        if not isinstance(value, (int, float)): 
            raise ValueError(f"Invalid input: {value} is not a number")  

 def __str__(self):
    return f"{self.name}"

 def get_power(self, v=v):
    """We define the function calculating the power output by wind speed"""
    # We calculate the power output P(v) based on power curve assumptions

    # We calculate the power output P(v)
    p = np.where(
        (v < self.v_in) | (v >= self.v_out), 0,
        np.where((v >= self.v_in) & (v < self.v_ratd),self.p_rated* (v/self.v_ratd)**3,
            np.where((self.v_ratd <= v) & (v < self.v_out), self.p_rated,
                0 
            )))
    
    # Combine wind speeds and powers into a 2-column array
    result = np.column_stack((v, p))

    return result

class WindTurbine(GeneralWindTurbine):
 """
 Wind Turbine class using power curve data to determine the power output
 """
 def __init__(self, p_rated=15, v_in=3, v_ratd=11, v_out=25, name=None):
    super().__init__(p_rated, v_in, v_ratd, v_out, name)

    power_curve_data = pd.read_csv("LEANWIND_Reference_8MW_164.csv", )
    self.power_curve_data = np.array(power_curve_data)

    self.wind_speeds = self.power_curve_data[:,0]
    self.power = self.power_curve_data[:,1]/1000

 def __str__(self):
    return f"{self.name}"

 def get_power(self, v=v):
     """ Calculating power based on power curve data"""

     #We define a interpolated power function:
     power_int = interp1d(self.wind_speeds, self.power, kind='linear', fill_value='extrapolate')

     p = np.where(
        (v < self.v_in) | (v >= self.v_out), 0,
        np.where((v >= self.v_in) & (v < self.v_ratd), power_int(v),
            np.where((self.v_ratd <= v) & (v < self.v_out), self.p_rated,
                0 
            )))
     
     # Combine wind speeds and powers into a 2-column array
     result = np.column_stack((v, p))

     return result
 

if __name__ == '__main__':
 # Write the main script to use the classes and make the plot here
 wt_gt = GeneralWindTurbine(p_rated=8, v_in=4, v_ratd=12.5, v_out=25, name= "GT")
 wt_dt = WindTurbine(p_rated=8, v_in=4, v_ratd=12.5, v_out=25, name= "DT")

 for turbine in [wt_gt, wt_dt]:
    # We call the function for that calculates the power output
    results = pd.DataFrame(turbine.get_power(), columns=("V", "P"))

    results.to_csv(f"results_{turbine}.csv", index=False, sep="\t")

# We create graphs tu compate the two power curves
GT = pd.read_csv("results_GT.csv", sep="\t")
DT = pd.read_csv("results_DT.csv", sep="\t")

fig, ax1 = plt.subplots()

ax1.plot(GT["V"], GT["P"], label = "General Wind Turbine - Power Equation" )
ax1.plot(DT["V"], DT["P"], label = "Wind Turbine - Power Data")

ax1.set_xlabel('Wind Speed (m/s)')
ax1.set_ylabel('Power Output (MW)')
plt.title("Power Curves for Power Equation and Power Data")
ax1.legend()

plt.show()

