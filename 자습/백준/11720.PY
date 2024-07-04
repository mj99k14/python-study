# n= int(input())
# c = 0 
# for i in range(n):
#     s  = int(input())
#     c += s
# print(c)

# n1 = int(input())
# for i in range(n1):
#     n = list(map(int,input()))
# print(sum(n))

n = input()
nums = input()  #공백없이 받아야하기떄문에 문자열로 받음 
total = 0
for i in nums :
    total += int(i)  # total= total+int(i) 
print(total)

#두번째
n = input()
print(sum(map(int,input()))) 
