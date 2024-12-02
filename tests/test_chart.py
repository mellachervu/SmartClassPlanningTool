import matplotlib.pyplot as plt

labels = 'Passed', 'Failed'
sizes = [6, 4]  # Example values
colors = ['lightblue', 'salmon']
explode = (0.1, 0)  # explode the 1st slice (Passed)

plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=90)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Test Case Results Distribution')
plt.show()

# Data for the bar chart
defect_severity = ['High', 'Medium', 'Low']
defect_counts = [2, 1, 1]  # Adjust based on your actual defect counts

# Create bar chart
plt.figure(figsize=(8, 5))
plt.bar(defect_severity, defect_counts, color=['#FF6347', '#FFD700'])
plt.xlabel('Defect Severity')
plt.ylabel('Number of Defects')
plt.title('Defect Density')
plt.xticks(rotation=45)
plt.savefig('defect_density_chart.png')  # Save the chart as a PNG file
plt.show()
