
def choice1():
    number = int(input("학번을 입력하세요: "))
    name = input("이름을 입력하세요 :")
    language = int(input("국어: "))
    english = int(input("영어: "))
    math = int(input("수학: "))
    total= language + english + math
    avg1 = total / 3
    return [number, name, language, english, math, total, avg1]
s_list = []
data = 0
a_avg = []
#메뉴 
while True:
    print("=" * 20)
    print("1.학생 성적 입력")
    print("2.학생 목록 출력(입력 순)")
    print("3.프로그램 종료")
    print("=" * 20)
    print(f"현 입력데이터 갯수 : {data} ")
    print(f"전체 학생 평균 값 :{sum(a_avg)/data if data >= 1 else 0.0}")
    choice = int(input("선택하세요!"))
    if choice == 1:
        student = choice1()
        s_list.append(student)
        a_avg.append(student[6])
        data +=1 

    elif choice == 2:
        for i in s_list:
            print(f" id:{i[0]} name:{i[1]} kor:{i[2]} eng:{i[3]} math:{i[4]} sum:{i[5]} avg:{i[6]}")
    else:
    
        break




