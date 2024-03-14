from tkinter import*

def button_press(num):
    global equation_text
    equation_text += str(num)
    equation_label.set(equation_text)

def equals():
    global equation_text
    try:
        total = str(eval(equation_text))
        equation_label.set(total)
        equation_text = total
    except ZeroDivisionError:
        equation_label.set("Zero Error")
        win.after(1200, clear_text)
    except SyntaxError:
        equation_label.set("Syntax Error")
        win.after(1200, clear_text)



def clear_text():
    global equation_text
    equation_text = ""
    equation_label.set(equation_text)


win = Tk()
win.title("calculator programme")
win.geometry("500x500")

equation_text = str()

equation_label = StringVar()

label = (Label(win,textvariable=equation_label,font=("consolas",20),bg="white",fg="black",width=24,height=2))
label.pack()

frame = Frame(win)
frame.pack()
buttons = [
    (1, 0, 0), (2, 0, 1), (3, 0, 2),
    (4, 1, 0), (5, 1, 1), (6, 1, 2),
    (7, 2, 0), (8, 2, 1), (9, 2, 2),
    (0, 3, 0), ("+", 0, 3), ("-", 1, 3),
    ("*", 2, 3), ("/", 3, 3), ("=", 3, 2),
    (".", 3, 1)
]

for (text, row, column) in buttons:
    button = Button(frame, text=text, height=4, width=9, font=35, command=lambda t=text: button_press(t))
    button.grid(row=row, column=column)
    if text == "=":
        button.config(command=equals)
    else:
        pass

clear = Button(win,
                text="A/C",
                height=4,
                width=9,
                font=35,
                command=clear_text)
clear.pack()

win.mainloop()