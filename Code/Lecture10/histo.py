import numpy as np
import matplotlib.pyplot as plt

data = np.random.randn(1000)

plt.figure(figsize=(10, 6))
plt.hist(data, bins=30, alpha=0.7, color='blue', edgecolor='black')
plt.title('Basic Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# Histogram with Density Plot
plt.figure(figsize=(10, 6))
plt.hist(data, bins=30, density=True, alpha=0.7, color='green', edgecolor='black')
plt.title('Histogram with Density Plot')
plt.xlabel('Value')
plt.ylabel('Density')
plt.grid(True)
plt.show()
