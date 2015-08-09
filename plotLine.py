import matplotlib as plt
#X-axis sorted for making the graph clean from crazy lines all over and just a single line

forest_fires = forest_fires.sort(["rain"])
plt.plot(forest_fires["rain"], forest_fires["area"])
plt.show()
