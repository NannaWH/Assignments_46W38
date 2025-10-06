################################################################################################
##### TASK 1: Energy Generation in EU Plot  ###################################################
################################################################################################

import matplotlib.pyplot as plt

# Defining the figure
fig = plt.figure(figsize=(9,7))
ax = fig.add_subplot()
#ax.set_xlabel('Energy Source')
#ax.set_ylabel('Percentage of Total Energy Generation')

#Generate the data for the for the chart
pie_labels = ['Crude Oil', 'Natural Gas', 'Renewable Energy', 'Solid Fuels', 'Nuclear Energy']
pie_sizes = [37.7, 20.4, 19.5, 10.6, 11.8]
pie_colors = ['grey', 'lightblue' ,'lightgreen', 'orange', 'red']

# Create the pie chart
ax.pie(pie_sizes, labels=pie_labels, colors=pie_colors, autopct='%1.1f%%')

#Show the pie chart
plt.show()