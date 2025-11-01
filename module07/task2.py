################################################################################
# TASK 2: Pitch Controller Guide #
################################################################################
## Part 1 - Plotting blade pitch vs wind speed + interpolation function
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#Loading the data into python
data_exc2 = pd.read_excel("Module 7 - Exercises data.xlsx", sheet_name='Exercise 2')

#Defining pirch and wind speed variables
Pitch = data_exc2["Blade pitch (degrees)"]
V = data_exc2["Wind speed (m/s)"]

# Making interpolation for other random wind speeds
from scipy.interpolate import interp1d

# Linear function of wind speed and pitch
f_linear = interp1d(V, Pitch, kind='linear')

# New interpolated data points
V_new = [4.5, 10.5, 15.5, 20.5]
Pitch_new =f_linear(V_new)

#Plotting the time series wind and pitch data + interpolated data points
fig, ax = plt.subplots()
ax.plot(V, Pitch, label = 'Actual Data')
ax.set_xlabel('Wind speed (m/s)', fontsize=10)
ax.set_ylabel('Blade pitch (degrees)', fontsize=10)
ax.plot(V_new, Pitch_new, 'o', label='Interpolated')
ax.grid(True, linestyle="--", alpha=0.5)
plt.show()

## Part 2 - Time Series Variation of Blade Pitch

#Import filtered wind speed data from task 1
import json

with open("filtered_v_output.json", "r") as f:
    winddata_task1 = json.load(f)

#Define variables and calulcate pitch angles from wind speed data
V_variations = np.array(winddata_task1['wind'])
Pitch_variations = f_linear(V_variations)
Time = np.array(winddata_task1['time'])

#Plot pitch angles across time - Showing variations in pitch angles
fig, ax1 = plt.subplots()
ax1.plot(Time, Pitch_variations, label = 'Actual Data')
ax1.set_xlabel('Time (s)', fontsize=10)
ax1.set_ylabel('Blade pitch (degrees)', fontsize=10)
ax1.grid(True, linestyle="--", alpha=0.5)
plt.show()




