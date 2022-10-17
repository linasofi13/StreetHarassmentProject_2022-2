from cmath import isnan, nan # check for NaN values
from queue import PriorityQueue #  a binary heap --> for dijkstra
import pandas as pd
import backmethods # methods we need to execute main
import path_map # to draw

data = pd.read_csv('calles_de_medellin_con_acoso.csv', sep=";")
graph = backmethods.generateGraph(data)

def main(): 
    condition = True
    while(condition): 
        print("-----------------Welcome----------------") # menu
        print("---The following program represents an algorithm for a pedestrian path that reduces both distance and risk of sexual street harassment---")
        print("| Select origin | ")
        print("---Here we have some options for you to test the algorithim:--")
        print("1. Universidad Autónoma Latinoamericana") # added these options to test the algorithm
        print("2. Universidad Santo Tomás Sede Poblado")
        print("3. Olivia San Lucas")
        print("4. Universidad Nacional")
        print("5. Estadio Atanasio Girardot")
        print("6. Parques del Río")
        print("7. Parque Arví")
        print("8. UdeA")
        print("9. CC Premium Plaza")
        print("10. Universidad de Medellín")
        print("-----")
        print("| Which origin do you want to choose? Enter a number ")
        num = int(input())
        print("| Which destination do you want to choose? Enter a number ")
        num2 = int(input())
        if (0 < num < 11) and  (0 < num2 < 11): # check if user entered a valid option
            origin = backmethods.getCoords(num) 
            destination = backmethods.getCoords(num2)
            contition = False
            break
        else: # user entered a wrong num
            print()
            print("-----------------------")
            print("Wrong input. Try again")
            print("-----------------------")
            print()
    parent = backmethods.dijkstraShortestSafest(graph, origin, destination) # calling dijkstra
    path_list = backmethods.make_path(parent, destination)
    path_switched = backmethods.switchXYInPath(path_list)
    print("------This is the path: ------")
    print(path_switched) 
    print("---- Now let's see the path in a map ----")
    path_map.createPath(path_switched, origin, destination) # will open a new tab with the map
  
    
main()
