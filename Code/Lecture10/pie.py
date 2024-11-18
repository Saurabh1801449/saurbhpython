import matplotlib.pyplot as plt

categories = ['A', 'B', 'C', 'D']
values = [10, 24, 36, 40]

labels = ['Category A', 'Category B', 'Category C', 'Category D']
sizes = [15, 30, 45, 10]
explode = (0.1, 0, 0, 0)

plt.figure(figsize=(10, 5))

plt.subplot(1, 3, 1)
plt.bar(categories, values, color='blue')
plt.title('Bar Chart')
plt.xlabel('Categories')
plt.ylabel('Values')

plt.subplot(1, 3, 2)
plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=140)
plt.title('Pie Chart 1')

colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
plt.subplot(1, 3, 3)
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.title('Pie Chart 2')

plt.tight_layout()
plt.show()
