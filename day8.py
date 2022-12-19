##### quick and dirty #####
def neighbors(board,pos):
    def in_bounds(r,c):
       return 0 <= r < len(board) and 0 <= c < len(board[0])
        
    res = []
    for dir in [[1,0],[0,1],[-1,0],[0,-1]]:
        nbors = []
        curpos = pos
        while in_bounds(*curpos):
            curpos = list(map(lambda a,b:a+b,curpos,dir))
            if in_bounds(*curpos): # clean up.. dbl check
                nbors.append(curpos)
        res.append(nbors)
    return res

board = open('day8.txt').read().splitlines()
board = [[int(c) for c in row] for row in board]

# perimeter
visible = len(board[0]) * 2 + (len(board) - 2) * 2

# part 1
for rix in range(1,len(board)-1):
    for cix in range(1,len(board[0])-1):
        nbors = neighbors(board,[rix,cix])
        tree = board[rix][cix]
        for n in nbors:
            if all(tree > board[r][c] for r,c in n):                
                visible += 1
                break

## part 2
def count_visible(tree_size,neighbors):
    count = 0
    for n in neighbors:
        r,c = n
        other_tree = board[r][c]
        if tree_size <= other_tree:
            count += 1
            return count
        else:
            count += 1
    return count

best_visibility = 0

for rix in range(0,len(board)):
    for cix in range(0,len(board[0])):
        nbors = neighbors(board,[rix,cix])
        tree = board[rix][cix]

        visibility = 1
        for n in nbors:             
            visibility *= count_visible(tree,n)
        if visibility > best_visibility:
            best_visibility = visibility
            
# if any(map(lambda n:all(tree > board[r][c] for r,c in n),
#        nbors)):                

print(best_visibility)
