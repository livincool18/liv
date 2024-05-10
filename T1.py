import matplotlib.pyplot as plt
import numpy as np
np.random.seed(0)
ages=np.random.randint(18,60,size=90)
plt.hist(ages,bins=9,edgecolor="blue")
plt.xlabel("Ages")
plt.ylabel("Frequency")
plt.title("Age Distribution")
plt.show()


