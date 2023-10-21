
import pandas as pd


excel_file = 'Details.xlsx'

# Read the Excel file into a pandas DataFrame
df = pd.read_excel(excel_file)
# print(df)

# Iterate through the DataFrame and print key-value pairs
for index, row in df.iterrows():
    for column in df.columns:
        key = column
        value = row[column]
        print(f"{key}: {value}")



#
# excel="Details.xlsx"
#
# df = pd.read_excel(excel)
# # print(df)
# l=[]
# for index,row in df.iterrows():
#     for colunm in df.columns:
#         key = colunm
#         value = row[colunm]
#         # print(f"{key}:{value}")
#         l.append([key,value])
#
#
# print(l)


