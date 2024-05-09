import matplotlib.pyplot as plt

import numpy as np
from numpy import cos

# create data
def generate_y():
    arr_y = []
    y = 0
    arr_x = np.linspace(0,10,100)
    for x in arr_x:
        y = 2*np.cos(x)
        arr_y.append(y)
    print(arr_x)    
    return np.array(arr_y)
#array_list = [i for i in range(1, 11)] creates a list where each element is the value of i

arr_y = generate_y()
print(arr_y)

plt.plot(arr_y)

# create limit
# Set y-axis lower limit to 0
plt.ylim(-4, 4)
plt.grid(True)
plt.gcf()
plt.savefig('Kundenauftrag5.png', dpi=30)
plt.show()


