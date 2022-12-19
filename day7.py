from collections import defaultdict

data = open('day7.txt').read().splitlines()
pwd = []
filesystem = defaultdict(list)

## decision to represent fsystem as a flatmap of path->files
## helped avoid the need to explicitly model a tree.
for instr in data:
    a,b,*c = instr.split()
    if instr.startswith('dir'):
        fullpath = tuple(pwd+[b])
        filesystem[fullpath]
    elif instr.startswith('$ cd') and c[0] == '..':
        pwd.pop()
    elif instr.startswith('$ cd'):
        pwd.append(c[0])     
    elif instr.startswith('$ ls'):
        continue
    else:
        fsize,fname = a,b
        fsize = int(fsize)
        filesystem[tuple(pwd)].append((fname,fsize))

def get_subdirs(path,filesystem):
    subdirs = []
    for filepath in filesystem:
        pathlen = len(path)
        if filepath[0:pathlen] == path[0:pathlen] and filepath != path:
            subdirs.append(filepath)
    return subdirs
  
total_dirsizes = {}
for directory,files in filesystem.items():
    directory_size = 0    
    for file in files:
        fname,fsize = file
        directory_size += fsize
    children = get_subdirs(directory,filesystem)
    for child in children:
        files = filesystem[child]
        directory_size += sum(f[1] for f in files)
    total_dirsizes[directory] = directory_size

## part 1
small = sum(sz for d,sz in total_dirsizes.items() if sz <= 100_000)      
print(small)

## part 2
total_filesystem_size = 70_000_000
update_filesize = 30_000_000
available_space = total_filesystem_size - total_dirsizes[('/',)]
needed_space = update_filesize - available_space

deletion_candidates = []
for d,sz in total_dirsizes.items():
    if sz >= needed_space:
        deletion_candidates.append(sz)

print(min(deletion_candidates))