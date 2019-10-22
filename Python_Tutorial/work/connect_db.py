import pyodbc

pyodbc.connect("Driver = /home/thileepan/Documents/driver/msodbcsql17_17.0.1.1-1_amd64;"
               "Server = LT-1237\MSSQL2016DEV;"
               "Database = IvyProduct_CPGDMS;"
               "username = sa;"
               "password = envision1!;"
               "Trusted_Connection = yes;")



# import pyodbc
#
# dsn = 'LT-1237\MSSQL2016DEV'
# user = 'sa'
# password = 'envision1!'
# database = 'IvyProduct_CPGDMS'
#
# con_string = 'DSN=%s;UID=%s;PWD=%s;DATABASE=%s;' % (dsn, user, password, database)
# cnxn = pyodbc.connect(con_string)