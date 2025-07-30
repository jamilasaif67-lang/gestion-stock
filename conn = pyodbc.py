conn = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\chemin\vers\ma_base.accdb;')
cursor = conn.cursor()
cursor.execute("SELECT * FROM MaTable")

for row in cursor.fetchall():
    print(row)
