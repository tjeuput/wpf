# %% [markdown]
# 
# # The double pendulum problem
# 
# This animation illustrates the double pendulum problem.
# 
# Double pendulum formula translated from the C code at
# http://www.physics.usyd.edu.au/~wheat/dpend_html/solve_dpend.c
# 
# Output generated via `matplotlib.animation.Animation.to_jshtml`.
# 

# %%
import matplotlib.pyplot as plt
import numpy as np

# generate 1000 numbers store in array x
def generate_y():
    x_values = [] # initialize array
    x = 0
    for i in range(1000):
        x += 1
        x_values.append(x)
    return np.array(x_values)

        
def generate_x():
    y_values = []  # Initialize an empty list to store y values
    y = 0.0  # Initialize y with a starting value (e.g., 0.0)

    for i in range(1000):
        y += 0.00004  # Increment y by 0.00004
        y_values.append(y)  # Add the updated y value to the list

    return np.array(y_values)  # Convert the list to a NumPy array

# Call the function to generate the y values
array_x = generate_x()
array_y = generate_y()
print(array_x)
print(array_y)

# Plot
fig, ax = plt.subplots()

ax.plot(array_x, array_y, linewidth=2.0)
#plt.xlabel('X-axis')  # Set X-axis label
#plt.ylabel('Y-axis')  # Set Y-axis label
#plt.title('Plot of X and Y Coordinates')  # Set plot title
#plt.grid(True)  # Add grid lines (optional)


plt.gcf() # get current figure
plt.savefig('Kundenauftrag0.png', dpi=30) # save figure; resolution
plt.show()

# %%



