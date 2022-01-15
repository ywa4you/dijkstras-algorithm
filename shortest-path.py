# Implementation of Dijbstra's algorithm by ywa. This was initially
# made as a part of a challenge.
# Copyright (C) 2021 ywa

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


import math

# ywa's dijkstra's algorithm implementaition

# graph in lists
# god kill me please
graf = [[[2, 3], [7, 9]],
        [[2, 3], [5, 3]],
        [[0, 1], [7, 5]],
        [[0, 1], [9, 3]]]

# temp vars for 
visited = []
shortest  = [0, math.inf, math.inf, math.inf]
x = shortest.copy()


def ch(point, way, point_val):
    global shortest
    if graf[point][1][way] + point_val < shortest[point]:
        shortest[graf[point][0][way]] = graf[point][1][way]


def da_way():
    global x
    for i in range(4):
        y = min(x)
# TODO fix this: index of point is in visited not its value
        print(y in visited)
        print(y)
        print(visited)
        if y in visited and y in x:
            print("xd")
            x.remove(y)
        else:
            #print(min(x))
            #print(x)
            return shortest.index(min(x))


# body
for i in range(4):
    cnt = da_way()
    for j in range(2):
        ch(cnt, j, shortest[cnt])
    visited.append(cnt)
