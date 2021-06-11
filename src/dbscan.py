import matplotlib.pyplot as plt
from random import randrange
from statistics import pstdev

def draw_plot(points, color, size, alpha, label):
    x = list(map(lambda p: p[0], points))
    y = list(map(lambda p: p[1], points))
    plt.scatter(x, y, c = color, s = size, alpha = alpha, label = label)

def dbscan(data, eps, min_pts, x_col = None, y_col = None):
    len_data = len(data)
    if len_data == 0:
        print("Data is empty!")
        return
        
    if x_col == None or y_col == None:
        cols = list(data[0].keys())
        if len(cols) <= 1:
            print("Too few columns!")
            return
        
        if x_col == None:
            x_col = cols[0]
        if y_col == None:
            y_col = cols[1]
        
    selected_points = list(map(lambda d: (float(d[x_col]), float(d[y_col])), data))
    x = list(map(lambda p: p[0], selected_points))
    y = list(map(lambda p: p[1], selected_points))
    pstdev_x = pstdev(x)
    pstdev_y = pstdev(y)
    
    def std_distance(p1, p2):
        return (((p1[0] - p2[0]) / pstdev_x) ** 2
            + ((p1[1] - p2[1]) / pstdev_y) ** 2)
    
    
    unused_points = selected_points.copy()
    clusters = []
    outliers = []
    while len(unused_points) > 0:
        current_cluster = []
        frontier = []
        frontier.append(unused_points.pop())
        while len(frontier) > 0:
            current_point = frontier.pop()
            current_cluster.append(current_point)
            points_in_radius = list(
                filter(
                    lambda p: std_distance(current_point, p) <= eps,
                    selected_points
                )
            )
            
            if len(points_in_radius) >= min_pts:
                for point in points_in_radius:
                    if point in unused_points:
                        frontier.append(point)
                        unused_points.remove(point)
                        
        if len(current_cluster) > 1:
            clusters.append(current_cluster)
        else: # len(current_cluster) == 1
            outliers.append(current_cluster[0])
    
    cluster_no = 1
    for cluster in clusters:
        draw_plot(
            cluster,
            "#{:0>6}".format(hex(randrange(0, 256 ** 3))[2:]),
            50,
            0.8,
            "cluster {}".format(cluster_no)
        )
        cluster_no += 1
    
    draw_plot(outliers, "black", 5, 1, "outliers")    
    
    print("Total clusters: {}".format(len(clusters)))
    print("Outliers: {} out of {}".format(len(outliers), len_data))
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.legend()
    plt.show()