# 자연수N을입력받아서, 지정된패턴으로별(*)을출력한다
N=int(input("입력: "))
#  ① 첫번째줄부터N번째줄까지별의개수를1씩증가시킨다
# 반복 (count)
# count * "*"
for i in range(1, N+1):
    print("*" *i )
for i in range(N-1,0,-1):
    print("*" * i)
#  ② N번째줄이후부터는별의개수를감소시켜마지막줄에는별1개를출력한다