import matplotlib as plt

month = [1,1,2,3,4,4,6,6,7,7,8,11,11,12]
temperature = [11,22,21,18,31,24,29,22,9,14,21,11,25]

plt.scatter(month, temperature)
plt.xlabel('month')
plt.xlabel('temperature')
plt.title('Temperature variation over the months')
plt.show()
