#메뉴
#1.구구단 선택
#2.삼각형 
#3.종료


def menu():
    print(""-" * 20")
    print("1.구구단")
    print("2.랜덤값 삼각형 출력")
    print("3.종료")
    print(""-" * 20")

user_input = int(input("원하는 메뉴 번호를 입력하세요 : "))

 
def gugudan(arg_start,arg_end):

    if len(user_input)  == 1:
        arg_end = arg_start
        for i in range(arg_start,arg_end + 1):
            for u in range(1,10):
                print(f"{i} * {u} = {i * u}")
                

    else:
        for i in range(arg_start,arg_end + 1):
            for u in range(1,10):
                print(f"{i} * {u} = {i * u}")
                








if user_input == 1:
    gugudan()