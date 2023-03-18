## Save the name of the website, username or email and equivalent password
## Generate random password for us

import json
import random as rd
import string as st
import tkinter as tk


def generate_password():
    password_entry.delete(0, tk.END)
    random_password = ''.join(
            rd.choices(st.ascii_lowercase + st.ascii_uppercase + st.digits + st.punctuation, k=12)
        )
    password_entry.insert(tk.END, random_password)

def save_data():
    website_name = website_entry.get()
    email_address = email_entry.get()
    password = password_entry.get()

    try:
        with open('data.json', 'r') as f:
            data = json.load(f)
            data.append(
                {
                    'website': website_name,
                    'email': email_address,
                    'password': password
                }
            )
        with open('data.json', 'w') as f:
            json.dump(data, f, indent=4)

    except FileNotFoundError:
        with open('data.json', 'w') as f:
            json.dump(
                [{
                    'website': website_name,
                    'email': email_address,
                    'password': password
                }], f, indent=4
            )




# INTERFACE
window = tk.Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = tk.Canvas(height=200, width=200)
logo_img = tk.PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = tk.Label(text='Website')
website_label.grid(row=1, column=0)
email_label = tk.Label(text='Email')
email_label.grid(row=2, column=0)
password_label = tk.Label(text='Password')
password_label.grid(row=3, column=0)

# Entry
website_entry = tk.Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2, padx=5)
website_entry.focus()
email_entry = tk.Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2, padx=5)
password_entry = tk.Entry(width=35)
password_entry.grid(row=3, column=1, columnspan=2, padx=5)

# Buttons
save_btn = tk.Button(text='Save', command=save_data)
save_btn.grid(row=4, column=2)
pwd_gen_btn = tk.Button(text='Genarate Password', command=generate_password)
pwd_gen_btn.grid(row=4, column=1, pady=5)




window.mainloop()



