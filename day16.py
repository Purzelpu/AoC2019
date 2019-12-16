
def list2num(l):
    if not l:
        return 0
    return l[-1] + 10*list2num(l[0:-1])

with open('input16') as f:
    line = f.readline()
    digits = [int(x) for x in line[:-1]]
    origDigits = digits[:]
    offset = digits[0:7]
    offset = list2num(offset)

    #skip = (len(digits)//2)

    for j in range(100):
        new = []
        for i in range(0, len(digits)):
            start = i
            segmentLength = i + 1
            periode = 4*segmentLength
            #positive = []
            #for k in range(segmentLength):
            #    positive = positive + digits[start+k::periode]
            if segmentLength < len(digits)/2+1:
                positive = [digits[start+k::periode] for k in range(segmentLength)]
                positive = list(map(sum, positive))
                negative = [digits[start+k+2*segmentLength::periode] for k in range(segmentLength)]
                negative = list(map(sum, negative))
            else:
                positive=digits[i:]
                negative = []

            s = sum(positive) - sum(negative)
            if s > 0:
                new.append(s%10)
            else:
                new.append((-s)%10)
        digits = new
        print(j)
    print(list2num(digits[0:8]))

    skip = offset
    print(skip)
    print(len(digits))
    digits = origDigits*10000
    digits = digits[skip:]
    for j in range(100):
        s = 0
        for i in range(len(digits)):
            s = s + digits[-(i+1)]
            digits[-(i+1)] = s%10
        print(j)
    print(list2num(digits[0:8]))
    #print(digits)
