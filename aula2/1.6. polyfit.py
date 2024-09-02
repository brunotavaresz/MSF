import matplotlib.pyplot as plt
import numpy as np

D = np.array([0.00, 0.735, 1.1363, 1.739, 2.805,
              3.814, 4.458, 4.955, 5.666, 6.329])
T = np.arange(0, 10, 1)

aprox = np.polyfit(T, D, 1)
print(aprox)
