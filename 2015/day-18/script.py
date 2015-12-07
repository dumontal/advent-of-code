#!/usr/bin/env python

def parse_grid(size, part_2 = False):
    grid = [['.' for col in range(size)] for row in range(size)]
    
    f = open('data')
    i = 0
    for l in f:
        line = l.replace('\n', '')
        for j in range(len(line)):
            grid[i][j] = line[j]

        i += 1

    f.close()

    if part_2:
        ensure_corners_are_on(grid)

    return grid

def must_die(light, on_neighbours):
    return light == '#' and on_neighbours not in (2, 3)

def must_live(light, on_neighbours):
    return light == '.' and on_neighbours == 3

def simulate_steps(grid, nb_steps, part_2 = False):
    s = len(grid)
    neighbours = [[0 for col in range(s)] for row in range(s)]
    
    for step in range(nb_steps):
        compute_nb_of_on_neighbours(grid, neighbours)
        next_step(grid, neighbours)

        if part_2:
            ensure_corners_are_on(grid)

        if step % 10 == 0 and step != 0:
            print('Processed', step, 'steps...')

    state_to_int = lambda light: 1 if light == '#' else 0
    sum_over_cols = lambda row: sum(map(state_to_int, row))
    return sum(map(sum_over_cols, grid))

def ensure_corners_are_on(grid):
    s = len(grid) - 1
    grid[0][0] = '#'
    grid[0][s] = '#'
    grid[s][0] = '#'
    grid[s][s] = '#'

def next_step(grid, neighbours):
    s = len(grid) # == len(neighbours)
    for i in range(s):
        for j in range(s):
            if must_die(grid[i][j], neighbours[i][j]):
                grid[i][j] = '.'

            elif must_live(grid[i][j], neighbours[i][j]):
                grid[i][j] = '#'

def compute_nb_of_on_neighbours(grid, neighbours):
    for i in range(len(grid)):
        for j in range(len(grid)):
            neighbours[i][j] = nb_of_on_neighbours(grid, i, j)

def nb_of_on_neighbours(grid, i, j):
    on_neighbours = 0
    for row, col in generate_neighbours_coords(i, j, len(grid)):
        if grid[row][col] == '#':
            on_neighbours += 1

    return on_neighbours

def generate_neighbours_coords(i, j, size):
    i_min = max(i - 1, 0)
    i_max = min(i + 1, size - 1)
    j_min = max(j - 1, 0)
    j_max = min(j + 1, size - 1)

    for row in range(i_min, i_max + 1):
        for col in range(j_min, j_max + 1):
            if row != i or col != j:
                yield row, col

if __name__ == '__main__':

    lights = parse_grid(100)
    print('[Part 1]')
    nb_of_on_lights = simulate_steps(lights, 100)
    print('Number of on lights is:', nb_of_on_lights)
    print('')

    lights = parse_grid(100, part_2 = True)
    print('[Part 2]')
    nb_of_on_lights = simulate_steps(lights, 100, part_2 = True)
    print('Number of on lights is:', nb_of_on_lights)
