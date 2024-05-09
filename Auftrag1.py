# Import necessary libraries
import matplotlib.pyplot as plt  # For creating plots
import numpy as np  # For numerical operations

# Import specific modules from Matplotlib
from matplotlib.colors import Normalize  # For normalizing colors
from matplotlib.markers import MarkerStyle  # For custom markers
from matplotlib.text import TextPath  # For rendering text as a path
from matplotlib.transforms import Affine2D  # For affine transformations

# Define symbols representing different levels of success
SUCCESS_SYMBOLS = [
    TextPath((0, 0), "☹"),  # Sad face
    TextPath((0, 0), "😒"),  # Neutral face
    TextPath((0, 0), "☺"),  # Happy face
]

# Define the number of data points
N = 25

# Set the seed for reproducibility
np.random.seed(42)

# Generate random data for skills, takeoff angles, thrusts, success, and positions
skills = np.random.uniform(5, 80, size=N) * 0.1 + 5
takeoff_angles = np.random.normal(0, 90, N)
thrusts = np.random.uniform(size=N)
successful = np.random.randint(0, 3, size=N)
positions = np.random.normal(size=(N, 2)) * 5
data = zip(skills, takeoff_angles, thrusts, successful, positions)

print(skills) # print skills
print(takeoff_angles) # 


# Choose a colormap for visualizing thrust values
cmap = plt.colormaps["plasma"]

# Create a figure and axis for the plot
fig, ax = plt.subplots()
fig.suptitle("Throwing success", size=14)  # Set the title of the figure

# Iterate over the data points and plot them
for skill, takeoff, thrust, mood, pos in data:
    # Apply affine transformations to the marker based on skill and takeoff angle
    t = Affine2D().scale(skill).rotate_deg(takeoff)
    # Create a custom marker with the appropriate symbol and transformation
    m = MarkerStyle(SUCCESS_SYMBOLS[mood], transform=t)
    # Plot the data point with the custom marker and color based on thrust
    ax.plot(pos[0], pos[1], marker=m, color=cmap(thrust))

# Add a colorbar to the plot to show the color mapping for thrust
fig.colorbar(plt.cm.ScalarMappable(norm=Normalize(0, 1), cmap=cmap),
             ax=ax, label="Normalized Thrust [a.u.]")

# Set labels for the x and y axes
ax.set_xlabel("X position [m]")
ax.set_ylabel("Y position [m]")

# Save the figure as an image and display it
plt.gcf()  # Get the current figure
plt.savefig('Kundenauftrag1.png', dpi=30)  # Save the figure as an image with custom DPI
plt.show()  # Display the plot
