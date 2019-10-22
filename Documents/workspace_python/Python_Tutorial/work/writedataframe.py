import pandas as pd
import

#Specify a writer
write = pd.ExcelWriter('employee.xlsx', engine='xlsxwriter')

#Write a DataFrame to you file
yourData.to_excel(writer, 'Sheet1')

#Save the result
writer.save