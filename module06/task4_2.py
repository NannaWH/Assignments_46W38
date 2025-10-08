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

# Make a bar chart
#Setting up the plot
fig, axs = plt.subplots(2, 2, figsize=(8, 8))  # Create a figure with 2 subplots side by side
ax1, ax2, ax3, ax4 = axs.flatten()

# Generate sample data for the bar chart
categories = ['Baseline', 'Alternative A', 'Alternative B']
values1 =  [RS1_std, RS2_std, RS3_std]
values2 =  [BP1_std, BP2_std, BP3_std]
values3 =  [PP1_std, PP2_std, PP3_std]
values4 =  [T1_std, T2_std, T3_std]

ax1.bar(categories, values1, color='blue') # command for creating a bar chart
ax1.set_ylabel('Standard Deviation', fontsize=8)
ax1.set_title('Rotor Speed (rpm)', fontsize=8)
ax1.tick_params(axis='both', labelsize=6)

ax2.bar(categories, values2, color='lightblue') # command for creating a bar chart
ax2.set_ylabel('Standard Deviation', fontsize=8)
ax2.set_title('Blade pitch (degrees)', fontsize=8)
ax2.tick_params(axis='both', labelsize=6)

ax3.bar(categories, values3, color='skyblue') # command for creating a bar chart
ax3.set_ylabel('Standard Deviation', fontsize=8)
ax3.set_title('Platform pitch (degrees)', fontsize=8)
ax3.tick_params(axis='both', labelsize=6)

ax4.bar(categories, values4, color='grey') # command for creating a bar chart
ax4.set_ylabel('Standard Deviation', fontsize=8)
ax4.set_title('Thrust (kN)', fontsize=8)
ax4.tick_params(axis='both', labelsize=6)

plt.show()


####### Normalizing Values
#Normalizing Variables with respect to alternative A
RS1_N = data_tbas["Rotor speed (rpm)"] /data_ta["Rotor speed (rpm)"] 
RS2_N = data_ta["Rotor speed (rpm)"] /data_ta["Rotor speed (rpm)"] 
RS3_N = data_tb["Rotor speed (rpm)"] /data_ta["Rotor speed (rpm)"] 

BP1_N = data_tbas["Blade pitch (degrees)"]/data_ta["Blade pitch (degrees)"]
BP2_N = data_ta["Blade pitch (degrees)"]/data_ta["Blade pitch (degrees)"]
BP3_N = data_tb["Blade pitch (degrees)"]/data_ta["Blade pitch (degrees)"]

PP1_N = data_tbas["Platform pitch (degrees)"]/data_ta["Platform pitch (degrees)"]
PP2_N = data_ta["Platform pitch (degrees)"]/data_ta["Platform pitch (degrees)"]
PP3_N = data_tb["Platform pitch (degrees)"]/data_ta["Platform pitch (degrees)"]

T1_N = data_tbas["Thrust (kN)"]/data_ta["Thrust (kN)"]
T2_N = data_ta["Thrust (kN)"]/data_ta["Thrust (kN)"]
T3_N = data_tb["Thrust (kN)"]/data_ta["Thrust (kN)"]

TBM1_N = data_tbas["Tower base moment (kNm)"]/data_ta["Tower base moment (kNm)"]
TBM2_N = data_ta["Tower base moment (kNm)"]/data_ta["Tower base moment (kNm)"]
TBM3_N = data_tb["Tower base moment (kNm)"]/data_ta["Tower base moment (kNm)"]

#Defining the X variables (time)
X = data_tbas["Time (s)"]

#Setting up the plot
fig, axs = plt.subplots(2, 2, figsize=(8, 8))  # Create a figure with 2 subplots side by side
ax_n1, ax_n2, ax_n3, ax_n4 = axs.flatten()

# Plotting the rotor speed for baseline and different alternatives
ax_n1.set_xlabel('Time (s)')
ax_n1.set_ylabel('Rotor speed (rpm)')
ax_n1.plot(X, RS1_N, color='black', label='Baseline, Normalized')
ax_n1.plot(X, RS2_N, color='red', label='Strategy A, Normalized')
ax_n1.plot(X, RS3_N, color='green', label='Strategy B, Normalized')
ax_n1.legend(fontsize=8) #adding legends to the graph

# Plotting the blade pitch for baseline and different alternatives
ax_n2.set_xlabel('Time (s)')
ax_n2.set_ylabel('Blade pitch (degrees')
ax_n2.plot(X, BP1_N, color='black', label='Baseline, Normalized')
ax_n2.plot(X, BP2_N, color='red', label='Strategy A, Normalized')
ax_n2.plot(X, BP3_N, color='green', label='Strategy B, Normalized')
ax_n2.legend(fontsize=8) #adding legends to the graph

# Plotting the Platform pitch for baseline and different alternatives
ax_n3.set_xlabel('Time (s)')
ax_n3.set_ylabel('Platform pitch (degrees)')
ax_n3.plot(X, PP1_N, color='black', label='Baseline, Normalized')
ax_n3.plot(X, PP2_N, color='red', label='Strategy A, Normalized')
ax_n3.plot(X, PP3_N, color='green', label='Strategy B, Normalized')
ax_n3.legend(fontsize=8) #adding legends to the graph

# Plotting the Thrust for baseline and different alternatives
ax_n4.set_xlabel('Time (s)')
ax_n4.set_ylabel('Thrust (kN)')
ax_n4.plot(X, T1_N, color='black', label='Baseline, Normalized')
ax_n4.plot(X, T2_N, color='red', label='Strategy A, Normalized')
ax_n4.plot(X, T3_N, color='green', label='Strategy B, Normalized')
ax_n4.legend(fontsize=8) #adding legends to the graph

plt.show()