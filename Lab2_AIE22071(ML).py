def euclidean_dist(co_ordinate_1,co_ordinate_2):
    # (x2-x1)^2+(y2-y1)^2
    dist=0
    # itterate over the co-ordinates and calculates the distance separately 
    # for x and y co-ordinates
    for i in range(len(co_ordinate_1)):
        dist+=(co_ordinate_1[i]-co_ordinate_2[i])**2
    return dist**0.5
def manhatten_dist(co_ordinate_1,co_ordinate_2):
    # intialize distance to 0
    dist=0
    #  and calculate the ths mod of the co-ordinates seperately for x and y
    for i in range(len(co_ordinate_1)):
        dist+=abs(co_ordinate_1[i]-co_ordinate_2[i])
    return dist   
def euclidean_dist(point1, point2):
    # Euclidean distance between two points
    return ((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)**0.5

def k_nn(k, co_ordinates):
    distances = []
    # caalculates distances from the first point to all other points
    for i in range(1, len(co_ordinates)):
        dist = euclidean_dist(co_ordinates[0], co_ordinates[i])
        distances.append((dist, co_ordinates[i][2]))  
    # sort the  distances
    distances.sort()
    # takes the k smallest distances
    k_nearest = distances[:k]
    frequency_1 = sum(1 for _, label in k_nearest if label == 1)
    frequency_2 = k - frequency_1 
    if frequency_1 > frequency_2:
        return "Belongs to class 1"
    else:
        return "Belongs to class 2"

def label_encode(labels):
    # creates a dictionary 
    unique_labels = set(labels)
    # it maps each label to numeric one
    label_to_code = {}
    code = 0
    for label in unique_labels:
        label_to_code[label] = code
        code += 1
    # encode them
    encoded_labels = [label_to_code[label] for label in labels]
    return encoded_labels, label_to_code

def one_hot_encode(labels):
    unique_labels = sorted(set(labels)) 
    # dictories to create using the unique labels
    label_to_one_hot = {label: [0] * len(unique_labels) for label in unique_labels}
    # giving them position
    for i, label in enumerate(unique_labels):
        label_to_one_hot[label][i] = 1
    # encodes label
    encoded_labels = [label_to_one_hot[label] for label in labels]
    return encoded_labels, label_to_one_hot
#  knn classifier 
labels = ['cat', 'dog', 'mouse', 'dog', 'cat']
encoded_labels, label_to_code = label_encode(labels)
print(  one_hot_encode(labels))
print('Encoded Labels and Label to Code Mapping:', encoded_labels, label_to_code)
coordinates = [(1.0, 2.0, 1),(2.0, 3.0, 1),(3.0, 4.0, 1),(5.0, 6.0, 2),(6.0, 7.0, 2),(7.0, 8.0, 2)]
k = 3 
result = k_nn(k, coordinates)
print("Classification result:", result)

