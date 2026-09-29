import sys
import tkinter as tk
from pathlib import Path


def resource_path(filename: str) -> Path:
    """
    Поиск файла 
    """
    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
        base_dir = Path(sys._MEIPASS)
    else:
        base_dir = Path(__file__).resolve().parent
    return base_dir / filename

clicks = 0

def click():
    global clicks
    clicks += 1
    label.config(text=f"Клики: {clicks}", fg="green" if clicks == 67 else "black")


window = tk.Tk()
window.title("JennyClick")

window.geometry("400x350")

label = tk.Label(window, text="Клики: 0", font=("Roboto", 20))
label.pack(pady=20)


image_path = resource_path("rezev2.png")
if not image_path.is_file():
    raise FileNotFoundError(
        f"Не найдена картинка: {image_path}\n"
        "Положи rezev2.png рядом с программой."
    )

img = tk.PhotoImage(file=str(image_path))


button = tk.Button(
    window,
    image=img,
    command=click,
    bd=0,
)
button.pack(pady=10)

window.mainloop()
