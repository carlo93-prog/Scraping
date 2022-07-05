import pyodbc


connection='Driver={odbc driver 17 for sql server};Server= .;Database=dblab;Trusted_Connection=yes;'


conn = pyodbc.connect('Driver={odbc driver 17 for sql server};'
                      'Server= .;'
                      'Database=dblab;'
                      'Trusted_Connection=yes;')


cursor = conn.cursor()