import pymysql
from cProfile import label
from email.mime import image
import tkinter
con=pymysql.connect(host='localhost',
            user='root',
            password='@dm1n-Admin',
            db='sensores')

data=input("codigo: ")

try: 
    with con.cursor() as cur:
        cur.execute('insert into registro(CI) values(%s)',data)
        con.commit()
        print('ok guardado')

finally:
       con.close()

ventana=tkinter.Tk()
ventana.title("Bienvenido")
ventana.geometry("1000x600")
ventana.configure(background='LightCyan3')

cabecera=tkinter.Label(ventana, text="Bienvenidos al protocolo sanitario automatico!!!! ", 
bg="LightCyan3", font=("Copperplate Gothic Bold", 18)).pack(padx=10, pady=10, ipadx=20, ipady=20)
cabecera2=tkinter.Label(ventana, text="Realizado por:", bg="LightCyan3", 
font=("Copperplate Gothic Bold", 12)).pack(padx=20, pady=20, ipadx=5, ipady=5)
cabecera2=tkinter.Label(ventana, text="Andrea Rios & Nicole Kuck", 
bg="LightCyan3", font=("Copperplate Gothic Bold", 18)).pack(padx=21, pady=21, ipadx=20, ipady=20)

cabecera2=tkinter.Label(ventana, text="El proceso inicia lavandose primero la mano", 
bg="LightCyan3", font=("Copperplate Gothic Bold", 20)).pack(padx=35, pady=35, ipadx=20, ipady=20)
image=tkinter.PhotoImage(file="protocolo.png")

label=tkinter.Label(image=image).pack()

ventana.mainloop()