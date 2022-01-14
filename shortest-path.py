# shortest path inpired by dijkstra

# graph in lists
# god kill me please
A = [["C", "D"], [7, 9]]
B = [["C", "D"], [5, 3]]
C = [["A", "B"], [7, 5]]
D = [["A", "B"], [9, 3]]
#first point
crnt = A

# temp vars for 
unvisited = [A, B, C, D]
shortest = ["1", "2", "3", "4"]


def short_pnt(point):
    short_val = min(point[1])
    return point[0][point[1].index(short_val)], short_val


# body

for i in range(4):
    pnt,val = short_pnt(crnt)
    unvisited.remove(pnt)
    
