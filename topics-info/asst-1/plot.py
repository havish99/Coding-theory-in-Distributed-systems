import matplotlib.pyplot as plt 
y = [2.9e-05,0.001177,0.014467,0.099879,0.512809]
x = [8,10,12,14,16]
plt.semilogy(x,y)
plt.xlabel("t")
plt.ylabel("fraction")
plt.show()