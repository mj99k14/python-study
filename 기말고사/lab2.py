import random


def print_bingo_board(arg_list, col_num = 3):#arg_list는 빙고보드요소 리스트 ,열의수는 3
    for index in range(len(arg_list)):
        print(arg_list[index], "\t", end="")
        
        if (index + 1)  % col_num == 0: # ->3,6,9일떄 줄바꿈이 있어야하니깐
            print()

#bingo_board =[1,2,3,/
            #  4,5,6,/
            #  7,8,9]
# N 값 입력
while True:
    N = int(input("N 값: 3 ~ 6"))
    
    if 3 <= N <= 6:
        break
    
bingo_element_num = N * N
# N X N 빙고 보드 작성: 1차원 배열, 1~36사이의 중복되지 않은 정수


bingo_board = []

while len(bingo_board) < bingo_element_num:
    
    rand_num = random.randint(1, 36)
    
    if rand_num not in bingo_board: #중복되지않는 랜덤수 발생시키면 bingo_board안에들어감
        bingo_board.append(rand_num)
        
        

bingo_count = 0

# # 빙고 숫자가 2미만일 경우
while bingo_count < 2:
    bingo_count = 0
    
    
    input("랜덤 넘버 생성: Press enter key!!")
    
    # 랜덤 넘버 생성 : 1 ~ 36
    rand_num = random.randint(1, 36)
    
    #빙고 보드 내 생성된 랜덤 값이 있을 경우 "*"로 변경
    for index in range(bingo_element_num):
        if bingo_board[index] == rand_num:
            bingo_board[index] = "*"
            break

    # 빙고 보드 출력
    print_bingo_board(bingo_board)

    # 빙고 검사
    # 가로 확인 알고리즘
    for row in range(N): #세로
        for col in range(N):#가로
            if bingo_board[col + (row * N)] != "*": #col 0,1,2 +(0*3)bingo_board[0]
                break                               #(1,2,3)(4,5,6)(7,8,9)
        else:
            bingo_count += 1 #빙고 찾기위해
    
    # 세로 확인 알고리즘                           # 1 2 3 
                                                 # 4 5 6 
    for col in range(N):                         # 7 8 9    
        for row in range(N):
            if bingo_board[col + (row * N)] != "*":  #(1,5,7) (2,5,8) (3,6,9)원소를 찾기위해
                break
        else:
            bingo_count += 1

    # 대각선 : 왼쪽 -> 오른쪽 \     
    for count in range(N):
        if bingo_board[ count * (N + 1) ] != "*": #(1,5,9)
            break
    else:
        bingo_count += 1

    # 대각선 : 오른쪽 -> 왼쪽 /
    for count in range(N):
        if bingo_board[(count + 1) * (N - 1)] != "*": #(3,5,7)
            break
    else:
        bingo_count += 1