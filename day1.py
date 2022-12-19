#### quick and dirty ####
elves = open('day1.txt').read().split('\n\n')

biggest = 0
all_elves = []
for elf in elves:
    s = sum(int(e) for e in elf.split('\n'))
    biggest = max(s,biggest)
    all_elves.append(s)
print(biggest)

print(sum(sorted(all_elves,reverse=True)[0:3]))

#### refactored ####
elves = open('day1.txt').read().split('\n\n')
totals = [sum(map(int,group.split('\n'))) for group in elves]

print(max(totals))
print(sum(sorted(totals,reverse=True)[0:3]))