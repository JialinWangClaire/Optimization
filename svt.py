import pandas as pd
import numpy as np

# load the dataframe from the pickle file
df = pd.read_pickle('dataframe.pkl')
df.to_excel('test.xlsx')
# print the dataframe
#print(df)

#add a mask
df = df.fillna(0)
df = df.astype(float)
data = df.iloc[:,:]
matrix = data.values
shape = matrix.shape
mask = np.zeros(shape)
for i in range(0,shape[0]):
    for j in range(0,shape[1]):
        if matrix[i,j]>0:
            mask[i,j]=1

from svd_solver import svd_solver
result=svd_solver(matrix,mask)
print('nuclear norm:', np.linalg.norm(result,'nuc'))

from new_rating import new_rating
A=new_rating(matrix,result,3)
rating = []
for each in A:
    rating.append(each[1])
from rescale import rescale_list
B=rescale_list(rating)
for j in range(len(B)):
    A[j][1]=B[j]
print('movie recommendation ranking:',A)
listA=[]
for each in A:
  listA.append(each[0])
print('five movie indice:',listA[:5])
for i in listA[:5]:
    print('movie name:', df.columns.values[i])
print(matrix)
print(result)