import random
def print_menu():   #메뉴 출력
    width = 15
    print("-" * width)
    print("1. 구구단 출력")
    print("2. 삼각형 출력")
    print("3. 종료")
    print("-" * width)
    
def is_valid_num(arg_start, arg_end, *args): #시작값 , 끝날값 #리스트값
    
    for value in args: # 리스트안에있는 값들이 사이에있는지 확인 
        if not (arg_start <= value <= arg_end): #시작~ 끝 사이에 있는지확인
            return False #없으면 틀림
            
    return True #맞음

def print_mul_table():
    
    while True:
        input_value = input("출력할 단을 입력하세요: ")
        
        input_list = input_value.split("~")
        input_list = [int(value) for value in input_list]
            
        if is_valid_num(2, 9, *input_list):   #2,9는 2~9의 범위 *input_list은 내가입력하게리스트로 나와서 위에is_valid_num()을 통해 검사함
            break
            
        print("2~9 정수를 입력 하세요")
              
    
    # 구구단을 출력
    start = input_list[0]      #입력 받은 리스트에 1번쨰
    end = input_list[1] if len(input_list) > 1 else input_list[0] # 입력받은갯수가 1개라면 1번째까지 입력받은 갯수가 2개라면 2번째거 선택
    
    for dan in range(start, end + 1):  
        for num in range(1, 10):
            print(f"{dan} X {num} = {dan * num}")
        print()
        
def print_triangle():
    
    while True:
        row_num = int(input("삼각형의 높이를 입력하세요: "))
        
        if is_valid_num(2, 3, row_num):  #범위 확인 
            break
        
        print("2~3 값을 입력 하세요")
    
    # rand_list = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    rand_list = [value for value in range(10)]
    
    for rnum in range(row_num):
        # 공백 출력
        print(" " * (row_num - rnum - 1), end="")   #row_num =3 rnum은 0부터시작 -1
        #공백 두개 #한개 #영개
         
        # 난수 값 출력
        for _ in range(rnum + 1):
            rand_num = rand_list[random.randint(0, len(rand_list) - 1)] #9를 맞춰주기위해서
            rand_list.remove(rand_num)
            
            print(rand_num, end="") #지워질 값이 print
            
        # 개행 문자
        print()
    
    
while True:

    # 메뉴 출력
    print_menu()

    input_value = int(input("메뉴를 선택 해주세요: "))

    if not (1 <= input_value <= 3):
        print("1~3 정수를 입력하세요")
        continue
    
    # 1. 구구단 실행
    if input_value == 1:
        print_mul_table()
    # 2. 삼각형 출력
    elif input_value == 2:
        print_triangle()
    # 3. 종료
    elif input_value == 3:
        print("종료")
        break