def fuel(x):
    return x // 3 -2

def total_fuel(x):
    if fuel(x) <= 0:
        return 0
    return fuel(x) + total_fuel(fuel(x))


print(fuel(14))
print(total_fuel(1969))

with open('input') as f:
    mass = list(map(int, f))
    print(sum(map(fuel,mass)))
    print(sum(map(total_fuel,mass)))
