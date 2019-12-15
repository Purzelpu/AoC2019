import re
import math

letter = re.compile("(\d+) (\D+)")

def parse_chemical(chem):
    index = re.search(letter,chem)
    quantity = int(index.group(1))
    name = index.group(2).strip()
    return quantity, name

def calculate_resources(demand, reactions):
    demand_new = {}
    for k in demand:
        try:
            reagents, quantity = reactions[k]
        except:
            try:
                demand_new[k] = demand_new[k] + demand[k]
            except:
                demand_new[k] = demand[k]
            continue
        if quantity < 0:
            demands_new[k] = quantity
        else:
            runs = math.ceil(demand[k] / quantity)
            for amount,chem in reagents:
                try:
                    demand_new[chem] = demand_new[chem] + amount*runs
                except:
                    demand_new[chem] = amount * runs
            produced = runs * quantity
            surplus = demand[k] - produced
            try:
                demand_new[k] = demand_new[k] + surplus
            except:
                demand_new[k] = surplus
    chemicals_in_demand = list(filter(lambda x : (x!='ORE' and demand_new[x] > 0), demand_new.keys()))
    if chemicals_in_demand:
        return calculate_resources(demand_new, reactions)
    else:
        return demand_new

with open('input14') as f:
    reactions = {}
    for line in f:
        reagents = line.split('>')
        outp = reagents[1].strip()
        quantity, name = parse_chemical(outp)
        inp = reagents[0]
        inp = inp[:-1]
        inp = inp.split(',')
        required = []
        for chem in inp:
            required.append(parse_chemical(chem))
        reactions[name] = (required, quantity)
    res = calculate_resources({'FUEL': 1}, reactions)
    print(res['ORE'])
    fuel = 1000000000000 // res['ORE']
    res = calculate_resources({'FUEL': fuel}, reactions)
    print(res['ORE'])
    fuel = round(1.243716*fuel)
    res = calculate_resources({'FUEL': fuel}, reactions)
    print(res['ORE'])
    while res['ORE']< 1000000000000:
        fuel = fuel + 1
        res = calculate_resources({'FUEL': fuel}, reactions)
    print(fuel-1)
