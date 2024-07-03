import pandas as pd
import numpy as np
#Series Attributes
marks=[29,10,23,45,33]
m=pd.Series(marks,name="shubam's marks")

print(m)

#1.size: it exactly tells us how many items are present int the given series
print(m.size)

#2.dtype:it basically tells us about the datatype of the elements present in the series
print(m.dtype)

#3. name: it gives the name which we have use to describe about who's or anyone's thing we have store in the series
print(m.name)

#4.is_unique:it checks whether each item in the series is unique or not if yes ,it return true else it returns false
print(m.is_unique)

#5.index: it is used to generate index generated values
print(m.index)

#values:it is used to get all values from the series
# output is always a list
print(m.values)



## Series using read_csv