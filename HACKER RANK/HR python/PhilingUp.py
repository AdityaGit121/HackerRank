from collections import deque

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    cubes = deque(map(int, input().split()))
    top = float('inf')
    possible = True
    while cubes:
        # pick the larger of the two ends
        if cubes[0] >= cubes[-1]:
            pick = cubes.popleft()
        else:
            pick = cubes.pop()
        # check if it can be placed on the pile
        if pick > top:
            possible = False
            break
        top = pick
    print("Yes" if possible else "No")