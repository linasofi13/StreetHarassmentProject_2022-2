from cmath import isnan, nan # check for NaN values
from queue import PriorityQueue #  a binary heap --> for dijkstra
import pandas as pd
import backmethods # methods we need to execute main
import path_map # to draw
import time

# start = time.time()

data = pd.read_csv('calles_de_medellin_con_acoso.csv', sep=";")
graph = backmethods.generateGraph(data)

# end = time.time()
# print(f"Runtime of the graph is {end - start}") # creation of the graph time execution  

def main():
    condition = True
    while(condition):
        print("-----------------Welcome----------------")
        print("---The following program represents an algorithm for a pedestrian path that reduces both distance and risk of sexual street harassment---")
        print("---Here we have some options for you to test the algorithim:--")
        print("1. Universidad Autónoma Latinoamericana")
        print("2. Universidad Santo Tomás Sede Poblado")
        print("3. Olivia San Lucas")
        print("4. Universidad Nacional")
        print("5. Estadio Atanasio Girardot")
        print("6. Parques del Río")
        print("7. Parque Arví")
        print("8. UdeA")
        print("9. CC Premium Plaza")
        print("10. Universidad de Medellín")
        print("11. Universidad EAFIT")
        print("12. Customize Coordinates") # enter your own coordinates -> (longitude, latitude)
        print("13. Exit Program")
        print("-----")
        print("| Which origin do you want to choose? Enter a number ")
        num = int(input())
        if (0 < num < 12):
            print("| Which destination do you want to choose? Enter a number ")
            num2 = int(input())
            origin = backmethods.getCoords(num)
            destination = backmethods.getCoords(num2)
            contition = False
            break
        if num == 12: 
            print("-->>>>>>> Enter '0' to go back to the main menu <<<<<<<--")
            origin, destination = backmethods.customizeCoords(data) # lil menu when user wants to enter custom coords 
            if origin == "0" or destination == "0":
                main()
            else: 
                condition = False
                break
        if num == 13: # exit
            print("-- Have a good day :) --")
            quit()
        else: 
            print()
            print("-----------------------")
            print("Wrong input. Try again")
            print("-----------------------")
            print()
            
    # execution of first path (red)
       
    # start1 = time.time()
    parent = backmethods.dijkstraShortestSafest(graph, origin, destination)
    path_list = backmethods.make_path(parent, destination)
    path_switched = backmethods.switchXYInPath(path_list)
    # end1 = time.time()
    # print(f"Runtime of the first path is {end1 - start1}") # first path time execution
    
    # execution of second path (green)
        
    # start2 = time.time()
    parent2 = backmethods.dijkstraShortestSafest2(graph, origin, destination)
    path_list2 = backmethods.make_path(parent2, destination)
    path_switched2 = backmethods.switchXYInPath(path_list2)
    # end2 = time.time()
    # print(f"Runtime of the second path is {end2 - start2}") # second path time execution
    
    # execution of second path (purple)
    # start3 = time.time()
    parent3 = backmethods.dijkstraShortestSafest3(graph, origin, destination)
    path_list3 = backmethods.make_path(parent3, destination)
    path_switched3 = backmethods.switchXYInPath(path_list3)
    # end3 = time.time()
    # print(f"Runtime of the third path is {end3 - start3}") # third path time execution    
    
    print("------This is the first path: ------")
    print(path_switched)
    print("-----------------------------------------------------------------------------")
    print("------This is the second path: ------")
    print(path_switched2)
    print("-----------------------------------------------------------------------------")
    print("------This is the third path: ------")
    print(path_switched3)
    print("----------------------------------------------------\n")
    print("---- Now let's see the paths in a map ----\n")
    path_map.createPath(path_switched, path_switched2, path_switched3, origin, destination)
    print("-----------------------------------------------------------------------------")
    print("... A browser window should have opened to see the map in a html view  ... ")
    print("... Click on each path or the markers of the path to see more info  ... ")
    print("-----------------------------------------------------------------------------\n")
    print("---- | Total lengths and Average Risks for each Path | ----\n")
    backmethods.getDistanceOfPath(data, path_list, "Red")
    backmethods.getDistanceOfPath(data, path_list2, "Green")
    backmethods.getDistanceOfPath(data, path_list3, "Purple")
   
main()       
