from statistics import pstdev, mean
import matplotlib.pyplot as plt
from random import shuffle, randrange

def centroid(points):
    x = list(map(lambda p: p[0], points))
    y = list(map(lambda p: p[1], points))
    return (mean(x), mean(y))
    
def draw_plot(points, color, size, alpha, label, marker = None):
    x = list(map(lambda p: p[0], points))
    y = list(map(lambda p: p[1], points))
    if marker == None:
        plt.scatter(x, y, c = color, s = size, alpha = alpha, label = label)
    else:
        plt.scatter(x, y, c = color, s = size, alpha = alpha, label = label, marker = marker)

def kmeans(data, k, x_col = None, y_col = None):
    len_data = len(data)
    if len_data < k:
        print("Too few data!")
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
            
    shuffle(selected_points)
    clusters = []
    for i in range(k):
        clusters.append(selected_points[i::k])
        
    centroids = list(map(centroid, clusters))
    
    has_been_modified = True # Agar bisa dijalankan untuk pertama kali

    while has_been_modified:
        has_been_modified = False
        for i in range(k):
            # i adalah indeks cluster sebelum
            moved_point_idxs = []
            current_centroid = centroids[i]
            for j in range(len(clusters[i])):
                current_point = clusters[i][j]
                shortest_distance = std_distance(current_centroid, centroids[0])
                nearest_centroid_idx = min(
                    [i for i in range(k)],
                    key = lambda idx: std_distance(current_point, centroids[idx])
                )
                
                if nearest_centroid_idx != i:
                    if len(clusters[i]) - len(moved_point_idxs) > 1:
                        # j adalah indeks titik pada cluster sebelum
                        # nearest_centroid_idx adalah indeks cluster sesudah
                        moved_point_idxs.append(j)
                        clusters[nearest_centroid_idx].append(current_point)
            
            # moved_point_idxs terurut ke atas, dibalik agar remove tidak mengganggu urutan
            moved_point_idxs.reverse()
            
            for idx in moved_point_idxs:
                clusters[i].pop(idx)
            
            if not has_been_modified:
                has_been_modified = len(moved_point_idxs) > 0
                
        # Perbarui centroid
        centroids = list(map(centroid, clusters))
        
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
    
    draw_plot(centroids, "red", 100, 1, "centroid", "*")   
    
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.legend()
    plt.show()
    
        
    