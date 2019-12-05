import operator
def parameters(x):
    if x < 3:
        return 3
    if 3 <= x <= 4:
        return 1
    if 5 <= x <= 6:
        return 2
    if 7 <= x <= 8:
        return 3
    if x == 99:
        return 0

def calculate(program, value):
    noun = value // 100
    verb = value % 100
    program[1] = noun
    program[2] = verb
    return run(program)

def run(program):
    counter = 0
    while counter < len(program):
        #print("Counter: {0}".format(counter))
        #print("State: {0}".format(program))
        opMem = program[counter]
        opCode = opMem % 100
        opMem = opMem // 100
        params = [] #Addresses of parameters
        for i in range(1,parameters(opCode)+1):
            if opMem % 10:
                params.append(counter+i)
            else:
                params.append(program[counter+i])
            opMem = opMem // 10

        counter = counter + 1 + len(params)
        if opCode == 1:
            op = operator.add
            program[params[2]] = op(program[params[0]],program[params[1]])
        if opCode == 2:
            op = operator.mul
            program[params[2]] = op(program[params[0]],program[params[1]])
        if opCode == 3:
            op = input
            #program[params[0]] = int(op())
            #program[params[0]] = 1
            program[params[0]] = 5
        if opCode == 4:
            op = print
            op(program[params[0]])
        if opCode == 5:
            if program[params[0]] != 0:
                counter = program[params[1]]
        if opCode == 6:
            if program[params[0]] == 0:
                counter = program[params[1]]
        if opCode == 7:
            if program[params[0]] < program[params[1]]:
                program[params[2]] = 1
            else:
                program[params[2]] = 0
        if opCode == 8:
            if program[params[0]] == program[params[1]]:
                program[params[2]] = 1
            else:
                program[params[2]] = 0
        if opCode == 99:
            return program[0]

        opCode = program[counter]

    return program[0]

test = "3,9,8,9,10,9,4,9,99,-1,8"
with open('input') as f:
    #prog = test
    prog = f.read()
    prog = prog.split(',')
    prog = list(map(int, prog))
    run(prog)
