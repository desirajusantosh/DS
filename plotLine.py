import matplotlib as plt
#X-axis sorted for making the graph clean from crazy lines all over and just a single line

print(plt.style.available)

plt.style.use('dark_background')
forest_fires = forest_fires.sort(["rain"])
plt.plot(forest_fires["rain"], forest_fires["area"])
# Set the x axis label
plt.xlabel('Amount of Rain')
# Set the y axis label
plt.ylabel('Area')
# Set the title
plt.title("Rain quantity vs fire area")
plt.show()
