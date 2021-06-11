from src.dbscan import dbscan
from src.kmeans import kmeans
from src.kmedoids import kmedoids
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
        min_pts = int(argument)
        
    elif option == "--k":
        k = int(argument)
        
    elif option == "--x":
        x_label = argument
        
    elif option == "--y":
        y_label = argument
    
    else:
        print("Unknown option: {}".format(option))
        exit(2)

if data == None:
    print("No data! Use --data <path-to-your-data> options. Make sure it\'s CSV.")
    exit(2)
    
if algorithm_type == "dbscan":
    if min_pts == None:
        print("DBSCAN needs minimum points. Use --min_pts <minimum-points>. Make sure it\'s integer.")
        exit(2)
        
    if eps == None:
        print("DBSCAN needs epsilon. Use --eps <epsilon>. Make sure it\'s float.")
        exit(2)
    
    dbscan(data, eps, min_pts, x_label, y_label)
    
elif algorithm_type == "kmeans":
    if k == None:
        print("K-means needs k. Use --k <k-value>. Make sure it\'s integer.")
        exit(2)

    kmeans(data, k, x_label, y_label)
    
elif algorithm_type == "kmedoids":
    if k == None:
        print("K-moloids needs k. Use --k <k-value>. Make sure it\'s integer.")
        exit(2)
        
    kmedoids(data, k, x_label, y_label)
    
else:
    print("Available algorithm: --dbscan; --kmeans; --kmedoids")
    exit(2)