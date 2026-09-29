import tkinter as tk

clicks = 0

def click():
    global clicks
    clicks += 1
    label.config(text=f"Клики: {clicks}")

window = tk.Tk()
window.title("JennyClick")

window.geometry("400x350")

label = tk.Label(window, text="Клики: 0", font=("Roboto", 20))
label.pack(pady=20)


img = tk.PhotoImage(file="2026-09-29 18.02.49.png")


button = tk.Button(
    window,
    image=img,
    command=click,
    bd=0,
)
button.pack(pady=10)

window.mainloop()
