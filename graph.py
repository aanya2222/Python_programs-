from matplotlib import pyplot as plt
names = ['Neeta','Chetana','sakshi']
marks = [85,83,80]
plt.subplot(2,3,1)
plt.bar(names,marks,color='red')
plt.subplot(2,3,2)
plt.scatter(names,marks,color='green')
plt.subplot(2,3,3)
plt.plot(names,marks)
plt.subplot(2,3,4)
plt.bar(names,marks)
plt.subplot(2,3,5)
plt.scatter(names,marks)
plt.subplot(2,3,6)
plt.plot(names,marks)
plt.suptitle("Plotting Graphs in Python")
plt.show()
