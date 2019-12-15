import operator

class Intcode:
    def __init__(self, program, inp):
        self.counter = 0
        self.base = 0
        self.input = inp
        self.program = program[:]

    def parameters(self, x):
        if 1<= x < 3:
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

    def step(self):
        #print("Counter: {0}".format(self.counter))
        #print("State: {0}".format(self.program))
        opMem = self.program[self.counter]
        opCode = opMem % 100
        opMem = opMem // 100
        params = [] #Addresses of parameters
        for i in range(1,self.parameters(opCode)+1):
            if opMem % 10 == 1:
                params.append(self.counter+i)
            elif opMem % 10 == 2:
                params.append(self.base+self.program[self.counter+i])
            else:
                params.append(self.program[self.counter+i])
            opMem = opMem // 10

        self.counter = self.counter + 1 + len(params)
        if opCode == 1:
            op = operator.add
            self.program[params[2]] = op(self.program[params[0]],self.program[params[1]])
        if opCode == 2:
            op = operator.mul
            self.program[params[2]] = op(self.program[params[0]],self.program[params[1]])
        if opCode == 3:
            #op = input
            #program[params[0]] = int(op())
            #self.program[params[0]] = 1
            #print('reading Input')
            got = next(self.input)
            self.history.append(got)
            #print(got)
            self.program[params[0]] = got
        if opCode == 4:
            #op = print
            #op(self.program[params[0]])
            return self.program[params[0]]
        if opCode == 5:
            if self.program[params[0]] != 0:
                self.counter = self.program[params[1]]
        if opCode == 6:
            if self.program[params[0]] == 0:
                self.counter = self.program[params[1]]
        if opCode == 7:
            if self.program[params[0]] < self.program[params[1]]:
                self.program[params[2]] = 1
            else:
                self.program[params[2]] = 0
        if opCode == 8:
            if self.program[params[0]] == self.program[params[1]]:
                self.program[params[2]] = 1
            else:
                self.program[params[2]] = 0
        if opCode == 9:
            self.base = self.base + self.program[params[0]]
        if opCode == 99:
            print('END')
        return None

    def run(self):
        while self.program[self.counter] != 99:
            x = self.step()
            if x != None:
                print('OUTPUT: {0}'.format(x))

    def __next__(self):
        x = None
        while x == None:
            x = self.step()
        return x

    def __iter__(self):
        return self

class RepairDroid(Intcode):
    def __init__(self, program, inp):
        Intcode.__init__(self, program, inp)
        self.history = []
