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
 

    A = [name,language,english,math,soccer,avg]
    return A

s1= ["이름", "국어", "영어", "수학", "총점", "평균", "등수"]
m = []
avg_list = []


count = 0
while True:
    menu()
    input_user = int(input("메뉴를 선택하라옹~! "))
    if input_user == 1:
        s = choice1()
        m.append(s)
        avg_list.append(s[5]) #평균값 리스트
        count += 1
    elif input_user == 2:
        grade = [1 for _ in range (len(avg_list))]
        print("[학생 성적 목록]")
        for i in range(len(avg_list)):
            for s in  range(len(avg_list)):
                if avg_list[i] < avg_list[s] :
                    grade[i] += 1   
        m.append(grade)    
    
        for i in s1:
            print(i,"\t",end="")
        print()
        for a in m:
            for z in a:
                print(z,"\t",end="")
            print()
       
    # elif input_user == 3: 
    #     with open('grade.txt','a+',encoding="utf-8") as f_handler:
    #         for i in s1:
    #             f_handler.write(i +"\t")
    #         f_handler.write("\n")
    #         for a in m:
    #             for z in a:
    #                 f_handler.write(str(z) +"\t")
    #             f_handler.write("\n")

             

    else:
        break
    




    
