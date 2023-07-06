import tkinter as tk
from tkinter import ttk
from color_picker import ColorPickerApp
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Color Picker")

splash_screen = tk.Toplevel(root)
splash_screen.overrideredirect(True) 
splash_screen.geometry("600x400")  

logo_path = "assets/loading.gif"
logo_image = Image.open(logo_path)
logo_photo = ImageTk.PhotoImage(logo_image)
logo_label = tk.Label(splash_screen, image=logo_photo)
logo_label.pack(pady=10)

splash_screen.after(2000, splash_screen.destroy)


entry_window = tk.Toplevel(root)
entry_window.overrideredirect(True)
entry_window.geometry("600x400")

entry_label = tk.Label(entry_window, text="Welcome to Color Picker", font=("Arial", 20))
entry_label.pack(pady=50)
enter_button = tk.Button(entry_window, text="Enter", command=lambda: [entry_window.destroy(), root.deiconify(), ColorPickerApp(root)])
enter_button.pack()

root.withdraw()

root.mainloop()
