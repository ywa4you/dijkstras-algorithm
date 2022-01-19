# Implementation of Dijkstra's algorithm by ywa. This was initially
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
from graphs import *


def alg(graph):
    # TODO fix the issue where python returns error with graph1 by
    # changing shortest to [index, shortest_value]

    # setup
    unvisited = [graph.index(i) for i in graph]
    shortest  = [math.inf for i in graph]
    shortest[0] = 0
    
    
    def wrt(point, point_val, graph, shrt):
        pnt_pos = graph[point][0]
        pnt_val = graph[point][1]
        for i in range(len(graph[point][0])):
            #print(pnt_val[i] + point_val, pnt_pos[i])
            if pnt_val[i] + point_val < shrt[pnt_pos[i]]:
                shrt[pnt_pos[i]] = pnt_val[i] + point_val
    

    def next_point(shrt, unvst):
        print([shrt[i] for i in unvst])
        print(min([shrt[i] for i in unvst]))
        return shrt.index(min([shrt[i] for i in unvst]))
    
    
    # body
    for i in range(len(graph)):
        cnt = next_point(shortest, unvisited)
        print(cnt)
        wrt(cnt, shortest[cnt], graph, shortest)
        print(shortest)
        unvisited.remove(cnt)
    
    return shortest


print(alg(graph0))
