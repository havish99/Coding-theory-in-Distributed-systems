
# coding: utf-8

# In[5]:


import numpy as np 
import matplotlib.pyplot as plt 

## constructing G matrix
temp = []
temp.append(np.ones(32))
temp.append(np.tile([1,0],16))
temp.append(np.tile([1,1,0,0],8))
temp.append(np.tile(np.repeat([1,0],4),4))
temp.append(np.tile(np.repeat([1,0],8),2))
temp.append(np.repeat([1,0],16))

n=32
k=16
t=10

for i in range(1,6):
	for j in range(i+1,6):
		temp.append(temp[i]^temp[j])


# In[2]:


t = [8,10,12,14,16]
count = []
samps = 1e6
for samp in t:
    frac = 0
    for i in range(int(samps)):
        G = np.array(temp)
        choice = np.random.choice(np.arange(1,31),samp,replace=False)
        choice = choice-1
        G[:,choice] = 0
        rk = np.linalg.matrix_rank(G)
        if(rk<k):
            frac = frac+1
    print(frac*1.0/samps)
    count.append(frac)
count = np.array(count)
count1 = count*1.0/samps


# In[9]:

t = np.array(t)
count = np.array(count)
plt.semilogy(t,count)
plt.xlabel("t")
plt.ylabel("frac")
plt.show()

