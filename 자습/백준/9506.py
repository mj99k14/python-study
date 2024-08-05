
# n = int(input())
# s = []
# for i in range(1,n):
#     if n % i == 0:
#         s.append(i)
# sum_s = sum(s) 
# if sum_s == n:
#     print(n,"=","+".join(str(i) for i in sum_s), sep="")   
# elif sum_s > n:
#     print(n, "is NOT perfect.")
# else:
#     pass

while True:
    n = int(input())
    if n == -1:
        break
    s = []
    for i in range(1, n):  # n을 제외한 약수를 찾기 위해 n까지 포함하지 않음
        if n % i == 0:
            s.append(i)
    sum_s = sum(s)  # 약수들의 합을 계산
    if sum_s == n:
        print(n, " = ", " + ".join(str(i) for i in s), sep="")  # 약수들을 문자열로 변환하여 출력
    else:
        print(n, "is NOT perfect.")
