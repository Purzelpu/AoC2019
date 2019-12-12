def euclid(a,b):
    if not b:
        return a
    else:
        return euclid(b, a%b)

def kgV(a,b):
    return a//euclid(a,b)*b

def total_energy(moonsX, moonsY, moonsZ):
    energy = 0
    for i in range(4):
        x,dx = moonsX[i]
        y,dy = moonsY[i]
        z, dz = moonsZ[i]
        energy = energy + sum(map(abs, [x, y,z])) * sum(map(abs, [dx, dy, dz]))
    return energy

def find_period(moons):
    start = moons[:]
    simulate_step(moons)
    i = 1
    while moons != start:
        simulate_step(moons)
        i = i +1
    return i


def simulate_step(moons):
    n = len(moons)
    for i in range(n):
        for j in range(i+1,n):
            posA, velA = moons[i]
            posB, velB = moons[j]
            dv = posB - posA
            if dv:
                dv = dv//abs(dv)
            velA = velA + dv
            velB = velB - dv
            moons[i] = (posA, velA)
            moons[j] = (posB, velB)
    for i in range(n):
        posA, velA = moons[i]
        posA = posA + velA
        moons[i] = posA, velA

with open('moons') as f:
    moonsX = []
    moonsY = []
    moonsZ = []
    for line in f:
        line = line[1:-2]
        line = line.split(',')
        coords = []
        for x in line:
            equal = x.find('=')
            number = x[equal+1:]
            coords.append(int(number))
        moonsX.append((coords[0], 0))
        moonsY.append((coords[1], 0))
        moonsZ.append((coords[2], 0))
    print([moonsX, moonsY, moonsZ])
    #for i in range(1000):
    #    simulate_step(moonsX)
    #    simulate_step(moonsY)
    #    simulate_step(moonsZ)
    #print(total_energy(moonsX, moonsY, moonsZ))
    period = list(map(find_period, [moonsX, moonsY, moonsZ]))
    print(period)
    a = kgV(period[0], period[1])
    print(kgV(a, period[2]))
