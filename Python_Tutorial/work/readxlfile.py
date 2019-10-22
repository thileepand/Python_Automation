# import pandas as pd
#
# xls = pd.ExcelFile("/home/thileepan/read.csv")
# sheetX = xls.parse(2) # 2 is sheet number
# var1 = sheetX["A"]
# print(var1[1])

import xlrd

#open workbook
workbook = xlrd.open_workbook("/home/thileepan/read.csv")

#open sheet by name
#worksheet = workbook.sheet_names("Sheet1")

#open sheet by index
worksheet = workbook.sheet_by_index(0)

#read cell value
worksheet.cell(0, 0).value()

print(worksheet)