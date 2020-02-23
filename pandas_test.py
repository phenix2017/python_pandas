simport pandas as pd


"""
This will not work,
since the length of the arrary of the "col1" and "col2"
are different
"""
# d = {"col1": [1,2,2], "col2":[2,3]}
# df = pd.DataFrame(data=d)

d = {"col1": [1, 2], "col2": [2, 3]}
df = pd.DataFrame(data=d)

df.dtypes
import numpy as np
df2 = pd.DataFrame(data=d,dtype=np.int8)
df2.dtypes

""""Construtcting DataFrame from numpyu array""
"""
# Each element should be equal length with the size of the columns 
data = np.array([[1, 2,3], [3,4,5]])

pd.DataFrame(data, columns=['a', 'b', 'c'])

# Attributes 
# T, at, attrs 

