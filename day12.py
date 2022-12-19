from collections import deque

data = open('day12.txt').read().splitlines()
GRID = [list(line) for line in data]

def neighbor_locs(pos):
    r,c = pos
    return [(r+d[0],c+d[1]) for d in [[0,1],[1,0],[-1,0],[0,-1]]]

## messed up here by using 'S' + alpha + 'E' originally, which
## makes S != a like the instructions said (same prob for E != z)
## this meant from S I could only go to a, when it should have been
## possible to go to both a and b.  Prob wouldn't have found w/o 
## reddit hints, bc the path returned was very,very close to the 
## correct one (same path shape, only a few moves longer)
def only_one_higher(pos,neighbor,part=1):
    pr,pc = pos
    nr,nc = neighbor
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    a = {a:i for i,a in enumerate(alpha)}
    a['S'] = 0
    a['E'] = 25
    if part == 2:
        alpha = reversed('abcdefghijklmnopqrstuvwxyz')
        a = {a:i for i,a in enumerate(alpha)}
        a['S'] = 25
        a['E'] = 0
    return a[GRID[nr][nc]] - a[GRID[pr][pc]] <= 1

def in_bounds(pos):
    r,c = pos
    return 0 <= r < len(GRID) and 0 <= c < len(GRID[0])

def p1_neighbors(pos):
    nlocs = filter(in_bounds,neighbor_locs(pos))
    onestep = filter(lambda n: only_one_higher(pos,n,part=1),nlocs)
    return onestep

def p2_neighbors(pos):
    nlocs = filter(in_bounds,neighbor_locs(pos))
    onestep = filter(lambda n: only_one_higher(pos,n,part=2),nlocs)
    return onestep
   
def bfs_search(start,goal_func,neighbor_func):
    paths, seen = deque([start]), set((start))
    while paths:
        path = paths.popleft()
        r,c = pos = path[-1]
        if goal_func(pos):
            return path     
        neighbors = neighbor_func(pos)   
        for n in neighbors:    
            if n not in seen:
                paths.append(path+[n])
                seen.add(n)    

def find_start(start):
    return [(r,c) for r,row in enumerate(GRID) 
                  for c,col in enumerate(row) 
                  if col == start]

def goal_func(goal,pos):
    return GRID[pos[0]][pos[1]] == goal

p1_goal = lambda pos: goal_func('E',pos)
p2_goal = lambda pos: goal_func('a',pos)

p1_best_path = (bfs_search(find_start('S'),p1_goal, p1_neighbors))
p2_best_path = (bfs_search(find_start('E'),p2_goal, p2_neighbors))

print(len(p1_best_path) - 1)
print(len(p2_best_path) - 1)

## visualize the best path in the grid
# def show_best_path(best_path,start):
#     empty_grid = [list('.' * len(GRID[0])) for row in GRID]
#     for p1,p2 in zip(best_path,best_path[1:]):
#         r,c = p2
#         dir = tuple(map(lambda x,y:x-y,p2,p1))
#         arrows = {(-1,0):'^',(1,0):'v',(0,-1):'<',(0,1):'>'}
#         empty_grid[r][c] = arrows[dir]
#     start_loc = find_start(start)
#     s0,s1 = start_loc[0]
#     empty_grid[s0][s1] = 'S'
#     empty_grid[r][c] = 'E'
    
#     for row in empty_grid:
#         print("".join(row))
        
# show_best_path(p1_best_path,'S')
# show_best_path(p2_best_path,'E')