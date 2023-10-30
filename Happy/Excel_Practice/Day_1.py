import pandas as pd

excel_file = 'Details.xlsx'
l= []
#read excel file into pandas data frame
df = pd.read_excel(excel_file)

for index,row in df.iterrows():
    for column in df.columns:
        key = column
        value = row[column]
        # print("key=", key,"value=",value)
        l.append([key,value])


print(l)