names = ['mark', 'henry', 'matthew', 'paul', 'robert', 'joseph', 'carl', 'luke', 'robert', 'joseph', 'carl', 'michael',
         'mark', 'henry', 'matthew', 'ada', 'grace', 'susan', 'hedy', 'radia']

letter_counts = {}
for x in names:
    if x in letter_counts:
        letter_counts[x] = letter_counts[x] + 1
    else:
        letter_counts[x] = 1

print(letter_counts)
