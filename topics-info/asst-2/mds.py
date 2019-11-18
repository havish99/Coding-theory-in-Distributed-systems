
# coding: utf-8

# In[1]:


import numpy as np 
import matplotlib.pyplot as plt 
t = [0.9,1.0,1.1,1.2,1.3]


# In[2]:


vals = []
for bound in t:
    count = 0
    for i in range(int(100000)):
        times = np.random.exponential(1,32)
        times.sort()
        if(times[15]>bound):
            count = count+1
    print(count*1.0/100000)
    vals.append(count*1.0/100000)


# In[3]:


plt.semilogy(t, vals)
plt.xlabel('t')
plt.ylabel('cdf')
plt.grid(True)
plt.show()

