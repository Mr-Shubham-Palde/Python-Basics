#dataframe : whenever there is tabular data ,panda called it as dataframe
#rows,column=series(every row is a series)

import numpy as np
import pandas as pd

#creation of dataframe using list :for creation of dataframe we need a 2d list

student_data=[
    [100,80,10],
    [99,100,5],
    [110,100,15]
]
a=pd.DataFrame(student_data,columns=['iq','marks','package'])
print(a)
print('*'*10)

#using dictionary
stud_dict={'iq':[100,90,120,59], 'marks':[100,90,85,78],'package':[10,7,8,5]}
a= pd.DataFrame(stud_dict)
print(a)

#using read csv we will see it on the visual studio code

a=pd.read_csv('/workspaces/Python-Basics/Pandas/Pandas Dataframe/movies.csv')
print(a)

#pandas table ko hi dataframe kehta hai
print('*'*30)
#dataframe attributes and methods

#1.shape: it is used to check dimension (no of rows and no of columns)
print(a.shape)
print('*'*30)
#2.dtypes: it is used to check the datatype
print(a.dtypes)
print('*'*30)

#3.index: it is used to fetch index
print(a.index)
print('*'*30)

#4.column\
print(a.columns)
print('*'*30)
#5.values
print(a.values)
print('*'*30)

#6.head(): it is a function in which top 5 values return karta hai
print(a.head())
print('*'*30)

#7.tail():
print(a.tail())
print('*'*30)

#8.Sample:
print(a.sample(5))
print('*'*30)

#info(): it returns the g=high level information  . it tells how many values are not null and the data type of that. and also tells about the memory used
print(a.info())
print('*'*30)

#describe() : it describe the whole dataset in 8 attributes
print(a.describe())
print('*'*30)

#isnull: it is used to check the null values present in the data or not

print(a.isnull())
print('*'*30)

print(a.isnull().sum())# if we use sum() then it return the total no of null values present in each colums
print('*'*30)
#duplicated(): it check whether there duplicate values are present in the data or not

print(a.duplicated())
print('*'*30)
#and again if we apply the sum function then tit will retrurn the  total no of duplicate values in each column
print(a.duplicated().sum())
print('*'*30)


#rename(): it renames the dataframe column. it does not reflect permanent changes . to do the permanent changes we have to pass inplace=True

