#Import pandas
import pandas as pd

#Assign spreadsheet file name to 'file'
file = 'employee.xlsx'

#Load spreadsheet
x1 = pd.ExcelFile(file)

#Print the sheet name
print(x1.sheet_names)

#Load a sheet into DataFrame by name : df1
df1 = x1.parse('Thileepan')