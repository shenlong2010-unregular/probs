import pandas as pd

filename = 'https://sololearn.com/uploads/files/one.csv'
column_name = 'a'
df = pd.read_csv(filename)
print(df)
print(df[column_name].values)