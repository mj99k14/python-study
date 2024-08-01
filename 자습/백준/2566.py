
s = []
for i in range(9):
    row = [input().split() for _ in range(9)]
    s.append(int(row))

max_value = max(max(row) for row in s1)
print(max_value)


