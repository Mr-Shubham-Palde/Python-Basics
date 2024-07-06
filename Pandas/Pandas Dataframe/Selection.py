import numpy as np
import pandas as pd


#selecting a column from a dataframe
a=pd.read_csv('movies.csv')
print(a)
print('*'*30)
# to select a single column from a dataframe, you just need to do is provide the column name in the square bracket. let's see it below
print(a['title_x'])
print('*'*30)

# to select a multiple column from a dataframe you just need to do is seperate one coumn name from another using comma(,) note that it is ppossible only if you provide  list in the square brackets.
print(a[['title_x','actors']])
print('*'*30)
# if you are collecting single colymn it is series and if you are collectiong multiple columns then it is dataframe

#Selecting rows from a dataframe
#1.iloc :searches using the index positons
#single row:
print(a.iloc[0])# it gives all the information present at row 1
print('*'*30)
#multiple rows: it works like a slicing in python
print(a.iloc[0:5])

#loc: it searches using index labels

print(a.loc[0])

#selecting both rows and columns
print(a.iloc[0:3,0:3].shape)