import tkinter as tk
from math import tan, radians
from time import sleep
from vector import *
from turtle import *
hideturtle()
tracer(0)
screen=screen(1,0,0,0)
def draw_point(x,y):
    up()
    goto(x,y)
    down()
    fd(1)
face([face([point(i,i,j) for j in range(100)]) for i in range(100)]).run(draw_point,screen)
update()
while True:
    pass
