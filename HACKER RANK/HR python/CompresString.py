from itertools import groupby
s = input().strip()
result = []
for char, group in groupby(s):
    count = len(list(group))
    result.append(f"({count}, {char})")
print(" ".join(result))