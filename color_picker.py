import tkinter as tk
from tkinter import colorchooser
from PIL import Image, ImageDraw
import math
import colorsys
from PIL import ImageTk

class ColorPickerApp:
    def __init__(self, master):
        self.master = master
        self.pick_button = tk.Button(self.master, text="Pick a Color", command=self.pick_color)
        self.pick_button.pack(pady=10)
        self.color_label = tk.Label(self.master, text="Selected Color", width=30, height=5)
        self.color_label.pack()
        self.wheel_radius = 150
        self.color_wheel = self.create_color_wheel(self.wheel_radius)
        self.wheel_image = ImageTk.PhotoImage(self.color_wheel)
        self.canvas = tk.Canvas(self.master, width=self.wheel_radius * 2, height=self.wheel_radius * 2)
        self.canvas.create_image(self.wheel_radius, self.wheel_radius, image=self.wheel_image)
        self.canvas.pack()

        self.canvas.bind("<Button-1>", self.get_color)

    def pick_color(self):
        color = colorchooser.askcolor(title="Select Color")
        if color[1] is not None:
            self.color_label.configure(bg=color[1])

    #membuat color wheel (circular)
    def create_color_wheel(self, radius):
        image = Image.new("RGB", (radius * 2, radius * 2), "white")
        draw = ImageDraw.Draw(image)
        center = (radius, radius)

        for y in range(radius * 2):
            for x in range(radius * 2):
                dx = x - radius
                dy = y - radius
                distance = math.sqrt(dx ** 2 + dy ** 2)

                if distance <= radius:
                    angle = math.atan2(dy, dx)
                    hue = (angle + math.pi) / (2 * math.pi)
                    saturation = distance / radius
                    r, g, b = colorsys.hsv_to_rgb(hue, saturation, 1)
                    r, g, b = int(r * 255), int(g * 255), int(b * 255)
                    
                    draw.point((x, y), (r, g, b))

        return image

    def get_color(self, event):
        x = event.x - self.wheel_radius
        y = event.y - self.wheel_radius
        distance = math.sqrt(x ** 2 + y ** 2)

        if distance <= self.wheel_radius:
            angle = math.atan2(y, x)
            hue = angle / (2 * math.pi) + 0.5
            saturation = distance / self.wheel_radius

        value = 1

        # HSV to RGB
        r, g, b = colorsys.hsv_to_rgb(hue, saturation, value)
        r, g, b = int(r * 255), int(g * 255), int(b * 255)

        # RGB to hexadecimal 
        hex_color = f"#{r:02x}{g:02x}{b:02x}"

        self.color_label.configure(bg=hex_color)