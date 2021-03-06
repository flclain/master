import sys 
import os

import  helpers

import time


import analysis.helpers_a as helpers_a
import json
import csv
import matplotlib.pyplot as plt


ROOT = "./"
CSV = ROOT + "data/csv/"




from matplotlib.lines import Line2D      
from matplotlib.patches import Polygon
def plot_street(param,depth):
    delta_y = -1.5
    delta_x = 0.
    lines = [
        plt.Polygon([[-param + delta_x,-param + delta_y],[0 + delta_x,-param + delta_y],[0 + delta_x,0 + delta_y],[-param + delta_x,0 + delta_y]],color = "black",fill = False), #5
        plt.Polygon([[0 + delta_x,0+ delta_y],[param + delta_x,0+ delta_y],[param + delta_x,-param+ delta_y],[0 + delta_x,-param+ delta_y]],color = "black",fill = False),#7
        plt.Polygon([[0 + delta_x,0+ delta_y],[param + delta_x,0+ delta_y],[param + delta_x,param+ delta_y],[0 + delta_x,param+ delta_y]],color = "black",fill = False),#8
        plt.Polygon([[0 + delta_x,0+ delta_y],[0 + delta_x,param+ delta_y],[-param + delta_x,param+ delta_y],[-param + delta_x,0+ delta_y]],color = "black",fill = False),#6
        plt.Polygon([[-depth + delta_x,-param+ delta_y],[-param + delta_x,-param+ delta_y],[-param + delta_x,0+ delta_y],[-depth + delta_x,0+ delta_y]],color = "black",fill = False,closed = False),#4
        plt.Polygon([[-depth + delta_x,0+ delta_y],[-param + delta_x,0+ delta_y],[-param + delta_x,param+ delta_y],[-depth + delta_x,param+ delta_y]],color = "black",fill = False,closed = False),#12
        plt.Polygon([[-param + delta_x,-depth+ delta_y],[-param + delta_x,-param+ delta_y],[0 + delta_x,-param+ delta_y],[0 + delta_x,-depth+ delta_y]],color = "black",fill = False,closed = False),#9
        plt.Polygon([[0 + delta_x,-depth+ delta_y],[0 + delta_x,-param+ delta_y],[param + delta_x,-param+ delta_y],[param + delta_x,-depth+ delta_y]],color = "black",fill = False,closed = False),#1
        plt.Polygon([[depth + delta_x,param+ delta_y],[param + delta_x,param+ delta_y],[param + delta_x,0+ delta_y],[depth + delta_x,0+ delta_y]],color = "black",fill = False,closed = False),#3
        plt.Polygon([[depth + delta_x,0+ delta_y],[param + delta_x,0+ delta_y],[param + delta_x,-param+ delta_y],[depth + delta_x,-param+ delta_y]],color = "black",fill = False,closed = False),#10
        plt.Polygon([[-param + delta_x,depth+ delta_y],[-param + delta_x,param+ delta_y],[0 + delta_x,param+ delta_y],[0 + delta_x,depth+ delta_y]],color = "black",fill = False,closed = False),#2
        plt.Polygon([[0 + delta_x,depth+ delta_y],[0 + delta_x,param+ delta_y],[param + delta_x,param+ delta_y],[param + delta_x,depth+ delta_y]],color = "black",fill = False,closed = False) #11
    ]
    for line in lines:
        plt.gca().add_line(line)
 
def plot_coordinates(coordinates):
    x = [p[0] for p in coordinates]
    y = [p[1] for p in coordinates]
    plt.plot(x,y)   

def plot_trajectories(file_path, user_type = None,selected_subscenes = [],plot_context = True,temp_path = "./data/temp/temp.txt"):
    helpers.extract_trajectories(file_path,destination_path = temp_path, save = True)

    param = 5
    depth = 20
    if plot_context:
        plot_street(param,depth)
    with open(temp_path) as trajectories:
        for i,trajectory in enumerate(trajectories):
            trajectory = json.loads(trajectory)
            coordinates = trajectory["coordinates"]
            scene = trajectory["scene"]

            if not selected_subscenes :
                if user_type == None:
                    plot_coordinates(coordinates)  
                elif trajectory["user_type"] == user_type:
                    plot_coordinates(coordinates)    
            elif scene in selected_subscenes:
                if user_type == None:
                    plot_coordinates(coordinates)  
                elif trajectory["user_type"] == user_type:
                    plot_coordinates(coordinates)  
        plt.show()    
        os.remove(temp_path)        
    return

# python visualize.py parameters/data.json scene original
def main():
    args = sys.argv
    data = json.load(open(args[1]))
    original = int(args[3])

    file_path = ""
    if original:
        file_path = data["extracted_datasets"] + args[2] + ".csv"
    else:
        file_path = data["preprocessed_datasets"] + args[2] + ".csv"
    
    user = None
    
    # id_scene = 1
    prefix = "minute number: "
    ids = [1]
    selected_subscenes = [prefix + str(i) for i in ids]
    selected_subscenes = []
    #         +str(id_scene)
    plot_trajectories(file_path, user_type = user,selected_subscenes= selected_subscenes,plot_context= False)
    

if __name__ == "__main__":
    main()
