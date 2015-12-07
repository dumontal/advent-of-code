#!/usr/bin/env python

import re, sys, itertools

def parse_line(line):
    m = re.match(r'(\w+) to (\w+) = (\d+).*', line)
    return ( m.group(1), m.group(2), int(m.group(3)) )

def distance_between(src, dst, city_routes):
    for route in city_routes:
        if (src in route) and (dst in route):
            return route[2]

    print('ERROR: Distance between', src, 'and', dst, 'not found.')
    sys.exit(1)

def path_distance(path, city_routes):
    distance = 0
    for i in range(len(path) - 1):
        distance += distance_between(path[i], path[i + 1], city_routes)

    return distance

def compute_path(cities_to_visit, city_routes, reduce_op):
    compute = lambda path: path_distance(path, city_routes)
    return reduce_op(map(compute, itertools.permutations(cities_to_visit)))

if __name__ == '__main__':
    cities = set()
    routes = set()

    f = open('data')
    for line in f:
        route = parse_line(line)

        cities.add(route[0])
        cities.add(route[1])
        routes.add(route)

    f.close()

    # Route procesing
    print('Minimum distance is:', compute_path(cities, routes, min))
    print('Maximum distance is:', compute_path(cities, routes, max))
