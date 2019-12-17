import Intcode
import sys

def findIntersections(image, width):
    intersections = []
    for i in range(width+1,len(image)-width):
        if image[i] == '#' and image[i-width] == '#' and image[i+width] == '#' and image[i-1] == '#' and image[i+1] == '#':
            intersections.append(i)
    return intersections

def calculateAlignmentParameter(x, width):
    line = x // width
    column = x % width
    return line*column

with open('input17') as f:
    prog = f.read()
    prog = prog.split(',')
    prog = list(map(int, prog))
    prog.extend([0]*3000)

    robot = Intcode.Robot17(prog, iter([]))
    robot.run()
    for c in robot.camera:
        sys.stdout.write(c)
    width = robot.camera.index('\n')+1
    intersections = findIntersections(robot.camera, width)
    print(intersections)
    print(sum(map(lambda x: calculateAlignmentParameter(x, width), intersections)))

    #AABCBCBCAC
    #A: R6L8R8
    #B: R4R6R6R4R4
    #C: L8R6L10L10
    movement = map(ord, 'A,A,B,C,B,C,B,C,A,C\nR,6,L,8,R,8\nR,4,R,6,R,6,R,4,R,4\nL,8,R,6,L,10,L,10\nn\n')
    prog[0] = 2
    robot = Intcode.Robot17(prog, movement)
    robot.run()
    for c in robot.camera:
        sys.stdout.write(c)
    print(robot.dust)
