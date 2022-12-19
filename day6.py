##### quick and dirty #####
data = open('day6.txt').read()

for i in range(len(data)-14): # replace 14 w/ 4 for part 1
    s = set(data[i:i+14])
    if len(s) == 14:
        print(i,i+14,s)
        break
        
##### refactored #####
def find_marker(signal,n):
    return [i+n for i in range(len(data)-n) if len(set(data[i:i+n])) == n][0]
    
print(find_marker(data,4))
print(find_marker(data,14))