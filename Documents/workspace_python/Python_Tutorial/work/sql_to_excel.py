## From SQL to DataFrame Pandas
import pandas as pd
import pyodbc

sql_conn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};
                            SERVER=qadb2016.ivy-support.com;
                            DATABASE=IVYProduct_CPGDMS;
                            Trusted_Connection=yes')
query = "select * From ADM_Retailer"
df = pd.read_sql(query, sql_conn)

df.head(3)