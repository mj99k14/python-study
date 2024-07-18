import random
#사용자로 부터 n값을 받는다 
n = 3
#n값은 3~6 유효하지않으면 올바른값이 입력될때 까지
#n * n 1~36 정수
#bd = [  0,1,2,\
        #3,4,5,\
        #6,7,8]
        
def print_bingo_board(arg_list, col_num):#arg_list는 빙고보드요소 리스트 ,열의수는 3
    for index in range(len(arg_list)):
        print(arg_list[index], "\t", end="")
        
        if (index + 1)  % col_num == 0: # ->3,6,9일떄 줄바꿈이 있어야하니깐
            print()

bd = n * n

bingo_board = []
while len(bingo_board) < bd:
    random_num = random.randint(1,36)
    if random_num not in bingo_board:
        bingo_board.append(random_num)
print(bingo_board)


r = random.randint(1,36)
print(r)

for i in range(len(bingo_board)):
    if r == bingo_board[i] :
        bingo_board[i] = "*"
        print(bingo_board)
    


 

#보드 가로 세로 대각선 최소 2개이상 빙고
