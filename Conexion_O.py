
import cx_Oracle
try:
    con = cx_Oracle.connect('system/12345@localhost:1521/xe')
    print("Conexion exitosa")
except cx_Oracle.DatabaseError as e:
    print("Error al conectar", e)

cursor = con.cursor()
cursor.execute("select * from ESTUDIANTES")
for row in cursor:
    print(row)

