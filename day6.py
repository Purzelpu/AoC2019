orbiting = {}
ROOT = 'COM'

def get_path_to_ancestor(x, ancestor):
    path = []
    while x != ancestor:
        x = orbiting[x]
        path.append(x)
    return path

def root_distance(x):
    return get_distance_to_ancestor(x, ROOT)

def get_distance_to_ancestor(x, ancestor):
    return len(get_path_to_ancestor(x, ancestor))

def distance(x,y):
    an = get_nearest_ancestor(x,y)
    return get_distance_to_ancestor(x,an) + get_distance_to_ancestor(y,an)

def get_nearest_ancestor(x,y):
    anX = get_path_to_ancestor(x, ROOT)
    anY = get_path_to_ancestor(y, ROOT)
    common_ancestors = [an for an in anX if an in anY]
    return common_ancestors[0]

with open('input') as f:
    for line in f:
        orbit = line[:-1].split(')')
        orbiting[orbit[1]] = orbit[0]
    print(sum(map(root_distance, orbiting.keys())))
    print(distance('YOU', 'SAN')-2)
