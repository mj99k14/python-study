import random
n = 3

#사용자로부터 크키 입력받기 n =3~6이하
#유효하지않으면 올바른 값이 될때까지 
bingo_board = []
# bingo_board = [ 1,2,3,/
               #  4,5,6,/
                # 7,8,9]
bingp_num = n * n
#9개의 랜덤 번호를 받아요

n1 = [o for o in range(random.randint(1,37))]

#빙고판 생성 1~36  중복되지않는 정수로
while len(bingo_board) < bingp_num: 
    random_num = random.randint(1,37)
    for i in range(bingp_num):
        if random_num not in bingo_board:
            bingo_board.append(random_num)
# 빙고 출력
print(bingo_board)  
bingo_board1 = [[i for i in random_num] for s in range(n)]
print(bingo_board1)
# 난수 생성 , 일치한난수 발견하면 

# 가로,세로대각선 2줄이상이면 빙고 
 