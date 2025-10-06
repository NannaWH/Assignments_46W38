#################################################################################################
# TASK 4: 3D Visualization of Power Coefficient as Function of Tip Speed Ratio and Pitch Angle #
#################################################################################################

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#Importing data from excel files
data_tbas = pd.read_excel("Module 6 - Exercises Data.xlsx", sheet_name='Exercise 4 - Baseline')
data_ta = pd.read_excel("Module 6 - Exercises Data.xlsx", sheet_name='Exercise 4 - A')
data_tb = pd.read_excel("Module 6 - Exercises Data.xlsx", sheet_name='Exercise 4 - B')

#Defining the rotor speed variables 
X = data_tbas["Time (s)"]
Y1 = data_tbas["Rotor speed (rpm)"] 
Y2 = data_ta["Rotor speed (rpm)"] 
Y3 = data_tb["Rotor speed (rpm)"]

##### Task 4.2

###### Standard Deviations
#Calculating standard diviations
RS1_std = np.std(data_tbas["Rotor speed (rpm)"])
BP1_std = np.std(data_tbas["Blade pitch (degrees)"])
PP1_std = np.std(data_tbas["Platform pitch (degrees)"])
T1_std = np.std(data_tbas["Thrust (kN)"])
TBM1_std = np.std(data_tbas["Tower base moment (kNm)"])

RS2_std = np.std(data_ta["Rotor speed (rpm)"])
BP2_std = np.std(data_ta["Blade pitch (degrees)"])
PP2_std = np.std(data_ta["Platform pitch (degrees)"])
T2_std = np.std(data_ta["Thrust (kN)"])
TBM2_std = np.std(data_ta["Tower base moment (kNm)"])

RS3_std = np.std(data_tb["Rotor speed (rpm)"])
BP3_std = np.std(data_tb["Blade pitch (degrees)"])
PP3_std = np.std(data_tb["Platform pitch (degrees)"])
T3_std = np.std(data_tb["Thrust (kN)"])
TBM3_std = np.std(data_tb["Tower base moment (kNm)"])

# Define the metrics (group names)
metrics = ["Rotor speed", "Blade pitch", "Platform pitch", "Thrust", "Tower base moment"]
x = np.arange(len(metrics))  # bar positions
width = 0.25  # bar width



####### Normalizing Values
#Normalizing the rotor speed variable
Y1_N = Y1/Y1
Y2_N = Y2/Y1
Y3_N = Y3/Y1

#Setting up the plot
fig, ax_n = plt.subplots()
ax_n.set_xlabel('Time (s)')
ax_n.set_ylabel('Rotor speed (rpm)')

# Plotting the rotor speed for baseline and different alternatives
ax_n.plot(X, Y1_N, color='black', label='Baseline, Normalized')
ax_n.plot(X, Y2_N, color='red', label='Strategy A, Normalized')
ax_n.plot(X, Y3_N, color='green', label='Strategy B, Normalized')

ax_n.legend() #adding legends to the graph
plt.show()