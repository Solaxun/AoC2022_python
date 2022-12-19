data = open('day9.txt').read().splitlines()
moves = {'U':(-1,0),'D':(1,0),'L':(0,-1),'R':(0,1)}
steps = [[moves[m],int(d)] for m,d in [d.split() for d in data]]

def dist1(head,tail):
    return sum(map(lambda x,y: abs(x-y),head,tail)) == 1

def overlaps(head,tail):
    return head == tail
    
def is_diagonal(head,tail):
    return list(map(lambda x,y: abs(x-y),head,tail)) == [1,1]

def touching(head,tail):
    return is_diagonal(head,tail) or dist1(head,tail) or overlaps(head,tail)

def move(head,dir):
    return tuple(map(lambda x,y:x+y,head,dir))

def catch_up(tail,head):
    dist = tuple(map(lambda x,y: x-y,head,tail))    
    adj_move = position_before(dist)
    return move(tail,adj_move)

def opposite_sign(num):
    return 1 if num < 0 else -1

def position_before(move):
    return tuple(m + opposite_sign(m) if abs(m) > 1 else m for m in move)

def move_snake(snake): 
    head = snake.pop()
    new_snake = [head]
    while snake:
        prev = snake.pop()
        if not(touching(prev,head)):
            prev = catch_up(prev,head)
        new_snake = [prev] + new_snake
        head = prev
    return new_snake

def solve(snake_size=2):
    snake = [[0,0] for i in range(snake_size)]
    tail_visited = {(0,0)}
    for dir,nsteps in steps:
        for n in range(nsteps):
            prev,head = snake[-2:]
            new_head = move(head,dir)
            if not(touching(new_head,prev)):            
                snake = move_snake(snake[0:-1]+[new_head])
            else:
                snake.pop()
                snake.append(new_head)
            tail_visited.add(tuple(snake[0]))
    return len(tail_visited)

print(solve(snake_size=2))
print(solve(snake_size=10))