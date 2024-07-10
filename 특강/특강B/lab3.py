def menu():
    print("[메뉴 선택]")
    print("1. 학생 성적 입력")
    print("2. 학생 성적 화면 출력")
    print("3. 학생 성적 파일 출력")
    print("4. 종료")

def choice1():
    name = input("학생 이름 : ")
    language = int(input("국어: "))
    english = int(input("영어: "))
    math = int(input("수학: "))
    soccer = language + english + math
    avg = soccer / 3 
 


    return [name,language,english,math,soccer,avg,]

s1= ["이름", "국어", "영어", "수학", "총점", "평균", "등수"]
m = []
avg_list = []


while True:
    menu()
    input_user = int(input("메뉴를 선택하라옹~! "))
    if input_user == 1:
        s = choice1()
        m.append(s)
  

    elif input_user == 2:
        print("[학생 성적 목록]")
        for i in s1:
            print(i,"\t",end="")
        print()
        for a in m:
            for z in a:
                print(z,"\t",end="")
            print()
    elif input_user == 3: 
        with open('grade.txt','a+') as f_handler:
            for i in s1:
                f_handler.write(i +"\t")
            f_handler.write("\n")
            for a in m:
                for z in a:
                    f_handler.write(str(z) +"\t")
                f_handler.write("\n")

             

    else:
        break
    




    
