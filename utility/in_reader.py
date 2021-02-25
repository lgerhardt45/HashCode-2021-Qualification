# read what ever we get from data/in/in_file
from classes import Car, Street, TrafficLight, Intersection, Input
import os

# opens a file and reads it
def open_file(file_name: str) -> Input:
    base_path = os.path.dirname(os.getcwd()) # get the base directory
    in_path = os.path.join(base_path, 'in', 'a_example')  # use os.path.join (works better across system)

    cars = []
    streets = []
    traffic_lights = []
    intersections = []

    input = Input()

    with open(in_path) as in_file:
        content = in_file.read()  # this should read it all in
        print(content)



        # return whatever is needed for the problem
