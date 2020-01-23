import sqlite3

conn = sqlite3.connect("Job_Application.db")

c = conn.cursor()
table_exist = False
# Create table
while table_exist == False:
    c.execute('''CREATE TABLE Job
                (Job Title, Employer, Location, GPA, Wages ''')