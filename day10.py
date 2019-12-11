from functools import partial
import math

WIDTH = 0

def angle(relPos):
    x,y = relPos
    #normalise
    n = math.sqrt(x*x + y*y)
    x,y = x/n ,y/n
    if x >=0:
        return math.acos(-y)
    else:
        return 2*math.pi - math.acos(-y)

def ggT(x,y):
    if y == 0:
        return abs(x)
    return ggT(y, x%y)

def show_belt(beltmap):
    n = 0
    while n*WIDTH < len(beltmap):
        print(beltmap[n*WIDTH:(n+1)*WIDTH])
        n = n + 1

def count_asteroids(beltmap, position):
    return len(visible_asteroids(beltmap, position))

def visible_asteroids(beltmap, position):
    if beltmap[position] == '.':
        return []
    directions = []
    myX = position % WIDTH
    myY = position // WIDTH
    for ast in range(len(beltmap)):
        if beltmap[ast] == '.' or ast == position:
            continue
        astX = ast % WIDTH
        astY = ast // WIDTH
        dx = astX - myX
        dy = astY - myY
        d = ggT(dx, dy)
        dx = dx // d
        dy = dy // d
        #print(ast, astX, astY, dx, dy, (dx,dy) in directions)
        if not (dx,dy) in directions:
            directions.append((dx,dy))
    return directions

def acquire_target(beltmap, laserPos, direction):
    dx, dy = direction
    offset = dy * WIDTH + dx
    targetPos = laserPos +offset
    #print(laserPos, dx, dy, offset)
    while beltmap[targetPos] != '#':
        targetPos = targetPos + offset
    return targetPos

def destroy_everything(beltmap, laserPos):
    targetList = sorted(visible_asteroids(beltmap, pos),key=angle)
    while targetList:
        for targetPos in targetList:
            targetPos = acquire_target(beltmap, laserPos, targetPos)
            beltmap[targetPos] = '.'
            yield targetPos
        targetList = sorted(visible_asteroids(beltmap, pos), key=angle)


with open('input') as f:
    beltmap = []
    for line in f:
        for c in line[:-1]:
            beltmap.append(c)
    WIDTH = len(line) -1
    count = partial(count_asteroids, beltmap)
    vis_ast = list(map(count, range(len(beltmap))))
    m = max(vis_ast)
    pos = vis_ast.index(m)
    vis_ast = visible_asteroids(beltmap, pos)
    #print(sorted(vis_ast, key=angle))
    #while True:
    #    print(next(destroy_everything(beltmap,pos)))
    #    show_belt(beltmap)
    #    input()
    laser = destroy_everything(beltmap, pos)
    for i in range(1,201):
        target = next(laser)
        print(i, target, target % WIDTH, target // WIDTH)
