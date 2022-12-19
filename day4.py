##### quick and dirty ######
data = open('day4.txt').read().splitlines()

n = 0
for section in data:
    range1,range2 = section.split(',')
    x1,x2 = map(int,range1.split('-'))
    y1,y2 = map(int,range2.split('-'))
    a = set(range(x1,x2+1))
    b = set(range(y1,y2+1))
    if a & b == b or a & b == a: # part 1
    # if a & b: #part 2
        n += 1
print(n)

##### refactored ######
data = open('day4.txt').read().splitlines()

def make_elf_sections(data):
    return [[list(map(int,x.split('-'))) for x in d.split(',')] for d in data]
      
def subsumes(elves):
    e1,e2 = elves 
    return e1[0] >= e2[0] and e1[1] <= e2[1] or e2[0] >= e1[0] and e2[1] <= e1[1]
    
def overlaps(elves):
    e1,e2 = elves
    return e1[1] >= e2[0] and e1[1] <= e2[1] or e2[1] >= e1[0] and e2[1] <= e1[1]

def count_elves(elves,assignment_func):
    return len(list(filter(assignment_func,elves)))

elves = make_elf_sections(data)

print(count_elves(elves,subsumes))
print(count_elves(elves,overlaps))
