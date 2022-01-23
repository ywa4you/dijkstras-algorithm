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

import time
from graphs import *

start = time.time()


def alg(graph):
    # form [[name, shortest_value], ...]
    vst = []
    vst_names = []
    dsc = [[0, 0]]


    def next_point(points_list, name_list, val_list):
        sml_val = min(val_list)
        # [smallest value name, smallest value]
        return [name_list[val_list.index(sml_val)], sml_val]


    def update(pnt, name_list, val_list):
        # pnt is [name, val]
        # name is values of the first column
        for name in graph[pnt[0]][0]:
            if name not in vst_names:
                #         graphs value of the way to the point + current shortest way to current point
                #         graph's point    values  index of name of point              current point value     
                new_val = graph[pnt[0]]    [1]     [graph[pnt[0]][0].index(name)] +    pnt[1]

                if name in name_list:
                    # value of point in dsc
                    val = val_list[name_list.index(name)]
                    if new_val < val:
                        dsc.remove([name, val])
                        dsc.append([name, new_val])
                else:
                    dsc.append([name, new_val])
            else:
                pass


    for point in graph:
    # step 0: define needed variables
        dsc_name_list = [pnt[0] for pnt in dsc]
        dsc_val_list = [pnt[1] for pnt in dsc]

    # step 1: find smallest point
        current_point = next_point(dsc, dsc_name_list, dsc_val_list)
        #method pop() needs index hence this
        pop_idx = dsc.index(current_point)

    # step 2: move it to visited
        vst.append(dsc.pop(pop_idx))
        vst_names.append(current_point[0])

    # step 3: update all the values
        update(current_point, dsc_name_list, dsc_val_list)
    return vst

print(alg(graph1))
#for x in range(10000):
#    alg(graph1)
#print((time.time() - start) / 10000)
