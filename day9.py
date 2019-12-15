import operator
import itertools

def parameters(x):
    if x < 3:
        return 3
    if 3 <= x <= 4:
        return 1
    if 5 <= x <= 6:
        return 2
    if 7 <= x <= 8:
        return 3
    if x == 9:
        return 1
    if x == 99:
        return 0
    raise ValueError(x)

def calculate(program, value):
    noun = value // 100
    verb = value % 100
    program[1] = noun
    program[2] = verb
    run(program)
    return program[0]

def run(program, inp ):
    out = []
    counter = 0
    base = 0
    while counter < len(program):
        #print("Counter: {0}".format(counter))
        #print("State: {0}".format(program))
        opMem = program[counter]
        opCode = opMem % 100
        opMem = opMem // 100
        params = [] #Addresses of parameters
        for i in range(1,parameters(opCode)+1):
            if opMem % 10 == 1:
                params.append(counter+i)
            elif opMem % 10 == 2:
                params.append(base+program[counter+i])
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
            #op = input
            #program[params[0]] = int(op())
            #program[params[0]] = 1
            program[params[0]] = next(inp)
        if opCode == 4:
            #op = print
            #op(program[params[0]])
            yield program[params[0]]
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
        if opCode == 9:
            base = base + program[params[0]]
        if opCode == 99:
            return None
    return None

def thruster(program, phase):
    inp = 0
    for x in phase:
        out = run(program[:],iter([x, inp]))
        inp = next(out)
    return inp

def recursive_thruster(program, phase):
    inp = []
    for x in phase:
        inp.append([x])

    prog = []
    for x in inp:
        prog.append(run(program[:],iter(x)))

    inp[0].append(0)

    for x in prog[0]:
        inp[1].append(x)
        inp[2].append(next(prog[1]))
        inp[3].append(next(prog[2]))
        inp[4].append(next(prog[3]))
        out = next(prog[4])
        inp[0].append(out)
    return out

with open('input9') as f:
    #prog = test
    prog = f.read()
    prog = prog.split(',')
    prog = list(map(int, prog))
    prog.extend([0]*10000)
    for x in run(prog, iter([1])):
        print(x)
