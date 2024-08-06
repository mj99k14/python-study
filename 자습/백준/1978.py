# N =int(input())
# s = list(map(int,input().split()))
# c = 0


# for i in s:


#     if s[i] % i ==0:
#         c += 1
# print(c)


n = int(input())
s = list(map(int, input().split()))
r = 0 #소수의 개수를 저장할 변수

for a in s:
    x = 0 # 약수개수를 세기위해
    if a > 1:
        for i in range(2, a):
            if a % i == 0:
                x += 1
        
        if x == 0: # 소수가 맞으니깐 
               r += 1