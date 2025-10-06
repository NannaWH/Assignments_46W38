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

##### Task 4.1

#Defining the rotor speed variables 
X = data_tbas["Time (s)"]
Y1 = data_tbas["Rotor speed (rpm)"] 
Y2 = data_ta["Rotor speed (rpm)"] 
Y3 = data_tb["Rotor speed (rpm)"]

#Setting up the plot
fig, ax = plt.subplots()
ax.set_xlabel('Time (s)')
ax.set_ylabel('Rotor speed (rpm)')

# Plotting the rotor speed for baseline and different alternatives
ax.plot(X, Y1, color='black', label='Baseline')
ax.plot(X, Y2, color='red', label='Strategy A')
ax.plot(X, Y3, color='green', label='Strategy B')

ax.legend() #adding legends to the graph
plt.show()