import cx_Oracle
import tkinter as tk
from tkinter import ttk

def Conexion_O():
    global con
    try:
        con = cx_Oracle.connect('system/12345@localhost:1521/xe')
        print("Conexion exitosa")
    except cx_Oracle.DatabaseError as e:
        print("Error al conectar", e)
    return con

def Cerrar_O():
    try:
        con.close()
        print("Desconectado")
    except:
        print("Error al Desconectar")

def Mostrar_O():
    try:
        con = Conexion_O()
        cursor = con.cursor()
        cursor.execute("select * from ESTUDIANTES")
        for i in cursor:
            tabla.insert("", "end", values=i)
        cursor.close()
    except:
        print("Error al Mostrar")

ventana = tk.Tk()
ventana.title("Conexion Oracle")
ventana.geometry("600x400")

boton = tk.Button(ventana, text="Conectar", command=Conexion_O)
boton.pack()
#boton desconectar
boton2 = tk.Button(ventana, text="Desconectar", command=Cerrar_O)
boton2.pack()
#boton mostrar
boton3 = tk.Button(ventana, text="Mostrar", command=Mostrar_O)
#Tabla
tabla=ttk.Treeview(ventana, columns=("ID","NOMBRE","APELLIDO","EDAD", "SEXO", "CARRERA", "SEMESTRE"))
boton3.pack()
tabla.heading("#0", text="ID")
tabla.heading("#1", text="NOMBRE")
tabla.heading("#2", text="APELLIDO")
tabla.heading("#3", text="EDAD")
tabla.heading("#4", text="SEXO")
tabla.heading("#5", text="CARRERA")
tabla.heading("#6", text="SEMESTRE")
tabla.pack()
#Tamaño de las columnas
tabla.column("#0", width=50)
tabla.column("#1", width=120)
tabla.column("#2", width=120)
tabla.column("#3", width=60)
tabla.column("#4", width=60)
tabla.column("#5", width=110)
tabla.column("#6", width=80)

Etiqueta1 = tk.Label(ventana, text="Nombre")
Etiqueta1.pack()
Entry1 = tk.Entry(ventana)
Entry1.pack()
Etiqueta2 = tk.Label(ventana, text="Apellido")
Etiqueta2.pack()
Entry2 = tk.Entry(ventana)
Entry2.pack()
Etiqueta3 = tk.Label(ventana, text="Edad")
Etiqueta3.pack()
Entry3 = tk.Entry(ventana)
Entry3.pack()
Etiqueta4 = tk.Label(ventana, text="Sexo")
Etiqueta4.pack()
Entry4 = tk.Entry(ventana)
Entry4.pack()
Etiqueta5 = tk.Label(ventana, text="Carrera")
Etiqueta5.pack()
Entry5 = tk.Entry(ventana)
Entry5.pack()
Etiqueta6 = tk.Label(ventana, text="Semestre")
Etiqueta6.pack()
Entry6 = tk.Entry(ventana)
Entry6.pack()

ventana.mainloop()
