from cmath import isnan, nan # check for NaN values
from queue import PriorityQueue #  a binary heap --> for dijkstra
import pandas as pd

def getAverageForNaN(data): # returns average (int)
    risk_data = data.loc[:, "harassmentRisk"]
    accumulator = 0
    count = 0
    for i in risk_data: # calculates the average risk 
        if isnan(i):
            continue
        accumulator = accumulator + i
        count = count + 1
    average = accumulator/count      
    return average
    
def generateGraph(data): 
    risk_data = data.loc[:, "harassmentRisk"]
    average = getAverageForNaN(data)
    new_harassment_data = risk_data.replace(to_replace = nan, value = average)
    data.loc[:, "harassmentRisk"] = new_harassment_data # adds the numpy array with risks updated to dataframe
    unique_origins = data.origin.unique() # gets unique origins of dataframe
    graph = {}
    for i in unique_origins:
        graph[i] = {} # assigns unique origins as keys of the adjacency list
    for i in data.index:
        if data["oneway"][i]: # if is true we need to add it from origin to destination and from destination to origin
            graph[data["origin"][i]][data["destination"][i]] = (data["length"][i],data["harassmentRisk"][i])
            try:
                graph[data["destination"][i]][data["origin"][i]] = (data["length"][i],data["harassmentRisk"][i])
            except KeyError: # when oneway is true and the destination should be a origin node, but it was not in the graph before, an error occurs (keyerror), so we add it as a new key
                destination = data["destination"][i]
                origin = data["origin"][i]
                graph[destination] = {origin: (data["length"][i], data["harassmentRisk"][i])}
        else: # it is false, so we add it only from origin to destination
            graph[data["origin"][i]][data["destination"][i]] = (data["length"][i],data["harassmentRisk"][i])
            
    return graph

def getCoords(num):
    if num == 1:
        return "(-75.5738729, 6.2514919)"
    if num == 2:
        return "(-75.5613677, 6.1870143)"
    if num == 3:
        return "(-75.5648682, 6.1815001)"
    if num == 4:
        return "(-75.5762232, 6.266327)"
    if num == 5:
        return "(-75.5879543, 6.2568545)"
    if num == 6:
        return "(-75.5777399, 6.2433649)"
    if num == 7:
        return "(-75.5090451, 6.2802547)"
    if num == 8:
        return "(-75.5694416, 6.2650137)"
    if num == 9:
        return "(-75.5714832, 6.2291303)"
    if num == 10:
        return "(-75.6101708, 6.231175)"
    
def dijkstraShortestSafest(graph, origin, destination):
    visited = set() 
    cost = {origin: 0}
    parent = {origin: None} # set parent as None
    priority = PriorityQueue() # using a priority queue 
    priority.put((0, origin)) # set origin as 0 
    while priority:
        while not priority.empty():
            _, vertex = priority.get() # finds lowest cost vertex
            # loop until we get a fresh vertex
            if vertex not in visited: 
                break # at first iteration this is true so it goes from here *
        else: # if priority ran out
            break # quit main loop
        visited.add(vertex) # add vertex to visited ||| to here*
        if vertex == destination:
            break
        for neighbor, lenrisk in graph[vertex].items():
            length, risk = lenrisk
            weigth = length * risk 
            if neighbor in visited: continue # skip these to save time
            old_cost = cost.get(neighbor, float('inf')) # default to infinity
            new_cost = cost[vertex] + weigth
            if new_cost < old_cost:
                priority.put((new_cost, neighbor))
                cost[neighbor] = new_cost
                parent[neighbor] = vertex

    return parent

def make_path(parent, destination): # returns the path --> a list of tuples, each tuple is a pair of coordinates
    if destination not in parent:
        return None
    v = destination
    path = []
    while v is not None: # root has null parent
        path.append(v)
        v = parent[v]
    return path[::-1]

def switchXYInPath(path_list): # we switch x,y for every typle in the path 
    tuples = [eval(ele) for ele in path_list]
    path_switched = []
    for i in tuples:
        y, x = i
        tuple_of_coords = (x, y)
        path_switched.append(tuple_of_coords)
    return path_switched #  we need them in the correct order to implement the path drawing
