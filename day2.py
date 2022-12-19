##### quick and dirty #####
data = open('day2.txt').read().splitlines()

## part 1 - lord forgive me for I have sinned.
score = 0
for round in data:
    you,me = round.split()
    if me == 'X':
        score += 1
        if you == 'C':
            score += 6
        elif you == 'A':
            score += 3            
    elif me == 'Y':
        score += 2
        if you == 'A':
            score += 6
        elif you == 'B':
            score += 3
    elif me == 'Z':
        score += 3
        if you == 'B':
            score += 6
        elif you == 'C':
            score += 3

    
print(score)

## part 2 - partial atonement
score = 0
losing_move = {'A':3,'B':1,'C':2}
draw_move   = {'A':1,'B':2,'C':3}
win_move   =  {'A':2,'B':3,'C':1}

for round in data:
    you,me = round.split()
    
    if me == 'X':
        # need to lose, if they have A (rock), you pick Y (paper)
        score += losing_move[you]
    elif me == 'Y':
        score += 3
        score += draw_move[you]      
    else:
        score += 6
        score += win_move[you]
   
print(score)

##### refactored #####
data = open('day2.txt').read().splitlines()
RPS = 'ABCXYZ'

## part 1
def draw(me,you): 
    return RPS.index(me) % 3 == RPS.index(you)

def win(me,you):
    me  = RPS.index(me) % 3
    you = RPS.index(you)
    if me == 0:
        return 1 if you == 2 else 0
    if me == 1:
        return 1 if you == 0 else 0
    if me == 2:
        return 1 if you == 1 else 0
    
def outcome_score(me,you):
    if draw(me,you):
        return 3
    elif win(me,you):
        return 6
    return 0

def move_score(me):
    return RPS.index(me) % 3 + 1

total_score = 0
for round in data:
    you,me = round.split()
    total_score += outcome_score(me,you) + move_score(me)  
    
print(total_score)

## part 2
total_score = 0
ldw = {'A':{'W':'Y','L':'Z','D':'X'},
       'B':{'W':'Z','L':'X','D':'Y'},
       'C':{'W':'X','L':'Y','D':'Z'}}

for round in data:
    you,me = round.split()
    objective = {'X':'L','Y':'D','Z':'W'}.get(me)
    me = ldw[you][objective]
    total_score += outcome_score(me,you) + move_score(me)
    
print(total_score)