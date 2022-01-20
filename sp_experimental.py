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
import time

from graphs import *

start = time.time()


def alg(graph):
    # TODO fix the issue where python returns error with graph1 by
    # changing shortest to [index, shortest_value]

    # setup
    visited = []
    located = [[0], [0]]
    
    def wrt(node, node_val, graph):
        pnt_name = graph[node][0]
        pnt_vals = graph[node][1]

        for i in range(len(pnt_name)):
            if pnt_name[i] in located[0]:
                if node_val + pnt_vals[i] < located[1][located[0].index(pnt_name[i])]:
                    located[1][located[0].index(pnt_name[i])] = node_val + pnt_vals[i] 
            else:
                located[0].append(pnt_name[i])
                located[1].append(pnt_vals[i] + node_val)
    

    def next_point(lct, vst):
        vst_names = [z[0] for z in vst]
        uvst_vals = []
        for i in lct[0]:
            if i not in vst_names:
                uvst_vals.append(lct[0].index(i))
        slc = [lct[1][i] for i in uvst_vals]
        min_num = lct[1].index(min(slc))
        print(vst_names)

        print(np.where(np.array(slc) == min_num)[0])
        return min_num
    # body
    for x in range(25):
        node_idx = next_point(located, visited)
        visited.append([located[0][node_idx], located[1][node_idx]])
        wrt(visited[-1][0], visited[-1][1], graph)
    print("")
    return visited


print(alg(graph1))
#for x in range(10000):
#     alg(graph1)
#print((time.time() - start) / 10000)
