import operator

def calculate(program, value):
    noun = value // 100
    verb = value % 100
    program[1] = noun
    program[2] = verb
    return run(program)

def run(program):
    counter = 0
    opCode = program[counter]
    while opCode != 99:
        opAdd1 = program[counter+1]
        opAdd2 = program[counter+2]
        resAdd = program[counter+3]

        if opCode == 1:
            op = operator.add
        if opCode == 2:
            op = operator.mul

        program[resAdd] = op(program[opAdd1],program[opAdd2])
        counter = counter + 4
        opCode = program[counter]

    return program[0]

with open('input') as f:
    prog = f.read()
    prog = prog.split(',')
    prog = list(map(int, prog))
    print(calculate(prog[:],1202))
    x = 1000
    while calculate(prog[:],x) != 19690720:
        x = x +1
    print(x)
