import random
#N값 3이상 6이하 정수 유효한 값이 입력될때까지
while True:
    N = int(input("3 ~ 6안에서 고르셈: "))
    if 3 <= N <=6:
        break
    else:
        print("다시 입력하셈")



#N*N빙고판 만들기 1차원 리스트로만
s = 36 - (N * N)  #27
bingo = [i for i in range(1,36)]
for i in range(1,s):
    del bingo[random.randint(1,s-1)]
print(bingo)

#이리스트 안에 1부터 36사이의 중복되지않은 정수
#보드판 출력
#엔터키를 누르면 난수발생 
#난수와 일치하면 *
#매 게임 횟수 출력
#랜덤으로 숫자가 만들어짐
#가로,세로,대각선 포함 최소 2개이상 *되면 끝
#2개이상 줄되면 사용자 승리
