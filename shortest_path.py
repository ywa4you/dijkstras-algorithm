# Implementation of Dijkstra's algorithm by ywa V. 1.0. This was initially
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

import numpy as np
# import math
import time

from graphs import *

start = time.time()


def alg(graph):
    # TODO fix the issue where python returns error with graph1 by
    # changing shortest to [index, shortest_value]

    # setup
    unvisited = [graph.index(i) for i in graph]
    #shortest  = [math.inf for i in graph]
    shortest  = [999 for i in graph]
    shortest[0] = 0
    
    
    def wrt(point, point_val, graph, shrt):
        pnt_pos = graph[point][0]
        pnt_val = graph[point][1]
        for i in range(len(graph[point][0])):
            if pnt_val[i] + point_val < shrt[pnt_pos[i]]:
                shrt[pnt_pos[i]] = pnt_val[i] + point_val
    

    def next_point(shrt, unvst):
        min_num = min([shrt[i] for i in unvst])
        for i in np.where(np.array(shrt) == min_num)[0]:
            if i in unvisited:
                return i 
    # body
    for i in range(len(graph)):
        cnt = next_point(shortest, unvisited)
        wrt(cnt, shortest[cnt], graph, shortest)
        unvisited.remove(cnt)
    
    return shortest


print(alg(graph1))
# for x in range(10000):
#     alg(graph1)
# print((time.time() - start) / 10000)
