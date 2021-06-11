from src.dbscan import dbscan
from src.kmeans import kmeans
from getopt import getopt, GetoptError
from sys import argv
from csv import DictReader as CSVDictReader


option_templates = [
    "data=",
    "dbscan",
    "eps=",
    "min_pts=",
    "kmeans",
    "k=",
    "kmedoids",
    "x=",
    "y="
]

try:
    options, _ = getopt(argv[1:], "", option_templates)
except GetoptError:
    print("Error!")
    exit(2)

data = None
algorithm_type = None
eps = None
min_pts = None
k = None
x_label = None
y_label = None
scale_x = 1
scale_y = 1

for option, argument in options:
    if option == "--data":
        # Load data
        with open(argument, mode="r") as csv_file:
            csv_reader = CSVDictReader(csv_file)
            data = [row for row in csv_reader]
            
    elif option in ["--dbscan", "--kmeans", "--kmedoids"]:
        algorithm_type = option[2:]
        
    elif option == "--eps":
        eps = float(argument)
        
    elif option == "--min_pts":
        min_pts = float(argument)
        
    elif option == "--k":
        k = int(argument)
        
    elif option == "--x":
        x_label = argument
        
    elif option == "--y":
        y_label = argument
    
    else:
        print("Unknown option: {}".format(option))
        exit(2)

if algorithm_type == "dbscan":
    dbscan(data, eps, min_pts, x_label, y_label)
elif algorithm_type == "kmeans":
    kmeans(data, k, x_label, y_label)
else:
    print("Soon.")