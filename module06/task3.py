#################################################################################################
# TASK 3: 3D Visualization of Power Coefficient as Function of Tip Speed Ratio and Pitch Angle #
#################################################################################################

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#Importing data from excel file
data = pd.read_excel("Module 6 - Exercises Data.xlsx", sheet_name='Exercise 3', index_col=0)

# Generate grid data for 3D surface
TSR = data.index.values.astype(float)
Pitch = data.columns.values.astype(float)
T, P = np.meshgrid(TSR, Pitch)
Z = data.values.T # Power Values

fig = plt.figure(figsize=(9, 7))
ax = fig.add_subplot(projection='3d')
ax.set_xlabel('Tip Speed Ratio')
ax.set_ylabel('Pitch Angle')
ax.set_zlabel('Power Coefficient')

surf = ax.plot_surface(T, P, Z, cmap='inferno', edgecolor='none')

# Change the view
ax.view_init(elev=25, azim=125)

# Customize grid appearance
ax.xaxis._axinfo['grid']['color'] = 'lightgray'
ax.xaxis._axinfo['grid']['linestyle'] = '--'

ax.yaxis._axinfo['grid']['color'] = 'lightgray'
ax.yaxis._axinfo['grid']['linestyle'] = '--'

ax.zaxis._axinfo['grid']['color'] = 'lightgray'
ax.zaxis._axinfo['grid']['linestyle'] = '--'

# Add a color bar
fig.colorbar(surf, ax=ax, shrink=0.5, aspect=10, pad=0.09)

plt.show()