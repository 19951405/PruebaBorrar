from cProfile import label
from email.mime import image
import tkinter

#------Ventana------
ventana=tkinter.Tk()
#ventana.title("Bienvenido")
#ventana.geometry("1000x600")
ventana.configure(background='LightCyan3')
#ventana.geometry("600x200")
#ventana.resizable(0,0)
#ventana.config(bg="grey")
#ventana.iconbitmap("LogoSample_ByTailorBrands.ico")

#------Etiqueta-----
cabecera=tkinter.Label(ventana, text="Bienvenidos al protocolo sanitario automatico!!!! ", bg="LightCyan3", font=("Copperplate Gothic Bold", 18)).pack(padx=10, pady=10, ipadx=20, ipady=20)
cabecera2=tkinter.Label(ventana, text="Realizado por:", bg="LightCyan3", font=("Copperplate Gothic Bold", 12)).pack(padx=20, pady=20, ipadx=5, ipady=5)
#cabecera2=tkinter.Label(ventana, text="Andrea Rios & Nicole Kuck", bg="LightCyan3", font=("Copperplate Gothic Bold", 18)).pack(padx=21, pady=21, ipadx=20, ipady=20)
#cabecera2=tkinter.Label(ventana, text="Andrea Rios", font=("Arial", 18)).pack(padx=22, pady=22, ipadx=20, ipady=20)
#cabecera2=tkinter.Label(ventana, text="El proceso inicia lavandose primero la mano", bg="LightCyan3", font=("Copperplate Gothic Bold", 20)).pack(padx=35, pady=35, ipadx=20, ipady=20)

#------Frame------
#miFrame=tkinter.Frame()
#miFrame.pack(fill="x", expand="y")
#miFrame.config(bg="grey")
#miFrame.config(width="600", height="400")

#ventana.destroy()

#-----Imagen-----
#image=tkinter.PhotoImage(file="C:/Users/Usuario/Documents/Python/protocolo.png")
#image=image.subsample(1,1)
#------LAbel------
#miLabel=tkinter.Label(miFrame, text="Bienvenidos al protocolo sanitario automatico!!!!", font=("Comic Sans MS", 16))
#miLabel.place(x=20, y=15)
#label=tkinter.Label(image=image).pack()
#miLabel.place(x=200, y=100)

ventana.mainloop()