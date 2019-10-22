import pandas as pd
from xlrd import open_workbook

x_file = '/home/nadmin/Documents/work/product_template.xls'
y_file = '/home/nadmin/Documents/work/customer_template.xls'

#pd.read_excel(newfile)

if y_file.split('.')[-1] == x_file.split('.')[-1]:
    print ("Invalid format")

if not y_file.split('.')[0].split('/')[-1] == x_file.split('.')[0].split('/')[-1]:
    print ("Invalid filename")

src_file = open_workbook(x_file)
test_file = open_workbook(y_file)

src_sheets = src_file.sheets()
test_sheets = test_file.sheets()

def check_cell_type(x_tuple):
    #print(x_tuple)
    if type(x_tuple[0].value) != type(x_tuple[1].value):
        return False
    return True

#Sheet Names checking in the same order
for i in range(0,len(src_sheets)):
    if not src_sheets[i].name == test_sheets[i].name:
        for x in zip(src_sheets[i].row(0),test_sheets[i].row(0)):
            if x[0].value != x[1].value:
                raise('Columns are Not matching')
        for y in zip(src_sheets[i].row(1), test_sheets[i].row(1)):
            if not check_cell_type(y):
                raise('Data Types Not Matching')

    else:
        raise('Sheet are not matching')



#
# # Create a Pandas dataframe from the data.sample/newxls.py:10sample/newxls.py:10
# df = pd.DataFrame({'Data': [10, 20, 30, 20, 15, 30, 45]})
#
# # Create a Pandas Excel writer using XlsxWriter as the engine.
# writer = pd.ExcelWriter('pandas_simple.xlsx', engine='xlsxwriter')
#
# # Convert the dataframe to an XlsxWriter Excel object.
# df.to_excel(writer, sheet_name='Sheet1')
#
# # Close the Pandas Excel writer and output the Excel file.
# writer.save()
#
# print(df)










