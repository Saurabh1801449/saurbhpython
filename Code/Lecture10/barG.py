import numpy as np
import matplotlib.pyplot as plt

categories = ['A', 'B', 'C', 'D']
variant1 = [4, 7, 1, 8]
variant2 = [5, 6, 3, 7]

x = np.arange(len(categories))
width = 0.35

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, variant1, width, label='Variant 1')
rects2 = ax.bar(x + width/2, variant2, width, label='Variant 2')

ax.set_xlabel('Categories')
ax.set_ylabel('Scores')
ax.set_title('Scores by category and variant')
ax.set_xticks(x)
ax.set_xticklabels(categories)
ax.legend()

fig.tight_layout()
plt.show()
