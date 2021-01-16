from anastruct import SystemElements
import random

ss = SystemElements()

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

nodes = [[0, 1], [1, 1]]

nodes.append(create_point(random.choice(nodes)))

del_point(nodes)


nodes = edit_point(nodes)


# ss.add_element(location=[[0, 0], [3, 4]])
# ss.add_element(location=[[3, 4], [80, 40]])

# ss.add_support_fixed(node_id=1)
# ss.add_support_fixed(node_id=3)

# ss.q_load(element_id=[1, 2], q=[1.5, -1.5])
# ss.solve()

# ss.show_structure()