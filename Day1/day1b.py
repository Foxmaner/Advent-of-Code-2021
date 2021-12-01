##Del2

lines = []
with open('data.txt') as f:
    lines = f.read().splitlines()
inc = 0
res = []
for x in range(0,len(lines)-2):
    res.append(int(lines[x]) + int(lines[x+1]) + int(lines[x+2]))

for x in range(0,len(res)-1):
    if int(res[x]) < int(res[(x+1)]):
        inc = inc + 1
print(inc)
