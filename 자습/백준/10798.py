
# s  =  [ input() for _ in range(5) ]
# result = ""
# for i in range(len(s[0])):
#     for j in range(5):
#        result += s[j][i]
# print(result)

s = [input() for _ in range(5)]

result = ""

max_length = max(len(row) for row in s)

for i in range(max_length):
    for j in range(5):
        if i < len(s[j]):
            result += s[j][i]

print(result)


words = [input() for i in range(5)]

for j in range(15):
    for i in range(5):
        if j < len(words[i]):
            print(words[i][j], end='')






