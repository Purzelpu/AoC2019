import operator
import itertools
import time
import Intcode

def hist2coord(hist):
    x = 0
    y = 0
    for m in hist:
        if m == 1:
            y = y +1
        elif m == 2:
            y = y -1
        elif m == 3:
            x = x -1
        elif m==4:
            x = x +1
    return (x,y)

with open('input15') as f:
    #prog = test
    prog = f.read()
    prog = prog.split(',')
    prog = list(map(int, prog))
    prog.extend([0]*2000)
    p = [[]]

    test = Intcode.RepairDroid(prog, iter([]))
    robots = [test]

    reachable = []

    while robots:
        robots_new = []
        for robot in robots:
            for direction in range(1,5):
                try:
                    if robot.history[-1]+direction == 3 or robot.history[-1] + direction == 7:
                        continue
                except:
                    pass
                n = iter([direction])
                test = Intcode.RepairDroid(robot.program,n)
                test.counter = robot.counter
                test.base = robot.base
                test.history = robot.history[:]
                thing = next(test)
                reachable.append(hist2coord(test.history))
                if thing == 1:
                    robots_new.append(test)
                elif thing == 2:
                    print("Found it")
                    print("Distance: {0}".format(len(test.history)))
                    oxygen = test
        robots = robots_new


    origin = hist2coord(oxygen.history)
    reachable.remove(origin)
    oxygen.history = []
    ox = [oxygen]
    time = 0
    while reachable:
        time = time + 1
        ox_new = []
        print("{0} squares without oxygen, {1} fronts". format(len(reachable), len(ox)))
        for robot in ox:
            for direction in range(1,5):
                try:
                    if robot.history[-1]+direction == 3 or robot.history[-1] + direction == 7:
                        continue
                except:
                    pass
                n = iter([direction])
                test = Intcode.RepairDroid(robot.program,n)
                test.counter = robot.counter
                test.base = robot.base
                test.history = robot.history[:]
                thing = next(test)
                x,y = hist2coord(test.history)
                x0, y0 = origin
                reachable = list(filter(lambda t : t != (x+x0,y+y0), reachable))
                if thing == 1:
                    ox_new.append(test)
        ox = ox_new
    print(time)
