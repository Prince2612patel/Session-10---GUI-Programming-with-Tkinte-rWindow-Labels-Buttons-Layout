import tkinter as tk

window = tk.Tk()
window.title("Music Options")
window.geometry("300x200")

tk.Button(window, text="Like").grid(row=0, column=0, padx=20, pady=20)
tk.Button(window, text="Share").grid(row=0, column=1, padx=20, pady=20)
tk.Button(window, text="Download").grid(row=1, column=0, padx=20, pady=20)
tk.Button(window, text="Add to Queue").grid(row=1, column=1, padx=20, pady=20)

window.mainloop()
