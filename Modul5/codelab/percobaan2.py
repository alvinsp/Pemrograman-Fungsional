import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([4, 8, 10])
ypoints = np.array([3, 10, 2])

plt.figure(figsize=(5,5))
plt.plot(xpoints, ypoints, color = 'red')
plt.xlim( [0, 15])
plt.ylim([0,15])
plt.show()