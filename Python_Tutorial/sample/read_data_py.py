import csv
def getCSVData(fileName):
    # create an empty list to store rows
    rows = []
    # open the CSV file
    dataFile = open(fileName, "r")
    # create a CSV Reader from CSV file
    reader = csv.reader(dataFile)
    # skip the headers
    next(reader)
    # add rows from reader to list
    for row in reader:
        rows.append(row)
    return rows

from future import print_function
from os.path import join, dirname, abspath, isfile
from collections import Counter
import xlrd
from xlrd.sheet import ctype_text
from sample import tes

def get_excel_sheet_object(fname, idx=0):
    if not isfile(fname):
        print ('File doesn't exist: ', fname)
            # Open the workbook and 1st sheet
    xl_workbook = xlrd.open_workbook(fname)
    xl_sheet = xl_workbook.sheet_by_index(0)
    print (40 * '-' + 'nRetrieved worksheet: %s' % xl_sheet.name)

return xl_sheetsdf