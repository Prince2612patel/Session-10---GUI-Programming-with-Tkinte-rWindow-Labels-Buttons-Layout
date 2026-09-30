import tkinter as tk

window = tk.Tk()
window.title("My Playlist")
window.geometry("400x250")

label = tk.Label(window, text="Welcome to Your Music Playlist")
label.pack(pady=20)

# result = tk.Label(window, text="")
# result.pack(pady=10)


def play():
    result.config(text="Playing")


def pause():
    result.config(text="Paused")


def next_song():
    result.config(text="Next Song")


tk.Button(window, text="Play", command=play).pack(side="left", padx=20)
tk.Button(window, text="Pause", command=pause).pack(side="left", padx=20)
tk.Button(window, text="Next", command=next_song).pack(side="left", padx=20)

window.mainloop()
