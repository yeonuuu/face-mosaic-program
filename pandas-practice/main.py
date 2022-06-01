import pandas as pd

data1 = {
    'name' : ['yeonwoo', 'seul', 'hyoeun'],
    'age' : [25, 25, 23],
    'height' : [163, 159, 167]
}

df1 = pd.DataFrame(data1)

print(df1)
print(df1[df1['age'] > 24])

print(df1.describe())


df2 = pd.read_excel('students-info.xlsx')
print(df2)