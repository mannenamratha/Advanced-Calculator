

import tkinter as tk
import math

expression = ""
history = []

themes = {
    "light": {
        "bg": "#F5F5F5",
        "entry_bg": "white",
        "btn_bg": "#E0E0E0",
        "fg": "#000"
    },
    "dark": {
        "bg": "#2E2E2E",
        "entry_bg": "#3E3E3E",
        "btn_bg": "#4E4E4E",
        "fg": "#FFFFFF"
    }
}
current_theme = "light"

root = tk.Tk()
root.title("Advanced Calculator")
root.geometry("420x700")
root.resizable(False, False)

entry_text = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_text, font=('Arial', 24), bd=10, relief=tk.RIDGE, justify='right')
entry.pack(expand=True, fill='both', ipadx=8, ipady=15, padx=10, pady=10)

def apply_theme():
    theme = themes[current_theme]
    root.configure(bg=theme["bg"])
    entry.configure(bg=theme["entry_bg"], fg=theme["fg"])
    for btn in buttons_dict.values():
        btn.configure(bg=theme["btn_bg"], fg=theme["fg"])

def press(char):
    global expression
    expression += str(char)
    entry_text.set(expression)

def clear():
    global expression
    expression = ""
    entry_text.set("")

def backspace():
    global expression
    expression = expression[:-1]
    entry_text.set(expression)

def evaluate():
    global expression
    try:
        expr = expression.replace("√", "math.sqrt").replace("^", "**")
        expr = expr.replace("sin", "math.sin").replace("cos", "math.cos")
        expr = expr.replace("tan", "math.tan").replace("log", "math.log10")
        result = str(eval(expr))
        entry_text.set(result)
        history.append(f"{expression} = {result}")
        expression = result
    except:
        entry_text.set("Error")
        expression = ""

def show_history():
    win = tk.Toplevel(root)
    win.title("History")
    win.geometry("300x400")
    tk.Label(win, text="Calculation History", font=('Arial', 14)).pack()
    text = tk.Text(win, font=('Arial', 12))
    text.pack(expand=True, fill='both')
    for h in history:
        text.insert(tk.END, h + '\n')

def toggle_theme():
    global current_theme
    current_theme = "dark" if current_theme == "light" else "light"
    apply_theme()

button_frame = tk.Frame(root)
button_frame.pack(expand=True, fill='both')

buttons_list = [
    ('C', 1, 0), ('⌫', 1, 1), ('(', 1, 2), (')', 1, 3),
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 3, 3),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3),
    ('0', 5, 0), ('.', 5, 1), ('^', 5, 2), ('+', 5, 3),
    ('sin(', 6, 0), ('cos(', 6, 1), ('tan(', 6, 2), ('log(', 6, 3),
    ('√(', 7, 0), ('History', 7, 1), ('Theme', 7, 2), ('=', 7, 3)
]

buttons_dict = {}
btn_font = ("Arial", 18)

for (text, row, col) in buttons_list:
    if text == 'C':
        cmd = clear
    elif text == '⌫':
        cmd = backspace
    elif text == '=':
        cmd = evaluate
    elif text == 'History':
        cmd = show_history
    elif text == 'Theme':
        cmd = toggle_theme
    else:
        cmd = lambda x=text: press(x)

    btn = tk.Button(button_frame, text=text, font=btn_font, width=5, height=2, command=cmd, bd=1, relief='ridge')
    btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
    buttons_dict[text] = btn

for i in range(8):
    button_frame.rowconfigure(i, weight=1)
for j in range(4):
    button_frame.columnconfigure(j, weight=1)

def key_input(event):
    key = event.char
    if key in '0123456789.+-*/()^':
        press(key)
    elif key == '\r':
        evaluate()
    elif key == '\x08':
        backspace()

root.bind("<Key>", key_input)
apply_theme()
root.mainloop()
