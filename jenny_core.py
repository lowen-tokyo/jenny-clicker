import tkinter as tk

clicks = 0

def click():
    global clicks
    clicks += 1
    label.config(text=f"Клики: {clicks}")

window = tk.Tk()
window.title("JennyClick")

window.geometry("400x350")

bg_img = tk.PhotoImage(file="bg1.png")
bg_label = tk.Label(window, image=bg_img)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

label = tk.Label(window, text="Клики: 0", font=("Arial", 20))
label.pack(pady=20)


img = tk.PhotoImage(file="rezev2.png")


button = tk.Button(
    window,
    image=img,
    command=click,
    bd=0,
)
button.pack(pady=10)

window.mainloop()
