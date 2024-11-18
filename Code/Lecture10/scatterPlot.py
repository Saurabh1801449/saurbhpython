import matplotlib.pyplot as plt

x1 = [1, 2, 3, 4, 5]
y1 = [2, 3, 5, 7, 11]

x2 = [1, 2, 3, 4, 5]
y2 = [1, 4, 6, 8, 10]

plt.scatter(x1, y1, color='r', label='Variant 1')
plt.scatter(x2, y2, color='b', label='Variant 2')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot of Two Variants')
plt.legend()

plt.show()
