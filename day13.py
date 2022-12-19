from itertools import zip_longest
from functools import cmp_to_key,reduce
from operator  import mul

data = open('day13.txt').read().split('\n\n')

def compare_list(l1,l2):
    if (not l1) and l2:
        return True
    if (not l2) and l1:
        return False
    for a,b in zip(l1,l2):
        r = compare(a,b)
        if r is not None:
            return r
    if len(l1) < len(l2):
        return True
    if len(l1) > len(l2):
        return False
               
def compare(a,b):
    if type(a) == list and type(b) == list:
        return compare_list(a,b)
    elif type(a) == list and type(b) != list:
        return compare_list(a,[b])
    elif type(a) != list and type(b) == list:
        return compare_list([a],b)
    elif a < b:
        return True
    elif a > b:
        return False

right_order = 0
for i,pair in enumerate(data,start=1):
    a,b = map(eval,pair.split())
    if compare(a,b):
        right_order += i
print(right_order)

packets = [[[2]], [[6]]]
for pair in data:    
    packets.extend(map(eval,pair.split('\n')))

def order_packets(a,b):
    c = compare(a,b)
    if c == True:
        return -1
    elif c == False:
        return 1
    else:
        return 0
    
sorted_packets = sorted(packets,key=cmp_to_key(order_packets))
res = [i for i,p in enumerate(sorted_packets,start=1) 
       if p == [[2]] or p == [[6]]]
print(reduce(mul,res))


## first element of [] in l1 is smaller than first element of '6'
## which gets converted to '[6]' in l2, so the whole l1 is smaller.
print(compare([[],1],[6]))

## had a nasty bug where the list comparator used zip_longest
## with a fill value of -100, which blows up for cases like this:
print(compare([2], [2,[]]))
## zip_longest returns: [([2],2) (-1,[])]
## first pair [2] v 2 -> [2] [2] same so continue
## but here we should stop bc left side ran out, but bc of 
## zip longest we compare -1 (ran out) to [], which converts
## to [-1] vs [] which shows right side shorter when left side
## was.  Zip longest breaks down when the longer list has an
## empty list, because the shorter list ends up comparing -1
## to the empty list on the right, resulting in coercion to [-1]
## vs the empty list on the right, so now the original empty list
## is no longer empty and the right side appears shorter incorreclty.


# cant rely on len if first list has a smaller element but is longer
# if weren't using zip longest
print(compare([1,2,3],[4]))
print(compare([2], 
              [2, []]
             ))
# [] 6 --> [] [6] --> a empty so true
# 1 -100

## before comparing length ,need  to make sure no element is smaller