import pandas as pd
import numpy as np
 
#Series and DataFrame are the two main data structures in pandas.
#A Series is a one-dimensional array-like object that can hold any data type
 
s=pd.Series()
print(s)
 
data=np.array(['a','b','c','d'])
s=pd.Series(data)
print(s)
 
print(s[1])
 
data2 = np.array(['g','e','e','k','s','f', 'o','r','g','e','e','k','s'])
ser = pd.Series(data2,index=[10,11,12,13,14,15,16,17,18,19,20,21,22])
 
print(ser[16])
 
series=pd.Series(df['Name'])
data=series.head(10)
print(data)
 
print(data.loc[3:6])
print(data.iloc[3:6])
 
ser1 = pd.Series([1, 2, 3], index=['A', 'B', 'C'])
ser2 = pd.Series([4, 5, 6], index=['A', 'B', 'C'])
 
print(ser1.add(ser2))
print(ser1.mul(ser2))
print(ser1.mean())
 
print(ser1.astype(float))
 
# A DataFrame is a two-dimensional table of data with rows and columns.
d=pd.DataFrame()
print(d)
 
lst=['car','bus','truck','plane','ship']
d=pd.DataFrame(lst)
print(d)
 
df=pd.read_csv("data.csv")
print(df.head())
print(df.info())
 
print(df.isnull().sum())
 
df.fillna(0, inplace=True)
print(df.isnull().sum())
print(df.head())
 
age=df['age']
print(age)
 
print(df[df['age']>25]) #returns the rows where the age is greater than 25
print(df['age']>25) # returns a boolean series
 
df['total']=df['a']+df['b']
print(df.head())
 
print(df.describe()) # gives the statistical summary of the numerical columns in the DataFrame
print(df.describe())
 
 
df=pd.read_csv("nba.csv")
print(df.head())
 
print(df[['Name', 'Team']].head())
 
sorted_data=df.sort_values(by='Age',ascending=False)
print(sorted_data.head())
 
print(df.tail(3))
 
percentiles = [.20, .40, .60, .80]
include = ['object', 'float', 'int']
desc=df.describe(percentiles=percentiles,include=include)
print(desc)
 
print(df['Name'].describe) # gives the statistical summary of the 'Name' column in the DataFrame.
 
df=pd.read_csv("nba.csv")
print(df.head())
 
print(df[['Name','Team']])
 
df['Experience']=1
print(df.head())
 
df.drop('Experience', axis=1, inplace=True)
print(df.head())
 
# #Dealing with Rows in DataFrames
# first = df.loc["Avery Bradley"]
# print(first)
 
#Adding a new row to the DataFrame:
new_row = {
    'Name': 'Geeks',
    'Team': 'Boston',
    'Number': 3,
    'Position': 'PG',
    'Age': 33,
    'Height': '6-2',
    'Weight': 189,
    'College': 'MIT',
    'Salary': 99999
}
 
new_row2 = {
    'Name': 'Deep',
    'Team': 'Boston',
    'Number': 5,
    'Position': 'PG',
    'Age': 21,
    'Height': '6-0',
    'Weight': 179,
    'College': 'SUAS',
    'Salary': 50000
}
 
df=pd.concat([df,pd.DataFrame([new_row])], ignore_index=True)
print(df.tail())
 
new_row_df=pd.DataFrame([new_row2])
print(new_row_df)
 
df=pd.concat([df,new_row_df], ignore_index=True)
print(df.tail())
 
df.drop(458,inplace=True)
print(df.tail())
 
Accessing data using index based columns
 
df=pd.read_csv("data.csv",index_col='name')
print(df.head(10))
 
print(df.loc['Swapndeep'])
print(df.loc['John':'Swapndeep'])
 
df.drop("Riya",inplace=True)
print(df.head())
 
 
 
