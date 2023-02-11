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

for x in range(19 * 30):
    d.append(999)
    p.append(-1)
    visited.append(0)

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

        visited[u] = 1
        for v in range(570):
            if ((d[u] + matrix[u][v]) < d[v]) and (u != v) and (visited[v] == 0):
                d[v] = d[u] + matrix[u][v]
                p[v] = u

def path(v, source):
    global array_path
    if p[v] != -1:
        path(p[v], source)
    if v != source:
        array_path.append(v)

def display(source, n):
    for i in range(n):
        if d[i] < 999:
            if i != source:
                path(i, source)
            if i != source:
                if array_path[-1] != e:
                    array_path.clear()
                else:
                    return
