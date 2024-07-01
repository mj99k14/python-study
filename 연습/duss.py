import random

def menu():
    width = 15
    print("-" * width)
    print("1. 구구단 출력")
    print("2. 삼각형 출력")
    print("3. 종료")
    print("-" * width)


def is_valid_num(arg_start,arg_end,*args):
    for value in args:
        if not (arg_start <= value <= arg_end):
            return False
    
    return True

def print_mul_table():
    while True:
        input_value = input("출력할 단을 입력하세요: ")

        input_list = input_value.split("~")
        input_list = [int(value) for value in input_list]

        if is_valid_num(2,9,*input_value):
            break

        print("2~9 정수를 입력하세요")

    start = input_list[0]
    end =input_value[1] if len(input_list) > 1 else input_value[0]

    for dan in range(start,end + 1 ):
        for num in range(1,10):
            print(f"{dan} x {num} = {dan * num}")

        print()


def print_triangle():
    while True:
        rom_num =  int(input("삼각형의 높이를 입력하세요: "))
        if is_valid_num(2,3,rom_num):
            break
        print("2~3 값을 입력하세요")


    ran_list =  [value for value in range(10)]
    for num in range(rom_num):

        print(" "*(rom_num - num -1 ),end="")

        for _ in range(num + 1):
            rand_num = ran_list[random.randint(0,len(ran_list)-1)]

            ran_list.remove(rand_num)

            print(rand_num, end = "")

        print()



while True:

    menu()

    input_value = int(input("메뉴를 선택 해주세요 : "))

    if not (1 <= input_value <=3):
        print("1 ~ 3 정수를 입력하세요")
        continue


    if input_value == 1:
        print_mul_table()
    elif input_value == 2:
        print_triangle()
    elif input_value ==3:
        print("종료")
        break 