import matplotlib.pyplot as plt
import numpy as np

# creating data set
data = {"Zement" : 30, "Warnweste": 10, "Rote Ampel":60, "Rasen": 90 }

suchbegriff = list(data.keys())
hauefigkeit = list(data.values())

fig = plt.figure(figsize=(8,5))

# color
color_bars = ['tab:red', 'tab:blue', 'tab:red','tab:orange' ]

# creating the bar plot x and y and size
plt.bar(suchbegriff, hauefigkeit, color=color_bars, width=0.4)

# Set y-axis lower limit to 0
plt.ylim(0, max(hauefigkeit) + 10)

# labeling x and y
plt.xlabel("Suchbegriffe")
plt.ylabel("Häufigkeit")
plt.title("Lfd Suchbegriff Häufigkeit")
plt.gcf()
plt.savefig('Auftrag4.png', dpi=30)
plt.show()
