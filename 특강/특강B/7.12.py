def menu():
    print("=" * 20)
    print("1.학생 성적 입력")
    print("2.학생 목록 출력(입력 순)")
    print("3.프로그램 종료")
    print("=" * 20)
# 학생들성적     
stu_d = {}
all_count = 0
all_avg = 0
while True:
    menu()
    print(f" 현재 입력데이터 갯수: {all_count}")
    print(f" 전체 학생 평균 값 :{all_avg}")
    user = int(input("메뉴를 선택하라옹~"))
    if user == 1:
        number = int(input("학번을 입력하셈"))
        name = input("君の名前は？")
        kor = int(input("국어 점수 넣으셈"))
        engilsh = int(input("영어 점수 넣으셈"))
        math = int(input("수학 점수 넣으셈"))
        sum = kor +  engilsh  + math 
        avg = sum / 3
        stu_d[number] ={"이름":name,"국어":kor,"영어":engilsh,"수학":math,"총합":sum,"평균":avg}
        all_count +=1 
        all_avg += avg /all_count

    elif user == 2:
        print(stu_d)
       

    else:
        break

