s = []
for _ in range(5):
    s.append(int(input()))
sums = sum(s) / 5
s.sort(reverse=True)  
third_largest = s[2]
print(int(sums))
print(third_largest)
