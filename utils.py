from math import sqrt




def read_graph_from_file(filename):
    routes = []
    with open(filename, 'r') as file:
        cities_no = int(file.readline())
        for i in range(cities_no):
            city_routes_string = file.readline().strip().split(',')
            city_routes = [float(route) for route in city_routes_string]
            routes.append(city_routes)
    return routes

def read_graph_from_file_with_coordinates(filename):
    routes = []
    coordinates = []
    with open(filename, 'r') as file:
        cities_no = get_nodes_from_file(file)
        for i in range(cities_no):
            line = file.readline().strip().split(' ')
            coordinates.append([float(line[1]), float(line[2])])
            routes.append([])
    for city1 in range(cities_no):
        for city2 in range(cities_no):
            routes[city1].append(get_euclidian_distance(coordinates[city1], coordinates[city2]))
    return routes

def get_euclidian_distance(a, b):
    return sqrt((b[0]-a[0])*(b[0]-a[0])+(b[1]-a[1])*(b[1]-a[1]))

def get_nodes_from_file(filename):
    nr = 0
    line = filename.readline().strip().split(':')
    while line[0].strip(' ') != 'DIMENSION':
        line = filename.readline().strip().split(':')

    nr = int(line[1])

    filename.readline()
    filename.readline()
    return nr


def result_to_file(access_mode, output_file, no_of_cities, cities_order, total_cost):
    with open(output_file, access_mode) as output:
        output.write(str(no_of_cities) + '\n')
        output.write(str(cities_order) + '\n')
        output.write(str(total_cost) + '\n')
