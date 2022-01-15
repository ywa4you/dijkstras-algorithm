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
itr = []
unvisited = [0, 1, 2, 3]
shortest  = [0, math.inf, math.inf, math.inf]



def ch(point, way, point_val):
    global shortest
    pnt_pos = graf[point][0][way]
    pnt_val = graf[point][1][way]
    if pnt_val + point_val < shortest[pnt_pos]:
        shortest[pnt_pos] = pnt_val + point_val

def da_way():
    x = []
    for i in unvisited:
        x.append(shortest[i])
    return shortest.index(min(x))


# body
for i in range(4):
    cnt = da_way()
    for j in range(2):
        ch(cnt, j, shortest[cnt])
    unvisited.remove(cnt)
    itr.append(cnt)

print(itr)
print(shortest)
