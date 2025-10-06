################################################################################################
##### TASK 2: Wind Turbine Metrics Vizualized ##################################################
################################################################################################

import matplotlib.pyplot as plt
import pandas as pd

#Importing data from excel file
data = pd.read_excel("Module 6 - Exercises Data.xlsx")

#Defining variables to be plottet
X = data["Wind speed (m/s)"]
Y1 = data["Power (kW)"]
Y2 = data["Thrust (kN)"]
Y3 = data["Rotor speed (rpm)"]
Y4 = data["Blade pitch (degrees)"]

# Creating a plot with a figure for each metrics
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2,2)

#Plot 1
ax1.plot(X,Y1)
ax1.set_xlabel('Wind speed (m/s)', fontsize=6)
ax1.set_ylabel('Power Curve (kW)', fontsize=6)
ax1.set_title('Power Curve (kW)', fontsize=8)
ax1.tick_params(axis='both', labelsize=6)

#Plot 2
ax2.plot(X,Y2)
ax2.set_xlabel('Wind speed (m/s)', fontsize=6)
ax2.set_ylabel('Thrust (kN)', fontsize=6)
ax2.set_title('Thrust (kN)', fontsize=8)
ax2.tick_params(axis='both', labelsize=6)

#Plot 3
ax3.plot(X,Y3)
ax3.set_xlabel('Wind speed (m/s)', fontsize=6)
ax3.set_ylabel('Rotor speed (rpm)', fontsize=6)
ax3.set_title('Rotor speed (rpm)', fontsize=8)
ax3.tick_params(axis='both', labelsize=6)

#Plot 4
ax4.plot(X,Y4)
ax4.set_xlabel('Wind speed (m/s)', fontsize=6)
ax4.set_ylabel('Blade pitch (degrees)', fontsize=6)
ax4.set_title('Blade pitch (degrees)', fontsize=8)
ax4.tick_params(axis='both', labelsize=6)


#Title for all 4 plots
fig.suptitle('Wind Turbine Metrics by Wind Speed', fontsize=10, fontweight='bold')
fig.tight_layout()



#Show fig
plt.show()