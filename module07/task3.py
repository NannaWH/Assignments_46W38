#################################################################################################
# TASK 3: Wind Speed Frequencies ###############################################################
#################################################################################################

## Part 1 - Plotting Histogram
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#Loading the data into python
data_exc3= pd.read_excel("Module 7 - Exercises data.xlsx", sheet_name='Exercise 3')

#Defining Variables
V = data_exc3["Wind Speed (m/s)"]

#Plot Histogram 
num_bins = 20

plt.hist(V, bins=num_bins, edgecolor='black', alpha=0.7)
plt.grid(True, linestyle="--", alpha=0.5)
plt.xlabel("Win Speed")
plt.ylabel("Frequency")
plt.title("Distribution of Wind Data")

# Display the histogram
plt.show()

## Part 2 - Weibull Parameters
from scipy.stats import weibull_min

#Finding the Weibull parameters
shape, loc, scale = weibull_min.fit(V, floc = 0)

#Generate the Weibull Distribution
# Smooth x-axis for PDF
V_sorted = np.linspace(V.min(), V.max(), num_bins)
pdf = weibull_min.pdf(V_sorted,shape,scale=scale)

#Plot Histogram with Weibull Distribution
fig, ax1 = plt.subplots()

ax1.hist(V, bins=num_bins, edgecolor='black', alpha=0.7)
ax1.grid(True, linestyle="--", alpha=0.5)
ax1.set_xlabel("Wind Speed")
ax1.set_ylabel("Frequency")
ax1.set_title("Distribution of Wind Data")

ax2 = ax1.twinx()
ax2.set_ylabel('Probability Density')
ax2.plot(V_sorted, pdf, color='r', label='Weibull PDF')

# Display the histogram
plt.legend()
plt.show()

