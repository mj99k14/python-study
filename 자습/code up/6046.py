# n = 5
# print(n<<1)  #10을 2배 한 값인 20 이 출력된다.
# print(n>>1)  #10을 반으로 나눈 값인 5 가 출력된다.
# print(n<<2)  #10을 4배 한 값인 40 이 출력된다.
# print(n>>2)  #10을 반으로 나눈 후 다시 반으로 나눈 값인 2 가 출력된다.
# print(n<<3) <<2 <<3 <<4 #2배수
# (>>/1 /2) (>>2 /4)
a,b=map(int,input().split())
if a < b:
    print(True)
else:
    print(False)