from tkinter import END, Tk, Button, Entry, Event

num1 = ""
num2 = ""
op = ""
r = 0
# Configuración ventana principal
root = Tk()
root.title("Calculadora POO")
root.resizable(0,0)
root.geometry("300x260")

# Configuración pantalla de salida 
pantalla = Entry(root, width=40, bg="black", fg="white", borderwidth=0, font=("arial", 18, "bold"))
pantalla.grid(row=0, column=0, columnspan=90, padx=1, pady=1)

# Configuración botones
boton_1 = Button(root, text="1", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_1.grid(row=1, column=0, padx=1, pady=1)
boton_2 = Button(root, text="2", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_2.grid(row=1, column=1, padx=1, pady=1)
boton_3 = Button(root, text="3", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_3.grid(row=1, column=2, padx=1, pady=1)
boton_4 = Button(root, text="4", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_4.grid(row=2, column=0, padx=1, pady=1)
boton_5 = Button(root, text="5", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_5.grid(row=2, column=1, padx=1, pady=1)
boton_6 = Button(root, text="6", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_6.grid(row=2, column=2, padx=1, pady=1)
boton_7 = Button(root, text="7", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_7.grid(row=3, column=0, padx=1, pady=1)
boton_8 = Button(root, text="8", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_8.grid(row=3, column=1, padx=1, pady=1)
boton_9 = Button(root, text="9", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_9.grid(row=3, column=2, padx=1, pady=1)
boton_igual = Button(root, text="=", width=20, height=3, bg="red", fg="white", borderwidth=0, cursor=" hand2")
boton_igual.grid(row=4, column=0, columnspan=2, padx=1, pady=1)
boton_punto = Button(root, text=".", width=9, height=3, bg="spring green", fg="black", cursor="hand2", borderwidth=0)
boton_punto.grid(row=4, column=2, padx=1, pady=1)
boton_mas = Button(root, text="+", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2")
boton_mas.grid(row=1, column=3, padx=1, pady=1)
boton_menos = Button(root, text="-", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2")
boton_menos.grid(row=2, column=3, padx=1, pady=1)
boton_multiplicacion = Button(root, text="*",  width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2")
boton_multiplicacion.grid(row=3, column=3, padx=1, pady=1)
boton_division = Button(root, text="/", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2")
boton_division.grid(row=4, column=3, padx=1, pady=1)

# Handler
def handle(event: Event) -> None:
    global op
    global num1
    global num2
    global r

    entry_actual: str = pantalla.get() #estado actual del entry
    str_input: str = event.widget.cget("text") #caracter que se esta ingresando
    
    match str_input:
        case "+":
            if num1 == "":
                pantalla.delete(0, END)
                return
            op = "+"
            pantalla.insert(len(entry_actual), op)
            return
        case "-":
            if num1 == "":
                pantalla.delete(0, END)
                return
            op = "-"
            pantalla.insert(len(entry_actual), op)
            return
        case "*":
            if num1 == "":
                pantalla.delete(0, END)
                return
            op = "*"
            pantalla.insert(len(entry_actual), op)
            return
        case "/":
            if num1 == "":
                pantalla.delete(0, END)
                return
            op = "/"
            pantalla.insert(len(entry_actual), op)
            return
        
    if str_input != "=":
        if (entry_actual == str(r) and str_input == ".") or (num1 == "" and str_input == "."):
            pantalla.delete(0, END)
            return
        if entry_actual == str(r):
            pantalla.delete(0, END)       
        pantalla.insert(len(entry_actual), str_input)
        if (op):
            num2 += str_input
            return
        num1 += str_input
        return
    
    if (num1 and num2):
        match op:
            case "+":
                r = float(num1) + float(num2)
            case "-":
                r = float(num1) - float(num2)
            case "*":
                r = float(num1) * float(num2)    
            case "/":
                r = float(num1) / float(num2)    
        
        pantalla.delete(0, END)
        num1, num2, op = "", "", ""
        pantalla.insert(0, str(r))


# Events
boton_1.bind("<Button-1>", handle)
boton_2.bind("<Button-1>", handle)
boton_3.bind("<Button-1>", handle)
boton_4.bind("<Button-1>", handle)
boton_5.bind("<Button-1>", handle)
boton_6.bind("<Button-1>", handle)
boton_7.bind("<Button-1>", handle)
boton_8.bind("<Button-1>", handle)
boton_9.bind("<Button-1>", handle)
boton_igual.bind("<Button-1>", handle)
boton_punto.bind("<Button-1>", handle)
boton_mas.bind("<Button-1>", handle)
boton_menos.bind("<Button-1>", handle)
boton_multiplicacion.bind("<Button-1>", handle)
boton_division.bind("<Button-1>", handle)

root.mainloop()
