import tkinter as tk
import tkinter.font as font
from tkinter import StringVar, ttk
from tkinter import messagebox
import time

ventana = tk.Tk()
ventana.title("Calculadora con Grid")
ventana.geometry("325x300")
ventana.config(bg="lightgrey")

myFont = font.Font(family='Verdana bold')

expression = ""
equation = StringVar()
equation.set("0")

def Salir():
    messagebox.askokcancel(
    title="Pregunta", message="¿Desea salir?")


def presiono(exp):
    global expression
    expression = expression + str(exp)
    equation.set(expression)
    return expression

def borro():
    print('Ioa')
    global expression
    equation.set("0")
    expression =""


def calculo():
    global expression
    global equation

    print('Holis')
    try:           
        res=eval(expression)
        total = str(res)
        print(total)
        equation.set(total)
        expression = total
        time.sleep(2)

    except ZeroDivisionError:      
        equation.set("0")
        expression =""
        tk.messagebox.showerror(title ="Error", message="Error al dividir por zero")


entrada_label=ttk.Label(text="Calculadora", padding= 5, font=myFont)
entrada_label.grid(row=0, column=0, columnspan=4, padx=5, pady=5)


entrada = ttk.Entry(textvariable = equation)
entrada.grid(row=1, column=0, columnspan=4, sticky=tk.EW, padx=5, pady=5)



boton_uno = ttk.Button( text='1', command=lambda: presiono(1))
boton_uno.grid(row=2, column=0, padx=2, pady=2)

boton_cuatro = ttk.Button( text='4', command=lambda: presiono(4))
boton_cuatro.grid(row=3, column=0, padx=2, pady=2)

boton_siete = ttk.Button( text='7', command=lambda: presiono(7))
boton_siete.grid(row=4, column=0, padx=2, pady=2)

boton_cero = ttk.Button( text='0', command=lambda: presiono(0))
boton_cero.grid(row=5, column=0, padx=2, pady=2)

boton_dos = ttk.Button( text='2', command=lambda: presiono(2))
boton_dos.grid(row=2, column=1, padx=2, pady=2)

boton_cinco = ttk.Button( text='5', command=lambda: presiono(5))
boton_cinco.grid(row=3, column=1, padx=2, pady=2)

boton_ocho = ttk.Button( text='8', command=lambda: presiono(8))
boton_ocho.grid(row=4, column=1, padx=2, pady=2)

boton_clear = ttk.Button( text='Clear', command=borro)
boton_clear.grid(row=5, column=1, padx=2, pady=2)

boton_tres = ttk.Button( text='3', command=lambda: presiono(3))
boton_tres.grid(row=2, column=2, padx=2, pady=2)

boton_seis = ttk.Button( text='6', command=lambda: presiono(6))
boton_seis.grid(row=3, column=2, padx=2, pady=2)

boton_nueve = ttk.Button( text='9', command=lambda: presiono(9))
boton_nueve.grid(row=4, column=2, padx=2, pady=2)

boton_igual = ttk.Button( text='=', command=calculo)
boton_igual.grid(row=5, column=2, padx=2, pady=2)

boton_mas = ttk.Button( text='+', command=lambda: presiono("+"))
boton_mas.grid(row=2, column=3, padx=2, pady=2)

boton_menos = ttk.Button( text='-', command=lambda: presiono("-"))
boton_menos.grid(row=3, column=3, padx=2, pady=2)

boton_mult = ttk.Button( text='*', command=lambda: presiono("*"))
boton_mult.grid(row=4, column=3, padx=2, pady=2)

boton_div = ttk.Button( text='/', command=lambda: presiono("/"))
boton_div.grid(row=5, column=3, padx=2, pady=2)

salir = ttk.Button(text='Salir', command=Salir)
salir.grid(row = 6, padx=2, pady=2)

ventana.mainloop()
