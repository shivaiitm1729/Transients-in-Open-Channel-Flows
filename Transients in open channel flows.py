# -*- coding: utf-8 -*-
"""
@author: shiva
"""

import numpy as np
import matplotlib.pyplot as plt
h=100
k=7.03
x = np.arange(0,5000+h,h)
t= np.arange(0,2000+k,k)
bc = [5.79]
ic = [5.79]
n= len(x)
m=len(t)
Y= np.zeros((n,m))
Y[0,:]= bc[0]
Y[:,0] = 5.79

V= np.zeros((n,m))
V[:,0] = 1.47
V[0,:]= 1.47

D= np.zeros((n,m))
D[0,:]= 14.8
D[:,0] = 14.8

Sf= np.zeros((n,m))
Sf1= np.zeros((n,m))
Sf[:,0]=0.002295
Sf[0,:]=0.002295
S = 0.00008
N=0.013
# i=50
# j=1
# V[i,j] = V[i+1,j-1]+((9.81/Y[i+1,j-1])**(0.5))*(5.79-Y[i+1,j-1])+9.81*7.03*(S-Sf[i+1,j-1])
# Y[i,j]=Y[i-1,j-1]+(9.81**(0.5))*Y[i-1,j-1]**(0.5)*(S-Sf[i-1,j-1])*7.03+V[i-1,j-1]*((Y[i-1,j-1]/9.81)**0.5)

# print(Y[i,j])
for j in range(1,m):
  for i in range(0,n):
   if ((i==0) and (j>=1)):
           V[i,j] = V[i+1,j-1]+((9.81/Y[i+1,j-1])**(0.5))*(5.79-Y[i+1,j-1])+9.81*7.03*(S-Sf[i+1,j-1])
   if ( (i>0) and (i<=49)):
    Sf[i,j-1]=0.5*(Sf[i+1,j-1]+Sf[i-1,j-1])
    D[i,j-1]= 0.5*(D[i+1,j-1]+D[i-1,j-1])

    Y[i,j] = 0.5*(Y[i-1,j-1]+Y[i+1,j-1])-0.5*(7.03/100)*(D[i,j-1])*(V[i+1,j-1]-V[i-1,j-1]) - 0.5*(7.03/100)*V[i,j-1]*(Y[i+1,j-1]-Y[i-1,j-1])
    V[i,j]= 0.5*(V[i-1,j-1]+V[i+1,j-1])-0.5*(7.03/100)*9.81*(Y[i+1,j-1]-Y[i-1,j-1]) - 0.5*(7.03/100)*V[i,j-1]*(V[i+1,j-1]-V[i-1,j-1])+9.81*7.03*(S-Sf[i,j-1])
    Sf[i,j]= ((N**2)*(V[i,j]**2))/(Y[i,j]**2)
    D[i,j] = Y[i,j]
    # break


  #  break
   if ((i==50) and (j>=1)):
        Y[i,j]=Y[i-1,j-1]+(9.81**(0.5))*Y[i-1,j-1]**(0.5)*(S-Sf[i-1,j-1])*7.03+V[i-1,j-1]*((Y[i-1,j-1]/9.81)**0.5)
  #  break


  # print(Y)
  # print(V)
  # plt.plot(Y)
  # plt.legend(t)


import seaborn as sns
sns.set(style = 'darkgrid')



fig, ax = plt.subplots()
ax.plot(Y[:, 0], label="0 S")
ax.plot(Y[:, 35], label="250 S")
ax.plot(Y[:, 72], label="500 S")
ax.plot(Y[:, 144], label="1000 S")



ax.plot(Y[:, 216], label="1500 S")
ax.plot(Y[:, 284], label="2000 S")
ax.set_title("Lax Diffusion")
ax.set_ylabel("Depth of water")
ax.set_xlabel("distance")
plt.grid(True)
plt.legend()
fig, vx = plt.subplots()
vx.plot(V[:, 0], label="0 S")
vx.plot(V[:, 35], label="250 S")
vx.plot(V[:, 72], label="500 S")

vx.plot(V[:, 144], label="1000 S")


vx.plot(V[:, 216], label="1500 S")
vx.plot(V[:, 284], label="2000 S")
vx.set_title("Lax Diffusion")
vx.set_ylabel("velocity")
vx.set_xlabel("distance")
plt.grid(True)
plt.legend()
# # plt.savefig("shiva_hm.png")
plt.show()

