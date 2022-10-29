import cx_Oracle
import tkinter as tk
from tkinter import ttk
from tkinter import *

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


def insertar_O(nombre, apellido, edad, sexo, carrera, semestre):
    try:
        con = Conexion_O()
        cursor = con.cursor()
        cursor.execute(f"INSERT INTO ESTUDIANTES(NOMBRE,APELLIDO,EDAD,SEXO,CARRERA,SEMESTRE) VALUES('{nombre}','{apellido}','{edad}','{sexo}','{carrera}','{semestre}')")
        con.commit()
        cursor.close()
        print("Insertado")
    except:
        print("Error al insertar")
    
ventana = Tk()
ventana.title("Conexion Oracle")
ventana.geometry("600x480")

boton = tk.Button(ventana, text="Conectar", command=Conexion_O)
boton.place(x=10, y=10)
#boton desconectar
boton2 = tk.Button(ventana, text="Desconectar", command=Cerrar_O)
boton2.place(x=100, y=10)
#boton mostrar
boton3 = tk.Button(ventana, text="Mostrar", command=Mostrar_O)
boton3.place(x=200, y=10)

tabla=ttk.Treeview(ventana, columns=("ID","NOMBRE","APELLIDO","EDAD", "SEXO", "CARRERA", "SEMESTRE"))
tabla.place(x=10, y=50)
#cammbiar tamaño de la tabla 
tabla.column("#0", width=0, stretch=NO)
tabla.column("ID", width=50, stretch=NO)
tabla.column("NOMBRE", width=100, stretch=NO)
tabla.column("APELLIDO", width=100, stretch=NO)
tabla.column("EDAD", width=50, stretch=NO)
tabla.column("SEXO", width=50, stretch=NO)
tabla.column("CARRERA", width=100, stretch=NO)
tabla.column("SEMESTRE", width=100, stretch=NO)

tabla.heading("#0", text="", anchor=CENTER)
tabla.heading("ID", text="ID", anchor=CENTER)
tabla.heading("NOMBRE", text="NOMBRE", anchor=CENTER)
tabla.heading("APELLIDO", text="APELLIDO", anchor=CENTER)
tabla.heading("EDAD", text="EDAD", anchor=CENTER)
tabla.heading("SEXO", text="SEXO", anchor=CENTER)
tabla.heading("CARRERA", text="CARRERA", anchor=CENTER)
tabla.heading("SEMESTRE", text="SEMESTRE", anchor=CENTER)

frame = Frame(ventana)
frame.place(x=10, y=300)
frame.config(bd=1 , relief="sunken")

nombre = Label(frame, text="NOMBRE")
nombre.grid(row=0, column=0)
nombre_g = Entry(frame)
nombre_g.grid(row=0, column=1)

apellido = Label(frame, text="APELLIDO")
apellido.grid(row=0, column=2)
apellido_g = Entry(frame).grid(row=0, column=3)

edad = Label(frame, text="EDAD")
edad.grid(row=0, column=4)
edad_g = Entry(frame).grid(row=0, column=5)

sexo = Label(frame, text="SEXO")
sexo.grid(row=1, column=0)
sexo_g = Entry(frame).grid(row=1, column=1)

carrera = Label(frame, text="CARRERA")
carrera.grid(row=1, column=2)
carrera_g = Entry(frame).grid(row=1, column=3)

semestre = Label(frame, text="SEMESTRE")
semestre.grid(row=1, column=4)
semestre_g = Entry(frame).grid(row=1, column=5)

boton4 = tk.Button(ventana, text="Insertar", command=insertar_O(nombre_g, apellido_g, edad_g, sexo_g, carrera_g, semestre_g))
boton4.place(x=10, y=400)
print(nombre_g)

ventana.mainloop()
