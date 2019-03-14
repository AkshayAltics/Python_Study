'''
Created on 08-Mar-2019

@author: Admin
'''
import numpy as np
#from skimage import io


a=np.zeros(3)
print(type(a[0]))
print(a)
z=np.zeros(10)
print(z)
z=np.linspace(2,10,5)
print(z)
blist=[[1,2,3,4,5,6],[11,22,33,44,55,66]]
z=np.array([blist])
print(z)
np.random.seed(0)
z1=np.random.randint(10,size=3)
print("z1 is ",z1)
'''
photo=io.imread("asas.jpg")
print(type(photo))
'''
b=[4,3,1]
print("b is ",b)
print("multiplication of 2 array z1*b",b*z1)
print(b**z1)
print(b@z1)