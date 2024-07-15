def menu():
    print("=" * 20)
    print("1.학생 성적 입력")
    print("2.학생 목록 출력(입력 순)")
    print("3.프로그램 종료")
    print("=" * 20)
stu_score_dictioary = {}
def stu_put_score():
    stu_num = int(input("학번을 입력하세요\n"))

    if stu_num in stu_score_dictioary:
        print("이미 등록된 학번입니다")
        return
    
    stu_name = input("이름을 선택하세요: ")
    stu_kor = int(input("국어 성적을 입력하세요: "))
    stu_math = int(input('수학 성적을 입력하세요: '))
    stu_english = int(input('영어 성적을 입력하세요: '))
    sum = stu_kor + stu_math + stu_english
    avg = sum /3
    stu_score_dictioary[stu_num] = {"학번":stu_num,"이름":stu_name,"국어":stu_kor,\
                                    "영어":stu_english,"총합": sum, "평균":avg}

def show_stu_score():
    show_num = int(input("학생 목록 출력입니다 학번알려줘셈\n"))
    choice_su = input("원하는 학번알려주세요(전체를 알고싶다면 '전체'를 써주세요)\n")\
    
    if choice_su == "전체":
        for key,value in stu_score_dictioary.items():
            print(f"{key} {value}")

        
    
