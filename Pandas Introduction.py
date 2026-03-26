Pandas Series
"""

#Pandas Series

# import pandas as pd
# a=[1,2,3,4,5]
# my=pd.Series(a)
# print(my)
# print(my[0])

#Create Labels

# import pandas as pd
# a=[1,2,3]
# myvar=pd.Series(a,index=["x","y","z"])
# print(myvar)
# print(myvar["x"])


#Key/Value Objects as Series

# import pandas as pd
# calories= {"Day1": 200,"Day2": 250,"Day3":300}
# myvar=pd.Series(calories)
# print(myvar)


# import pandas as pd
# calories={"Day1": 200, "Day2": 300, "Day3": 400, "Day4": 500}
# myvar=pd.Series(calories,index=["Day1","Day2"])
# print(myvar)

"""Data Frames"""

# DataFrames

# import pandas as pd
# data={
#     "calories":[100,200,300,400,500],
#     "duration":[10,20,30,40,50]
# }
# myvar=pd.DataFrame(data)
# print(myvar)
# print(myvar.loc[[0,1]])


# Named Indexes in DataFrame

# import pandas as pd
# data={
#     "calories":[100,200,300,400,500],
#     "Duration":[10,20,30,40,50]
# }
# df=pd.DataFrame(data,index=["Day1","Day2","Day3","Day4","Day5"])
# print(df)
# print(df.loc["Day1"])
# print(df.loc[["Day1","Day2"]])

import pandas as pd
data={
    "calories":[100,200,300,400,500],
    "Duration":[10,20,30,40,50]
}
df=pd.DataFrame(data,index=["Day1","Day2","Day3","Day4","Day5"])
print(df)
print(df.loc["Day1"])
print(df.loc[["Day1","Day2"]])

# from google.colab import files
# uploaded = files.upload()
import pandas as pd
df = pd.read_csv('data.csv')
# print(df.to_string())
print(df)
print(pd.options.display.max_rows)

import pandas as pd
pd.options.display.max_rows=999
df=pd.read_csv('data.csv')
print(df)

"""JSON"""

from google.colab import files
uploaded = files.upload()
import pandas as pd
df=pd.read_json("data.js")
print(df.to_string())

import pandas as pd

data = {
  "Duration":{
    "0":60,
    "1":60,
    "2":60,
    "3":45,
    "4":45,
    "5":60
  },
  "Pulse":{
    "0":110,
    "1":117,
    "2":103,
    "3":109,
    "4":117,
    "5":102
  },
  "Maxpulse":{
    "0":130,
    "1":145,
    "2":135,
    "3":175,
    "4":148,
    "5":127
  },
  "Calories":{
    "0":409,
    "1":479,
    "2":340,
    "3":282,
    "4":406,
    "5":300
  }
}

df = pd.DataFrame(data)

print(df)
