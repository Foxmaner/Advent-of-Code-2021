##Del1
lines = []
with open('data.txt') as f:
    lines = f.read().splitlines()
inc = 0
for x in range(0,len(lines)-1):
    if int(lines[x]) < int(lines[(x+1)]):
        inc = inc + 1
print(inc)