from scipy.special import lambertw
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('seaborn-whitegrid')

x = np.arange(0, 36000, 30)
y = 3e6*lambertw(0.0000465*x)/x
plt.plot(x, y.real);
#plt.xlim([0, 100])  
plt.show()
