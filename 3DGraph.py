from mpl_toolkits import mplot3d
from matplotlib import pyplot as plt

height = [100,110,87,85,65]
weight = [105,123,84,85,78]

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.scatter3D(height,weight)
ax.plot3D(height,weight)
plt.title('3D Graph')
plt.xlabel("Height")
plt.ylabel("Weight")
plt.show()
