from functools import reduce

def increasing(n):
    num = [int(x) for x in str(n)]
    adjacent = zip(num, num[1:])
    return reduce(lambda x,y : x and y[0] <= y[1], adjacent, True)

def equal_digits(n):
    num = [int(x) for x in str(n)]
    adjacent = zip(num, num[1:])
    return reduce(lambda x,y : x or y[0] == y[1], adjacent, False)

def count_adjacent(n):
    num = [int(x) for x in str(n)]
    adj = []
    pos = 0
    start = 0
    while pos < len(num):
        while pos + 1 < len(num) and num[pos] == num[pos+1]:
            pos = pos + 1
        pos = pos + 1
        adj.append(pos-start)
        start = pos
    return adj

print(increasing(111111))
print(equal_digits(111111))

print(increasing(223450))
print(equal_digits(123789))

low = 264360
high = 746325
numbers = range(low,high+1)
numbers = filter(increasing, numbers)
numbers = filter(lambda x : 2 in count_adjacent(x), numbers)
#numbers = filter(equal_digits, numbers)
print(len(list(numbers)))

print(2 in count_adjacent(11122344))
