import tkinter as tk
import math
import colorsys

from tkinter import colorchooser
from PIL import Image, ImageDraw
from PIL import ImageTk


def pick_color():
    color = colorchooser.askcolor(title="Select Color")
    if color[1] is not None:
        color_label.configure(bg=color[1])
        
#membuat color wheel (circular)
def create_color_wheel(radius):
    diameter = radius * 2
    image = Image.new("RGB", (diameter, diameter), "white")
    draw = ImageDraw.Draw(image)
    center = (radius, radius)

    for y in range(diameter):
        for x in range(diameter):
            distance = math.sqrt((x - radius) ** 2 + (y - radius) ** 2)

            if distance <= radius:
                angle = math.atan2(y - radius, x - radius)
                hue = (angle + math.pi) / (2 * math.pi)
                saturation = distance / radius
                r, g, b = colorsys.hsv_to_rgb(hue, saturation, 1)
                r, g, b = int(r * 255), int(g * 255), int(b * 255)
                draw.point((x, y), (r, g, b))

    return image

#TKinter windows style
root = tk.Tk()
root.title("Color Picker")

pick_button = tk.Button(root, text="Pick a Color", command=pick_color)
pick_button.pack(pady=10)

color_label = tk.Label(root, text="Selected Color", width=30, height=5)
color_label.pack()

wheel_radius = 150
color_wheel = create_color_wheel(wheel_radius)
wheel_image = ImageTk.PhotoImage(color_wheel)

canvas = tk.Canvas(root, width=wheel_radius * 2, height=wheel_radius * 2)
canvas.create_image(wheel_radius, wheel_radius, image=wheel_image)
canvas.pack()

def get_color(event):
    x = event.x - wheel_radius
    y = event.y - wheel_radius
    distance = math.sqrt(x ** 2 + y ** 2)

    if distance <= wheel_radius:
        angle = math.atan2(y, x)
        hue = angle / (2 * math.pi) + 0.5
        saturation = distance / wheel_radius
        value = 1
        r, g, b = colorsys.hsv_to_rgb(hue, saturation, value)
        r, g, b = int(r * 255), int(g * 255), int(b * 255)
        hex_color = f"#{r:02x}{g:02x}{b:02x}"
        color_label.configure(bg=hex_color)

canvas.bind("<Button-1>", get_color)

#jalankan aplikasi
root.mainloop()
