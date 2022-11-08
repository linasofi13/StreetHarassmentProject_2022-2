import folium # drawing library
import webbrowser
import os # auxiliary library to save the map
from folium.plugins import MarkerCluster # just a lil of decoration for the markers 

def createPath(path_switched1, path_switched2, path_switched3, origin, destination):
    tuple_origin = tuple(origin[1:-1].split(", "))
    latitude_origin =  float(tuple_origin[1]) # origin needs to be switched
    longitude_origin =  float(tuple_origin[0])

    tuple_destination = tuple(destination[1:-1].split(", "))
    latitude_destination =  float(tuple_destination[1]) # destination also needs to be switched
    longitude_destination =  float(tuple_destination[0])

    m = folium.Map(location=[latitude_origin, longitude_origin], # generates map 
                zoom_start=15)

    location1 = path_switched1 # coords
    location2 = path_switched2 # coords
    location3 = path_switched3 # coords
    
    marker1 = folium.Marker(location = [latitude_origin, longitude_origin], 
                            popup = "Origin",
                            icon = folium.Icon(color = 'blue', icon = 'home')).add_to(m)
    
    marker2 = folium.Marker(location = [latitude_destination, longitude_destination], 
                            popup = "Destination",
                            icon = folium.Icon(color = 'blue', icon = 'flag')).add_to(m)

    route1 = folium.PolyLine(location1,
                    color='red',
                    popup="v=d*r",
                    weight=10,
                    opacity=0.8).add_to(m) # v = d * r
    
    route2 = folium.PolyLine(location2,
                    color='green',
                    popup="v=d**(2*r)",
                    weight=10,
                    opacity=0.8).add_to(m) # v = d ** (2 * r)
    
    route3 = folium.PolyLine(location3,
                    color='purple',
                    popup="v=d+(80r)",
                    weight=10,
                    opacity=0.8).add_to(m) # v = d + 80r

    m.save(os.path.join('Path.html'))
    webbrowser.open_new_tab('Path.html')
