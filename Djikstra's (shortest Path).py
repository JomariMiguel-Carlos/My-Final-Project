from tkinter import *

root = Tk()
root.geometry("662x500+300+100")
root.title("Shortest path - Dijkstra's algorithm")

grid = []
matrix = []
c = 0
count = 0
start, end = None, None
btn = None
rst = None
find = False
d = []
p = []
visited = []
u = -1
s = 0
e = 0
array_path = []

def dijk():
    global u, s, e
    s = start.grid_info()["row"] * 30 + start.grid_info()["column"]
    e = end.grid_info()["row"] * 30 + end.grid_info()["column"]
    d[s] = 0
    for i in range(570):
        mini = 999
        for j in range(570):
            if (d[j] < mini) and (visited[j] == 0):
                mini = d[j]
                u = j