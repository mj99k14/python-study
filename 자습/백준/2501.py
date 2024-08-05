# n,k = map(int,input().split())
# s = []
# for i in range(1,n+1):
#     if n % i  == 0:
#         s.append(i)
# if len(s) < k :	# 약수의 개수가 K보다 작을 때
#     print(0)
# else :
#     print(s[k-1])




# n = int(input())
# s = []
# while True:
#     for i in range(1,n+1):
#         if n % i ==0:
#             s.append(i)
#             s.sort()
#             print(f"{n} = {s[i]} + {s[i]} + {s[i]}")
#         elif n % i != 0 :
#             print(f"{n} is  NOT perfect.")
#         else:
#             break



n = int(input())
s = []
for i in range(1,n+1):
    if n % i ==0:
        s.append(i)
s.sort()
sum_s = sum(s) - n 

if sum_s < n :
    print(f"{n}is NOT perfect.")
elif sum(s) == n:
    for i in s:
        print(f"{n} = {sum_s}+")      
else:
    pass