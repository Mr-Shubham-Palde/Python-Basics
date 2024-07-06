#pandas os a fast powerful ,flecible and easy to use open source data analysis and manipulation tool,nuilt on top of the python programming languauge. 

import pandas as pd # importing pandas library
import numpy as np # wheneve you import the pandas import numpy also because it helps a lot

#pandas series : it is a 1-D array holding any type of data


#string
country=['india','afganistan','england',"sa"]
print(pd.Series(country))

'''
o/p:
0         india
1    afganistan
2       england
3            sa
dtype: object

'''

#float
runs=[90,7,119,9]
p=pd.Series(runs)
print(p)
'''
O/P:
0     90
1      7
2    119
3      9
dtype: int64
'''

#custom index:in this what happen is we provide our own index for the given list .lets  see in the example

marks=[23,21,27,25,25]
subjects=["SE","PA","M3","DBMS","CG"]
mark=pd.Series(marks,index=subjects)

print(mark)
'''
O/P:
SE      23
PA      21
M3      27
DBMS    25
CG      25
dtype: int64

'''

# we can also make marks as an index

s=pd.Series(subjects,index=marks)
print(s)
'''
O/P:
23      SE
21      PA
27      M3
25    DBMS
25      CG
dtype: object

'''
#setting a name

shubham=pd.Series(marks,index=subjects,name="Shubham's insem marks")
print(shubham)

