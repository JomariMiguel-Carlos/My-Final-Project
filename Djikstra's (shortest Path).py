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
