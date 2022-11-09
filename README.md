
<h1 align="center">
  Street Harassment Project - Data Structures and Algorithms I
  <br>
</h1>

<h4> Team members: Lina Ballesteros and Camilo Córdoba
  <br>
  </h1>
</p>
</p>

![image](https://user-images.githubusercontent.com/103126242/200477431-9acc2e45-baee-48e7-8504-76682bd10060.png)


# Third Delivery Update 
## Code 
* Program can now receive custom coordinates and verify if the given coords are in the dataframe of the streets of Medellín.
  - Check out `customizeCoords()` at the "backmethods" file.
* Program shows 3 paths by redefining the variable v in 3 different ways with Dijkstra's Algorithm.
  - Red path: `v = l * r`
  - Green path: `v = l**(2*r)`
  - Purple path: `v = l + (80r)`
* Added `getDistanceOfPath()` at the "backmethods" file which give us the total length and average risk of a path.
  - Function is being called 3 times to see all the results for each path. 

### Technical Report and Slides

Both technical report and slides for this delivery have been added to the third delivery folder

## How does this Project work ?

Code files are divided in 3 files: 

* [backmethods.py](https://github.com/linasofi13/StreetHarassmentProyect_2022-2/blob/master/codigo/backmethods.py)

  - This file contains all the methods we call in the main file, some of them are:

`generateGraph()`
`getCoords()`
`dijkstraShortestSafest()`

* [main.py](https://github.com/linasofi13/StreetHarassmentProyect_2022-2/blob/master/codigo/main.py)

  - This is the executable file, here we have the main menu inside an infinite loop, which offers us different places to test the algorithm
  or we can just add the coords that we want to test. You can also quit the program by entering the specific option in the menu. 
  - We keep calling functions from backmethods.py. and path_map.py.

* [path_map.py](https://github.com/linasofi13/StreetHarassmentProyect_2022-2/blob/master/codigo/path_map.py)

  - This is our file to draw. We use "Folium", a really nice library to draw the 3 paths requested and we added cute markers to the starting point and the destination.
