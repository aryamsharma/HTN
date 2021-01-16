from anastruct import SystemElements
import random

def create_point(rand_node, radius_min=0, radius_max=10):
    base_x = rand_node[0]
    base_y = rand_node[1]
    rand_x = base_x + random.randint(radius_min, radius_max)
    rand_y = base_y + random.randint(radius_min, radius_max)
    return [rand_x, rand_y]

def del_point(nodes):
    del nodes[random.randint(0, len(nodes) - 1)]

def edit_point(nodes, radius_min=0, radius_max=10):
    n = random.randint(0, len(nodes) - 1)
    nodes[n][0] += random.randint(radius_min, radius_max)
    nodes[n][1] += random.randint(radius_min, radius_max)
    return nodes

def manhattan_distance_calc(node1, node2):
    return abs(node1[0] - node2[0]) + abs(node1[1] - node2[1])

def fitnees_function(nodes, start_xy, end_xy):
    max_reward = 1
    first = True

    for node in nodes:
        if first:
            first = False
            lowest_distance = manhattan_distance_calc(node, end_xy)
            continue

        tmp = manhattan_distance_calc(node, end_xy)
        if tmp <= lowest_distance:
            lowest_distance = tmp
    
    distance_max = manhattan_distance_calc(start_xy, end_xy)
    if first:
        lowest_distance = distance_max
    fitness = (-max_reward / distance_max ) * lowest_distance + max_reward

    return fitness

def modify_nodes(nodes):
    # num = random.randint(1, 3)
    # if num == 1:
    return create_point(random.choice(nodes))
    # elif num == 2:
        # del_point(nodes)
    # else:
    # nodes = edit_point(nodes)

def build_struct(nodes):
    ss = SystemElements()
    for i in range(len(nodes) - 1):
        ss.add_element(location=[nodes[i], nodes[i + 1]])

    ss.add_support_fixed(node_id=1)
    if nodes.count(end_xy) > 0:
        print("End point reached")
        ss.add_support_fixed(node_id=nodes.index(end_xy) + 1)
    
    ss.q_load(element_id=1, q=-1)
    ss.solve()
    ss.show_structure()
    ss.show_displacement()

start_xy = [0, 0]
end_xy = [100, 20]

no_gens = 10
gen_size = 100

nodes = [start_xy]

first = True

for i in range(no_gens):
    base_nodes = nodes[:]
    for i in range(gen_size):
        nodes = base_nodes[:]
        nodes.append(modify_nodes(base_nodes))
        print(nodes)

        if first:
            first = False
            highest_fitness = fitnees_function(nodes, start_xy, end_xy)
            best_nodes = nodes[:]
            

        fitness = fitnees_function(nodes, start_xy, end_xy)
        if fitness > highest_fitness:
            highest_fitness = fitness
            best_nodes = nodes[:]
    # build_struct(nodes)
    nodes = best_nodes[:]

build_struct(nodes)