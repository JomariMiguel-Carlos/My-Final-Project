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

def counter(n):
    global c
    if n - 30 < 0:
        return c, n
    else:
        c += 1
        return counter(n - 30)

def make_matrix():
    global c
    for i in range(570):
        matrix.append([])
        for j in range(570):
            c = 0
            i_r, i_c = counter(i)
            c = 0
            j_r, j_c = counter(j)
            if i == j:
                matrix[i].append(0)
            elif i_r == j_r:
                if (i_c == j_c - 1) or (i_c == j_c + 1):
                    if grid[i_r][i_c]["bg"] == "black" or grid[j_r][j_c]["bg"] == "black":
                        matrix[i].append(999)
                    else:
                        matrix[i].append(1)
                else:
                    matrix[i].append(999)
            elif i_c == j_c:
                if (i_r == j_r - 1) or (i_r == j_r + 1):
                    if grid[i_r][i_c]["bg"] == "black" or grid[j_r][j_c]["bg"] == "black":
                        matrix[i].append(999)
                    else:
                        matrix[i].append(1)
                else:
                    matrix[i].append(999)
            else:
                matrix[i].append(999)

def make_grid():
    for i in range(19):
        grid.append([])
        for j in range(30):
            b = Button(root, bg="white", width=2, bd=1)
            b.grid(row=i, column=j)
            grid[i].append(b)

def restart():
    global start, end, grid, count, c, matrix, btn, rst, find, d, p, visited, u, s, e, array_path
    start = None
    end = None
    grid.clear()
    count = 0
    c = 0
    matrix.clear()
    find = False
    d.clear()
    p.clear()
    visited.clear()
    u = -1
    s = 0
    e = 0
    array_path.clear()

    for k in range(19 * 30):
        d.append(999)
        p.append(-1)
        visited.append(0)

    make_grid()