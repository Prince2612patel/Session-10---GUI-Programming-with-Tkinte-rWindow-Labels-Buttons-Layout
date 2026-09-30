import tkinter as tk

window = tk.Tk()
window.title("Login Form")
window.geometry("350x250")

tk.Label(window, text="Username").pack(pady=5)
username = tk.Entry(window)
username.pack()

tk.Label(window, text="Password").pack(pady=5)
password = tk.Entry(window, show="*")
password.pack()

result = tk.Label(window, text="")
result.pack(pady=15)


def login():
    if username.get() != "" and password.get() != "":
        result.config(text="Login Successful")
    else:
        result.config(text="Please enter username and password")


tk.Button(window, text="Login", command=login).pack()

window.mainloop()
