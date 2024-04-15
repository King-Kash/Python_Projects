import pandas as pd

df = pd.read_csv('pokemon_data.csv')

print(df.head(3))

##Read Headers
print(df.columns)

##Read Each Column
print(df[['Name', 'Type 1', 'HP']])

## Read Each Row
print(df.iloc[0:4]) #rows 0, 4
for index, row in df.iterrows():
    print(index, row['Name'])

## Print Everything of Certain Type
print(df.loc[df['Type 1'] == 'Fire'])

## Read a Specific location (R, C)
print(df.iloc[2,1])

##Gives all the statistics information like mean and standard deviation
df.describe()

##sort by first param, second param is ascending or deceinding order
df.sort_values('Name', ascending=False)

##sorty by multiple parameters, 1 = true, 0 = false
df.sort_values(['Type 1', 'HP'], ascending=[1, 0])

##find totoal of various columns
df['Total'] = df['HP'] + df['Attacks'] + df['Speed']
df.drop(columns=['Total'])
##adding the columns 4,9; axis 1 = column, axis 0 = row
df['Total'] = df.iloc[:, 4:9].sum(axis = 1)

##move the columns around
cols = list(df.columns.values)
df = df[cols[0:4] + [cols[-1]] + cols[4:12]]