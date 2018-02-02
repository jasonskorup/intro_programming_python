names = ['mark', 'henry', 'matthew', 'paul', 'robert', 'joseph', 'carl', 'luke', 'robert', 'joseph', 'carl', 'michael',
         'mark', 'henry', 'matthew', 'ada', 'grace', 'susan', 'hedy', 'radia']

name_counts = {}
for x in names:
    if x in name_counts:
        name_counts[x] = name_counts[x] + 1
    else:
        name_counts[x] = 1

print(name_counts)
