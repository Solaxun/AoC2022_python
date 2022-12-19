import re
from collections import defaultdict

data = """Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II"""

pat = 'Valve ([A-Z]{2}) has flow rate=(\d+); tunnels? leads? to valves? (.*)'
valve_map =  defaultdict(list)
valve_flow_rates = {}

for from_valve,flow_rate,to_valves in re.findall(pat,data):
    valve_map[from_valve].extend(to_valves.split(','))
    valve_flow_rates[from_valve] = int(flow_rate)
# min to open, min to go to another valve

    ### NO IDEA WHERE TO BEGIN ####
ALL_RELEASED = []
OPEN = 0
CLOSED = 1

def mario(valve,released=0,time=30,closed=None):
    print(valve,released,time,closed,id(closed))
    if closed is None:
        closed = set()
    if time <= 0:
        ALL_RELEASED.append(released)
        return
        
    connected = set(valve_map[valve]) - closed 
    for status in [CLOSED,OPEN]:            
        time -= status
        for c in connected:
            released = valve_flow_rates[valve] * time
            # this is a bug, gets mutated by subsequent calls.  
            # instead, recursively call with new set, don't assign
            # intermediate value
            closed = closed|{valve} if status == CLOSED else closed
            mario(c,released,time - 1,closed)    

mario('AA')
print(ALL_RELEASED)