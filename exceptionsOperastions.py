import xlsxwriter
import sqlite3
from sqlite3.dbapi2 import Cursor,connect

    
wb = xlsxwriter.Workbook("hllbr1.xlsx")
page = wb.add_worksheet("Join_Operations")
connection = sqlite3.connect("chinook.db")
   
def joinOperation():

    cursor = connection.execute("SELECT albums.Title, artists.Name FROM artists INNER JOIN albums on artists.ArtistId = albums.ArtistId")
    for data,row in enumerate(cursor):
        page.write(data,0,row[0])
        page.write(data,1,row[1])

def defaulOperation():
    page1 = wb.add_worksheet("Default_Operations")
    page1.write(0,0,"Default Operation Passed")

try:
    joinOperation()
    defaulOperation()
except:
    
    page2 = wb.add_worksheet("exception results")
    page2.write(0,0,"Operation Failed")

wb.close()
