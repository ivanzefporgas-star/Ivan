# from tkinter import*
# import random 
# A = 0 
# B= ["#42855C","#57AB2B","#9688A6","#1D73F4","#83206E"]
# def klic():
#     global A
#     A += 1
#     text["text"] = "Кнопок нажато "+str(A)
#     color = random. choice(B)
#     red["bg"]=color
#     print("Шутка")
# app = Tk()
# red = Button(text="На северную корею",command= klic)
# text = Label(text=A,bg="#727295",fg= "#421873")
# text. place(x=300,y=100)
# app. geometry("333x333+500+100")
# app. title("ivanzefporgas")
# app["bg"]="#417065"
# red. place(x=100,y=100)
# app. mainloop()


# import tkinter as tk

# def on_click(event):
#     text = event.widget.cget("text")
#     if text == "=":
#         try:
#             result = str(eval(str(entry.get())))
#             entry.delete(0, tk.END)
#             entry.insert(0, result)
#         except Exception as e:
#             entry.delete(0, tk.END)
#             entry.insert(0, "Error")
#     elif text == "C":
#         entry.delete(0, tk.END)
#     else:
#         entry.insert(tk.END, text)

# root = tk.Tk()
# root.title("Tkinter Calculator")

# entry = tk.Entry(root, font="Arial 20", borderwidth=5, relief=tk.RIDGE, justify='right')
# entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# buttons = [
#     '7', '8', '9', '/',
#     '4', '5', '6', '*',
#     '1', '2', '3', '-',
#     'C', '0', '=', '+'
# ]

# row_val = 1
# col_val = 0

# for button in buttons:
#     btn = tk.Button(root, text=button, font="Arial 18", width=4, height=2)
#     btn.grid(row=row_val, column=col_val, padx=5, pady=5)
#     btn.bind("<Button-1>", on_click)
#     col_val += 1
#     if col_val > 3:
#         col_val = 0
#         row_val += 1

# root.mainloop()

import tkinter as tk

def on_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(0, result)
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(0, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        if entry.get() == "Error":
            entry.delete(0, tk.END)
        entry.insert(tk.END, text)

root = tk.Tk()
root.title("Modern Calculator")
root.geometry("350x500")
root.config(bg="#222831")

# Modern font and colors
ENTRY_BG = "#393e46"
ENTRY_FG = "#eeeeee"
BTN_BG = "#00adb5"
BTN_BG_OP = "#393e46"
BTN_FG = "#eeeeee"
BTN_FONT = ("Segoe UI", 18, "bold")
ENTRY_FONT = ("Segoe UI", 26, "bold")

entry = tk.Entry(root, font=ENTRY_FONT, borderwidth=0, relief=tk.FLAT,
                 bg=ENTRY_BG, fg=ENTRY_FG, justify='right')
entry.insert(0, "0")
entry.pack(fill=tk.BOTH, pady=(40, 20), padx=20, ipady=15)

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", "C", "=", "+"]
]

frame = tk.Frame(root, bg="#222831")
frame.pack(padx=15, pady=10, expand=True, fill=tk.BOTH)

for i, row in enumerate(buttons):
    for j, btn_text in enumerate(row):
        if btn_text in {'/', '*', '-', '+', '='}:
            bg = BTN_BG
        elif btn_text == "C":
            bg = "#f96d00"
        else:
            bg = BTN_BG_OP
        btn = tk.Button(frame, text=btn_text, font=BTN_FONT, bg=bg, fg=BTN_FG,
                        borderwidth=0, relief=tk.FLAT, activebackground="#222831", activeforeground="#00adb5")
        btn.grid(row=i, column=j, sticky="nsew", padx=8, pady=8, ipadx=5, ipady=15)
        btn.bind("<Button-1>", on_click)

# Make buttons expand and fill space
for i in range(4):
    frame.grid_rowconfigure(i, weight=1)
    frame.grid_columnconfigure(i, weight=1)

root.mainloop()
#Hi all eg fra ukraina eg likar meg katt