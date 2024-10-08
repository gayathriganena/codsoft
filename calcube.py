import tkinter as tk
from fractions import Fraction

r = tk.Tk()
r.title("CALCULATOR")
r.geometry("260x350")
r.config(bg="#3b3b3b")

exp = ""
f = True
calculated = False

def calculate():
    global calculated, exp
    if not screenvar.get():
        return
    try:
        tmpexp = eval(exp.replace("÷", "/").replace("×", "*"))
        exp = str(Fraction(tmpexp).limit_denominator())
        screenvar.set(exp)
        calculated = True
    except:
        screenvar.set("ERROR PRESS C")
        exp = ""

def frac():
    global f, exp, calculated
    if calculated:
        try:
            tmpexp = Fraction(exp)
            if f:
                exp = str(tmpexp)
                screenvar.set(exp)
                f = False
            else:
                screenvar.set(str(float(tmpexp)))
                f = True
        except:
            screenvar.set("ERROR PRESS C")

def clear():
    global exp, f, calculated
    exp = ""
    calculated = False
    f = True
    screenvar.set("")

def numoperator(t):
    global exp, calculated
    if calculated:
        screenvar.set("ANS")
        if t.isdigit():
            exp += ".."
        calculated = False
    if t == "÷":
        exp += "/"
    elif t == "×":
        exp += "*"
    else:
        exp += t
    screenvar.set(screenvar.get() + t)

def click(event):
    t = event.widget.cget("text")
    if screenvar.get() != "ERROR PRESS C":
        if t == "C":
            clear()
        elif t == "%":
            exp += "/100"
            screenvar.set(screenvar.get() + t)
        elif t == "S<>D":
            frac()
        elif t == "=":
            calculate()
        else:
            numoperator(t)
    else:
        if t == "C":
            clear()

f1 = tk.Frame(r, bg="black")
screenvar = tk.StringVar()
screenentry = tk.Entry(f1, width=30, text=screenvar, fg="black", bg="#e5f2e5", font=("Eurostile", 15, "bold"), justify="right", state="readonly")
screenentry.pack(fill="x")
f1.pack(fill="x")

f2 = tk.Frame(r, bg="#3b3b3b")

buttons = [
    ("OFF", "black"), ("S<>D", "black"), ("%", "black"), ("÷", "black"),
    ("7", "#D3D3D3"), ("8", "#D3D3D3"), ("9", "#D3D3D3"), ("×", "black"),
    ("4", "#D3D3D3"), ("5", "#D3D3D3"), ("6", "#D3D3D3"), ("-", "black"),
    ("1", "#D3D3D3"), ("2", "#D3D3D3"), ("3", "#D3D3D3"), ("+", "black"),
    ("C", "orange"), ("0", "#D3D3D3"), (".", "#D3D3D3"), ("=", "black"),
]

for i, (text, color) in enumerate(buttons):
    button = tk.Button(f2, text=text, height=1, width=4, fg="white", bg=color, font=("Arial", 10, "bold"))
    button.grid(row=i//4, column=i % 4, padx=8, pady=8)
    button.bind("<Button-1>", click)

f2.pack(pady=15)

r.mainloop()
