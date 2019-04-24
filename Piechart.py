import matplotlib.pyplot as plt

# Data to plot
labels = '0 change', '1 change', '2 changes', 'Others'
sizes = [175, 477, 58, 6]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0, 0.1, 0, 0)  # explode 1st slice

# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)
plt.title('Number of changes in corrections using GED')
plt.axis('equal')
plt.show()