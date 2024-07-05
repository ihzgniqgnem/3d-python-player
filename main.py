from classes import *
import tkinter as tk
from PIL import Image,ImageTk
screen3d=screen(800,600,0,0,0,0,0,0)
root = tk.Tk()

def draw_point(p):
    a=p.prj(screen3d)
    screen[a[0]][a[1]]=p.color
canvas = tk.Canvas(root, width=800, height=600)
canvas.pack()
scene=scene([cube(0,0,0,100)])
while True:
    canvas.delete("all")
    screen=[[(0,0,0) for i in range(600)] for j in range(800)]
    screen3d.xangle+=0.01
    screen3d.yangle+=0.01
    screen3d.zangle+=0.01
    img = Image.new('RGB', (800, 600))
    scene.run(draw_point)
    pixels = img.load()
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            pixels[i, j] = screen[i][j]
    photo = ImageTk.PhotoImage(img)
    canvas.create_image(0, 0, anchor=tk.NW, image=photo)
    root.update()