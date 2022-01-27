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


def alg(graph, start, end):
    # form [[name, shortest_value], ...]
    vst = []
    vst_names = set()
    # dsc = [[start, 0]]
    dsc = [[0, 0, 0]]
    current_point = [start, 0]


    def next_point(points_list, name_list, val_list):
        sml_val = min(val_list)
        # [smallest value name, smallest value]
        val_idx = val_list.index(sml_val)
        return [name_list[val_idx], sml_val], val_idx


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
                    name_idx = name_list.index(name)
                    val = val_list[name_idx]
                    if new_val < val:
                        del dsc[name_idx]
                        dsc.append([name, new_val, pnt[0]])
                else:
                    dsc.append([name, new_val, pnt[0]])
            else:
                pass


    for point in graph:
        if current_point[0] != end or dsc == True:
        # step 0: define needed variables
            dsc_name_list = [pnt[0] for pnt in dsc]
            dsc_val_list = [pnt[1] for pnt in dsc]
        # step 1: find smallest point
            current_point, current_idx = next_point(dsc, dsc_name_list, dsc_val_list)
        # step 2: move it to visited
            vst.append(dsc.pop(current_idx))
            del dsc_name_list[current_idx]
            del dsc_val_list[current_idx]
            vst_names.add(current_point[0])
        # step 3: update all the values
            update(current_point, dsc_name_list, dsc_val_list)
        else:
            return vst
    return vst


def order(spp, start, point, res=[]):
    if point == start:
        res.insert(0, point)
        return(res)
    else:
        res.insert(0, point)
        idx = [i[0] for i in spp].index(point)
        next_pnt = spp[idx][2]
        order(spp[:idx], start, next_pnt)
        return(res)


if __name__ == "__main__": 


    import time
    from graphs import *
    
    
    start = 0
    end = 29
    
    result = alg(graph2, start, end)
    
    order = "->".join([str(i) for i in order(result, start, end)])
    
    start = time.time()
    for x in range(10000):
        alg(graph1, start, end)
    time = (time.time() - start) / 10000
    
    print("Time: %gsec" %time)
    print("Order: %s" %order)
    print("Shortes path length: %i" %result[-1][1])
