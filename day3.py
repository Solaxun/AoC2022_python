##### quick and dirty #####
data = open('day3.txt').read().splitlines()
alpha = 'abcdefghijklmnopqrstuvwkyz'
priorities = alpha+alpha.upper()

## part1
total = 0
for rucksack in data:
    half = len(rucksack)//2
    first_half = rucksack[0:half]
    second_half = rucksack[half:]
    in_both = set(first_half) & set(second_half)
    p = priorities.index(in_both.pop()) + 1
    total += p
print(total)

## part 2
total = 0
groups = [data[i:i+3] for i in range(0,len(data),3)]
shared = [set.intersection(*map(set,g)) for g in groups] 
for s in shared:
    p = priorities.index(s.pop()) + 1
    total += p
print(total)

##### refactored #####
data = open('day3.txt').read().splitlines()
alpha = 'abcdefghijklmnopqrstuvwkyz'
priorities = alpha+alpha.upper()

def partition(n,xs):
    return [xs[i:i+n] for i in range(0,len(xs),n)]

def halve(xs):
    return partition(len(xs)//2,xs)

## part 1
intersections = [set.intersection(*map(set,halve(rucksack))) for rucksack in data]
score = sum(priorities.index(x.pop()) + 1 for x in intersections)
print(score)

## part 2
intersections = [set.intersection(*map(set,p)) for p in partition(3,data)]
score = sum(priorities.index(x.pop()) + 1 for x in intersections)
print(score)