import cx_Oracle
import tkinter as tk
from tkinter import ttk
from tkinter import *

def Conexion_O(): #Conexion a la base de datos
    global con
    try:
        con = cx_Oracle.connect('system/12345@localhost:1521/xe')
        Terminal("Conexion exitosa")
    except:
        Terminal("Error al conectar")
    return con

def Cerrar_O(): #Cerrar la conexion
    try:
        con.close()
        Terminal("Conexion cerrada")
    except:
        Terminal("Error al cerrar")

def Mostrar_O(): #Mostrar datos
    Actualizar_T()
    try:
        cursor = con.cursor()
        cursor.execute("select * from ESTUDIANTES") #Consulta
        for i in cursor:
            tabla.insert("", "end", values=i) 
        cursor.close()
    except:
        Terminal("Error al mostrar datos")

def Insertar_O(): #Insertar datos
    try:
        cursor = con.cursor()
        cursor.execute(f"INSERT INTO ESTUDIANTES(NOMBRE,APELLIDO,EDAD,SEXO,CARRERA,SEMESTRE) VALUES('{Nombre.get()}','{Apellido.get()}','{Edad.get()}','{Sexo.get()}','{Carrera.get()}','{Semestre.get()}')")
        con.commit()
        cursor.close()
        Actualizar_T()
        Mostrar_O()
        Terminal("Datos insertados correctamente")
    except:
        Terminal("Error al insertar datos")   

def Eliminar_O(): #Eliminar datos
    try:
        cursor = con.cursor()
        cursor.execute(f"DELETE FROM ESTUDIANTES WHERE ID = '{ID.get()}'")
        con.commit()
        Actualizar_T()
        Mostrar_O()
        cursor.close()
        Terminal("Datos eliminados correctamente")
    except:
        Terminal("Error al eliminar datos")

def Actualizar_T(): #Actualizar tabla/Eliminar datos en la tabla
    for i in tabla.get_children():
        tabla.delete(i)

def Terminal(Msg):
    for widget in Frame2.winfo_children(): #Limpiar el frame2
        widget.destroy()
    Label_T = tk.Label(Frame2, text="# "*5+ Msg +" #"*5).grid(row=0, column=0) #Label Terminal 

ventana = Tk()
ventana.title("BD Oracle")
ventana.geometry("600x500")
ventana.iconbitmap("icono.ico") #Icono

Btn_Conectar = tk.Button(ventana, text="Conectar", command=Conexion_O) #Boton conectar
Btn_Conectar.place(x=10, y=10)
Btn_Desconectar = tk.Button(ventana, text="Desconectar", command=Cerrar_O) #Boton desconectar
Btn_Desconectar.place(x=100, y=10)
Btn_Mostrar = tk.Button(ventana, text="Mostrar Datos", command=Mostrar_O) #Boton mostrar
Btn_Mostrar.place(x=200, y=10)
tabla=ttk.Treeview(ventana, columns=("ID","NOMBRE","APELLIDO","EDAD", "SEXO", "CARRERA", "SEMESTRE")) #Tabla 
tabla.place(x=10, y=50)
tabla.column("#0", width=0, stretch=NO) #Columnas
tabla.column("ID", width=50, stretch=NO)
tabla.column("NOMBRE", width=100, stretch=NO)
tabla.column("APELLIDO", width=100, stretch=NO)
tabla.column("EDAD", width=50, stretch=NO)
tabla.column("SEXO", width=50, stretch=NO)
tabla.column("CARRERA", width=100, stretch=NO)
tabla.column("SEMESTRE", width=100, stretch=NO)
tabla.heading("#0", text="", anchor=CENTER) #Encabezados
tabla.heading("ID", text="ID", anchor=CENTER)
tabla.heading("NOMBRE", text="NOMBRE", anchor=CENTER)
tabla.heading("APELLIDO", text="APELLIDO", anchor=CENTER)
tabla.heading("EDAD", text="EDAD", anchor=CENTER)
tabla.heading("SEXO", text="SEXO", anchor=CENTER)
tabla.heading("CARRERA", text="CARRERA", anchor=CENTER)
tabla.heading("SEMESTRE", text="SEMESTRE", anchor=CENTER)

frame = Frame(ventana) #Frame
frame = LabelFrame(ventana, text="Insertar Datos") 
frame.place(x=10, y=290, width=560, height=70)
frame.config(bd=1 , relief="sunken")
tk.Label(frame, text="Nombre: ").grid(row=0, column=0) #Label/Entry Nombre

Nombre = tk.StringVar()
Nombre_g = tk.Entry(frame, textvariable=Nombre).grid(row=0, column=1)
tk.Label(frame, text="Apellido: ").grid(row=0, column=2) #Label/Entry Apellido

Apellido = tk.StringVar()
Apellido_g = tk.Entry(frame, textvariable=Apellido).grid(row=0, column=3)
tk.Label(frame, text="Edad: ").grid(row=0, column=4) #Label/Entry Edad

Edad = tk.IntVar()
Edad_g = tk.Entry(frame, textvariable=Edad).grid(row=0, column=5)

tk.Label(frame, text="Sexo: ").grid(row=1, column=0) #Label/Combobox Sexo
Sexo = tk.StringVar()
Sexo_g = ttk.Combobox(frame, textvariable=Sexo, state="readonly")
Sexo_g["values"] = ("M", "F")
Sexo_g.grid(row=1, column=1)
Sexo_g.config(width=17)

tk.Label(frame, text="Carrera: ").grid(row=1, column=2) #Label/Entry Carrera
Carrera = tk.StringVar()
Carrera_g = ttk.Combobox(frame, textvariable=Carrera, state="readonly")
Carrera_g["values"] = ("Ing.Sistemas","Ing.Contabilidad","Ing.Civil","Ing.Industrial","Medicina","Gastronomia","Derecho","Psicologia","Arquitectura")
Carrera_g.grid(row=1, column=3)
Carrera_g.config(width=17)

tk.Label(frame, text="Semestre: ").grid(row=1, column=4) #Label/Combobox Semestre
Semestre = tk.IntVar()
Semestre_g = ttk.Combobox(frame, textvariable=Semestre, state="readonly")
Semestre_g["values"] = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10")
Semestre_g.grid(row=1, column=5)
Semestre_g.config(width=17)
Semestre_g.current(0)

frame1 = Frame(ventana) #Frame
frame1 = LabelFrame(ventana, text="Eliminar")
frame1.place(x=10, y=360, width=560, height=45)
frame1.config(bd=1 , relief="sunken")

tk.Label(frame1, text="ID: ").grid(row=0, column=0) #Label/Entry ID
ID = tk.IntVar()
ID_g = tk.Entry(frame1, textvariable=ID).grid(row=0, column=1)

Btn_Insertar = tk.Button(ventana, text="Insertar Datos", command=Insertar_O).place(x=10, y=410) #Boton insertar
Btn_Eliminar = tk.Button(ventana, text="Eliminar", command=Eliminar_O).place(x=100, y=410) #Boton eliminar

Frame2 = Frame(ventana)
Frame2 = LabelFrame(ventana, text="Terminal")
Frame2.place(x=10, y=440, width=560, height=45)
Frame2.config(bd=1 , relief="sunken")

ventana.mainloop()
