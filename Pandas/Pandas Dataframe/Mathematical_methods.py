import numpy as np
import pandas as pd

# we will create a dataframe using a dictionary

a={'iq':[100,80,79],
   'marks':[98,87,84],
   'package':[7,5,4]}
students=pd.DataFrame(a)
print(students)
print('*'*30)

#sum(): if i apply the sum() function then it will return addition of number in each column
print(students.sum())
#if we want the addition of rows then there is a axis attribute , if axis=1 give me row wise addition
print('*'*30)
print(students.sum(axis=1))
print('*'*30)

#mean(): it gives us the mean of all the columns
print(students.mean())
print('*'*30)
#in this case also if we apply the axis attribute =1 then it will return the row wise mean
print(students.mean(axis=1))
print('*'*30)

#min: it returns the minimum values form each colum of the dataframe
print(students.min())
print('*'*30)
#in this case also if we apply the axis=1 then we will also get the row wise minimum values
print(students.min(axis=1))
print('*'*30)



