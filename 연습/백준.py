#정수 두개를 입력받는다
n,x=map(int(input().split()))
#n만큼 입력받는다
num=list(map(int(input().split())))
list_j=[]
#입력받은 n 중에 x보다 작은수를 찾아낸다
for i in range(num):
    if i <n:
        list_j.append(i)
print(list_j)