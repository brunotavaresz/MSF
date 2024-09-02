import numpy as np
import matplotlib.pyplot as plt

d = [9.676, 6.355, 4.261, 2.729, 1.862, 1.184, 0.7680, 0.4883, 0.3461, 0.2119]
t = np.arange(0, 50, 5)

plt.semilogy(t, d)

plt.ylim([0, 10])

plt.xlim([0, 50])

plt.show()
