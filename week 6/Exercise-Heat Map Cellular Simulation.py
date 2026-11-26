from tkinter import * 
from tkinter.ttk import *
from time import sleep
from random import randint, random

grid = []
for r in range(50):
    thisrow = []
    for c in range(70):
        thisrow.append(0)
    grid.append(thisrow)
for person in range(50):
    grid[randint(15,35)][randint(15,55)]=1

heatmap=[]
for r in range(50):
    thisrow=[]
    for c in range(70):
        thisrow.append(-1)
    heatmap.append(thisrow)

heatmap[25][69]=0

heatmap_max=0
heatmapIncomplete=True
while heatmapIncomplete:
    for r in range(50):
        for c in range(70):
            if heatmap[r][c] == -1:
                if r-1>=0 and heatmap[r-1][c] == heatmap_max:
                    heatmap[r][c] = heatmap_max+1
                elif c-1>=0 and heatmap[r][c-1] == heatmap_max:
                    heatmap[r][c] = heatmap_max+1
                elif r+1<=49 and heatmap[r+1][c] == heatmap_max:
                    heatmap[r][c] = heatmap_max+1
                elif c+1<=69 and heatmap[r][c+1] == heatmap_max:
                    heatmap[r][c] = heatmap_max+1
    heatmap_max += 1

    heatmapIncomplete = False
    for row in heatmap:
        if -1 in row:
            heatmapIncomplete = True

window = Tk()
window.geometry('1400x1000')
window.title("Evacuation")
canvas = Canvas(window, width=1400, height=1000, bg='white')
canvas.pack(anchor=CENTER, expand=True)

def handler():
    global run
    run = False
    window.destroy()
window.protocol("WM_DELETE_WINDOW", handler)

run = True

while run:
    canvas.delete("all")

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if heatmap[r][c] == 0:
                colour = "red"
            elif grid[r][c] == 1:
                colour = "blue"
            else: 
                colour = "white"
            canvas.create_rectangle((20*c,20*r), (20*(c+1), 20*(r+1)), fill=colour)
    nextgrid = []
    for r in range(len(grid)):
        thisrow = []
        for c in range(len(grid[0])):
            thisrow.append(0)
        nextgrid.append(thisrow)
    for h in range(0,heatmap_max):
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if heatmap[r][c] == h:
                    if grid[r][c] == 1 and heatmap[r][c] > 1: # person not by exit
                        min_r = r
                        min_c = c
                        if r-1>=0 and heatmap[r-1][c] < heatmap[r][c]:
                            min_r = r-1
                            min_c = c
                        if c-1>=0 and heatmap[r][c-1] < heatmap[r][c]:
                            min_r = r
                            min_c = c-1
                        if r+1<=49 and heatmap[r+1][c] < heatmap[r][c]:
                            min_r = r+1
                            min_c = c
                        if c+1<=69 and heatmap[r][c+1] < heatmap[r][c]:
                            min_r = r
                            min_c = c+1
                        if nextgrid[min_r][min_c] == 0:
                            nextgrid[min_r][min_c] = 1
                        else:
                            nextgrid[r][c] = 1
    window.update()
    sleep(0.2)
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            grid[r][c] = nextgrid[r][c]

window.mainloop()
