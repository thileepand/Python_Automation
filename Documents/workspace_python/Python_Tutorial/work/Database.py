#!/usr/bin/python2.7

import cgi
import cgitb

cgitb.enable()


print ("Content-type: text/html\n\n")

print ("<h1>Hello Python</h1>")

#!/usr/bin/python

import MySQLdb
# Create instance of FieldStorage
form = cgi.FieldStorage()

# Get data from fields
first_name = form.getvalue('first_name')
last_name  = form.getvalue('last_name')

# Open database connection
db = MySQLdb.connect("localhost","root","123456789","testdrive" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database
sqlstmt = "SELECT * FROM EMPLOYEE WHERE FIRST_NAME = %(first_name)s AND LAST_NAME = %(last_name)s"

try:
   # Execute the SQL command
 cursor.execute(sqlstmt, {'first_name': first_name, 'last_name': last_name})
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   for row in results:
      fname = row[0]
      lname = row[1]
      age = row[2]
      sex = row[3]
      income = row[4]
      # Now print fetched result
            print "fname=%s,lname=%s,age=%d,sex=%s,income=%d" % \ (fname, lname, age, sex, income )
except:
             print "Error: unable to fecth data"

# disconnect from server
db.close()