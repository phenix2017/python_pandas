# 10 minutes to pandas 
import numpy as np
import pandas as pd
# Object creation 

# Create, Delete, Retrieve
## Create from scrach and other object
# Data type: 1.series 2. DataFrame
s = pd.Series([1,3,4, np.nan,6])

# s = pd.DataFrame(data=[[1,2]],columns=["1","2"])

dates = pd.date_range("20130101", periods=6)# used for the following

df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
# create DataFrame using dictionalry: 1. 
# all the elements are scale, we have to specify the index
# If we specify the index in any case, the index should be the same length as the rows
# data_dict = {"A":1,
#              "B":pd.Timestamp("20130102")}
# df = pd.DataFrame(data_dict, index=[0])


# View data (Retreive information)
df.head()
df.tail(2)
df.index

df.to_numpy()
df.describe()
df.T
df.sort_index(axis=1, ascending=True)
df.sort_values(by="B", ascending=False)



"""" Selection """
df["A"] # selcting a single column, which yields a series 
# df.A == df["A"]
df[0:2] # index [)
df['20130102':'20130104'] # index []


df.index = [str(i) for i in range(0,6)]

df[0:3]
df["0":"3"]

# Selection by label 


df.loc["0"]
# Selecting on a multi-axis by label
df.loc[:,['A','B']]
df.loc[:]
# Showing label slicing, both endpionts are included
df.loc["0":"2",['A','B']]


# df.loc[0:2] cannot use index 
# df[0:2]
# df.iloc[0:2]

# Fro getting a scalar value 
df.loc["0","A"]

df.at["0","A"]

# Slection by position 

df.iloc[3] # slect via the position of the passed integers

df.iloc[2:4,0:3] # acting simular the numpy/pyton style

# For slicing rows explicitly 
df.iloc[1:3,:]
df.iat[1,1]


# Slecting values from a dataframe where a boolean condition is met

df[df>0] # False: NaN, True: selected

df2 = df.copy()
df2.index = dates

df2["E"]  = list("ABCDEF")

# Setting 

# Setting a new column automatically aligns the data by the index
s1 = pd.Series([1,2,3,1,2,3], index=pd.date_range("20200102",periods=6))

s1
df2["F"] = s1
df2["F"]

# Missing data
df2.reindex(index=dates[0:4])
df2.reindex(columns=list(df.columns) + ["E"])
df2["A"]


df3 = df2.fillna(value=5)
df.dropna(how="all")
df.dropna(how="any")
pd.isna(df)

# Operations 
df.mean()
df.mean(1) # axis
# df.mean(axis=1)
# df.mean(axis=0)

# Operating with objects that have different dimentionality and need alignment
# In addition, padans automatically broadcosts along the specified dimension
s = pd.Series([1,2,4, np.nan, 7,8], index=dates).shift(2)
df2.sub(s,axis="index")



# Apply
df = df.iloc[0:5,0:3]
df.apply(np.cumsum)


# Histogrammming 
s = pd.Series(
    np.random.randint(0,7,size=10)
    )
type(s.value_counts())
s.value_counts()

# String methods 


df = pd.DataFrame(np.random.randn(10,4))
# Break it into pieces 
pieces = [df[:3], df[3:7], df[7:]]



# Join
left = pd.DataFrame({'key': ['foo', 'foo'], 'lval': [1, 2]})

right = pd.DataFrame({'key': ['foo', 'foo'], 'rval': [4, 5]})

pd.merge(left,right,on="key")

# Grouping 

df = pd.DataFrame({'A': ['foo', 'bar', 'foo', 'bar',
                         'foo', 'bar', 'foo', 'foo'],
                   'B': ['one', 'one', 'two', 'three',
                         'two', 'two', 'one', 'three'],
                   'C': np.random.randn(8),
                   'D': np.random.randn(8)})


df.groupby("A").sum()
df.groupby("B").sum()

df.groupby(["A","B"]).sum()


# Reshaping 

