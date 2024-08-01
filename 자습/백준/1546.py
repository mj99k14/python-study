s = int(input())
socers = list(map(int,input().split()))
m =max(socers)
for i in range(s):
    socers[i] = socers[i] / m * 100

print(sum(socers)/s)

# print("|\_/|")
# print("|q p|   /}")
# print("( 0 )\"\"\"\\")
# print("|\"^\"`    |")
# print("||_/=\\__|")