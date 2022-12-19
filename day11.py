## part 1 ##
monkies = (
    {0:
       {
        'items':[57],
        'op':lambda old: old * 13,
        'test':lambda x: 3 if not x % 11 else 2,
        'divisor':11
       },
     1: 
       {
        'items':[58, 93, 88, 81, 72, 73, 65],
        'op':lambda old: old + 2,
        'test':lambda x: 6 if not x % 7 else 7,
        'divisor':7
       },
     2: 
       {
        'items':[65, 95],
        'op':lambda old: old + 6,
        'test':lambda x: 3 if not x % 13 else 5,
        'divisor':13
       },
     3: 
       {
        'items':[58, 80, 81, 83],
        'op':lambda old: old * old,
        'test':lambda x: 4 if not x % 5 else 5,
        'divisor':5
       },
     4: 
       {
        'items':[58, 89, 90, 96, 55],
        'op':lambda old: old + 3,
        'test':lambda x: 1 if not x % 3 else 7,
        'divisor':3
       },
     5: 
       {
        'items':[66, 73, 87, 58, 62, 67],
        'op':lambda old: old * 7,
        'test':lambda x: 4 if not x % 17 else 1,
        'divisor':17
       },
     6: 
       {
        'items':[85, 55, 89],
        'op':lambda old: old + 4,
        'test':lambda x: 2 if not x % 2 else 0,
        'divisor':2
       },
     7: 
       {
        'items':[73, 80, 54, 94, 90, 52, 69, 58],
        'op':lambda old: old + 7,
        'test':lambda x: 6 if not x % 19 else 0,
        'divisor':19
       }
    }
)

from math import prod
from copy import deepcopy

def monkey_business(monkies,rounds,calming_func=lambda x:x//3):
    processed = {i:0 for i in range(8)}
    for round in range(rounds):    
        for monkey_num in range(0,8):
            monkey = monkies[monkey_num]
            test = monkey['test']
            op = monkey['op']
            items = monkey['items']
            # divisors = [mnk['divisor'] for n,mnk in monkies.items()]
            while items:
                worry_level = items.pop(0)
                new_worry_level  = calming_func(op(worry_level))
                pass_to = test(new_worry_level)
                monkies[pass_to]['items'] = (
                    [new_worry_level] + monkies[pass_to]['items']
                )
                processed[monkey_num] += 1
                
    a,b = sorted(list(processed.values()),reverse=True)[0:2]
    return a*b

print(monkey_business(deepcopy(monkies),20))

def divisor_prods(x):
    divisors = [mnk['divisor'] for n,mnk in monkies.items()]    
    return x % prod(divisors)
## part 2 - cheated by looking up the trick to modulo by prod of test
## divisors.  I hate the "find the math trick" problems so I'm just not
## going to do them any more.
print(monkey_business(deepcopy(monkies),10_000,calming_func=divisor_prods))