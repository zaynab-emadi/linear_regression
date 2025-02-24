import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets

# simulating data
n = 1000
x = np.random.normal(3, 5, size=n)
y = -15* x + 20 +np.random.normal(0, 3, size=n)