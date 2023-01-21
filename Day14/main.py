# GIU 



# interface = tk.Entry(window)
# interface.pack()

# def calculate():
#     print(interface.get())

# cal_btn = tk.Button(window, text="Calculate", command=calculate)
# cal_btn.pack()


# calculator


import tkinter as tk

window = tk.Tk()
# window.geometry("500x500")
window.config(padx=50, pady=50)
window.title("Calculator")

def display(btn):
    # print("Button: ", type(btn))
    screen.insert(tk.END, btn['text'])


screen = tk.Entry(window)
screen.grid(column=0, row=0, columnspan=3)

btn_1 = tk.Button(text="1", command=lambda: display(btn_1))
btn_1.grid(column=0, row=1)

btn_2 = tk.Button(text="2", command=lambda: display(btn_2))
btn_2.grid(column=1, row=1)

btn_3 = tk.Button(text="3", command=lambda: display(btn_3))
btn_3.grid(column=2, row=1)

btn_4 = tk.Button(text="4", command=lambda: display(btn_4))
btn_4.grid(column=0, row=2)

btn_5 = tk.Button(text="5", command=lambda: display(btn_5))
btn_5.grid(column=1, row=2)

btn_6 = tk.Button(text="6", command=lambda: display(btn_6))
btn_6.grid(column=2, row=2)

btn_7 = tk.Button(text="7", command=lambda: display(btn_7))
btn_7.grid(column=0, row=3)

btn_8 = tk.Button(text="8", command=lambda: display(btn_8))
btn_8.grid(column=1, row=3)

btn_9 = tk.Button(text="9", command=lambda: display(btn_9))
btn_9.grid(column=2, row=3)

btn_0 = tk.Button(text="0", command=lambda: display(btn_0))
btn_0.grid(column=1, row=4)

btn_dot = tk.Button(text=".", command=lambda: display(btn_dot))
btn_dot.grid(column=0, row=4)


btn_eql = tk.Button(text="=")
btn_eql.grid(column=2, row=4)






window.mainloop()




