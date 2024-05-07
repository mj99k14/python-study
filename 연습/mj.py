# # 사용자로부터"남자" 또는"여자"라는문자열입력받기
# Name=input("성별을 한글로 입력하세요")
# # § 입력된문자열이"남자"인경우"MAN"으로변환하여출력
# if Name=="남자":
#     print("MAN")
# # § 입력된문자열이"여자"인경우"WOMAN"으로변환하여출력
# elif Name=="여자":
#     print("WOMAN")
# # § 이외의입력에대해서는오류메시지출력
# else:
#     print("잘못된 입력입니다.")


# dis=float(input())
# light=299792
# print(dis/light)


# #  사용자로부터나이를입력받습니다. 
# age=int(input("나이를 입력하세요:"))
# # – 입력된나이에따라사용자를"청소년(Teenager)", "성인(Adult)", "노년(Senior)" 중 하나로 분류
# # 합니다.
# # – 13세에서19세사이는"Teenager"
# # if 13<=age<=19:
# #     print("teenager")
    
# # – 20세에서64세사이는"Adult"
# elif 20<= age <=64:
#      print("adult")
# # – 65세이상은"Senior"
# elif age>=65:
#     print("senior")
# # – 해당하는나이대의영어단어를화면에출력합니다.
# else:
#     print("unknown age group")
# # – 범위에맞지않는입력값에대해서는"Unknown age group"이라고출력합니다

# 사용자에게두정수숫자를입력받습니다.
# number1=int(input("첫번쨰 숫자를 입력하세요:"))
# number2=int(input("두번쨰 숫자를 입력하세요:"))
# # – 입력받은숫자들의합, 차, 곱, 나눗셈결과를계산합니다.
# print("합:",number1+number2)
# print("차:",number1-number2)
# print("곱:",number1*number2)
# print("나눗셈:",number1/number2)
# # – 계산된결과를출력합니다
# 사용자로부터하나의영문자를입력받고,
# letter=input("하나의 문자를 입력하세요")
# # 해당문자가모음(a, e, i, o, u) 중
# num=['a','e','i','o','u']
# # 하나인지아닌지를판별하여결과를출력하는프로그램을작성하세요 
# if letter in num:
#     print(letter,"는 모음입니다.")
# else:
#     print(letter,"는 모음이 아닙니다.")
# loction=input("left,right,up,down")
# if loction=="left":
#     print("왼쪽으로 이동합니다.")
# elif loction=="right":
#     print("오른쪽으로 이동합니다.")
# elif loction=="up":
#     print("위로 이동합니다.")
# elif loction=="down":
#     print("아래로 이동합니다.")
# else:
#     print("알수없는 명령입니다")
    
    
    

# while True:
#     A,B=map(int,input().split())
#     if A==0 and B==0:
#         break
#     else:
#         print(A+B) 








# math=float(input("수학 점수를 입력하세요:"))
# science=float(input("과학 점수를 입력하세요:"))
# english=float(input("영어 점수를 입력하세요:"))
# #입력받은 점수들을 바탕으로 평균을 계산합니다
# average=int(math+science+english)/3

# print(average)










#  사용자의나이(age)
#  • 사용자가예약하려는이벤트코드(event_code) - 이벤트코드는'E1', 'E2', 'E3' 중 하나입니다.
#  • 사용자가예약을원하는날짜(reservation_date) - 예약 날짜는 1부터 30까지의 숫자로 입력됩니다.
#  2. 각이벤트코드별로다음과같은규칙이적용됩니다:
#  • 'E1': 만 18세 이상만 예약가능합니다.
#  • 'E2': 모든 연령대가예약가능하지만, 날짜는짝수일에만예약할수있습니다.
#  • 'E3': 만 16세 이상만 예약할수있으며, 7의배수인날짜에만예약가능합니다.
#  3. 사용자는각이벤트코드에따라예약을시도할때다음과같은결과를받게됩니다:
#  • 예약성공: "예약이완료되었습니다!"
#  • 나이미달: "나이제한으로인해예약할수없습니다."
#  • 날짜제한: "선택하신날짜에는예약할수없습니다."
#  • 잘못된입력: "잘못된입력입니다. 프로그램을종료합니

# age=int(input("나이를 입력하세요:"))
# event_code=input("예약하려는 이벤트 코드를 입력하세요:")
# reservation_date=int(input("원하는 예약 날짜를 입력하세요:"))

# def happy(age,event_code,reservation_date):
#     date=range(1,31)
#     if not event_code in ["E1","E2","E3"] and not reservation_date in date:
#       return ("잘못된 입력입니다.프로그램을 종료합니다.")
#     else:
#         if event_code=="E1": 
#             if age >= 18:
#                 return("예약이 완료되었습니다!")
#             else:
#                 return("나이 제한으로 인해 예약할 수 없습니다.")
#         if event_code=="E2":
#             if reservation_date%2==0:
#                 return("예약이 완료되었습니다.")
#             else:
#                 return("선택하신 날짜에는 예약할 수 없습니다.")
#         if event_code=="E3":
#             if reservation_date%7==0 and age >= 16:
#                 return("예약이 완료되었습니다!") 
#             elif reservation_date%7!=0:
#                 return("선택하신 날짜에는 예약할 수없습니다.")
#             elif  age < 16:
#                return("나이 제한으로 인해 예약할 수 없습니다.") 
           
# print(happy(age,event_code,reservation_date))             
        


# password=input("비밀번호를 입력하세요:")
# if len(password)<8:                     #여기서 일단 8자리가 안넘으면 실행이안되니깐
#     print("비밀번호가 안전하지않습니다 ")
# else:
#     has_number = False     
#     has_uppercase = False            #여기에다가 초기화시켜준다
    
# for i in password:
#     if i.isdigit():
#         print(i)
#         has_number = True
#         break
# for i in password:
#     if i. isupper():
#         print(i)
#         has_uppercase = True
#         break

# if has_number ==has_uppercase:
#     print("비밀번호가 안전합니다.")
# else:        
#     print("비밀번호가 안전하지 않습니다.")




# password=input("비밀번호를 입력하세요:")
# if len(password) >= 8:
#     print()
# else:
#     print()


# has_number = False
# for i in  password:
#     if i.isdigit():
#         print(i)
#         has_number = True
#         break

# has_uppercase = False
# for i in password:
#     if i.isupper():
#         print(i)
#         has_uppercase = True
#         break

# if len(password) >= 8 and has_uppercase== has_number == True: 
#     print("비밀번호가 안전합니다.")
# else:
#     print("비밀번호가 안전하지 않습니다.")  




# while True:
#     try:
#         a,b= map(int,input().split())
#         print(a + b)
#     except:
#         break



# N=int(input())
# for i1 in range(1,10):
#         print(f"{N} * {i1} = {N*i1} ")



# basevalue =float(input("기본값을 입력하세요: "))
# a="1.더하기"
# print(a)
# b="2.뺴기"
# print(b)
# c="3.곱하기"
# print(c)
# d="4.나누기"
# print(d)

# def select0peration():
#     global basevalue
#     cho=int(input("선택: " ))
#     in1=int(input("숫자 입력: "))

#     if cho ==4 and in1 == 0:
#        print("에러: 0으로 나눌수 없습니다.")
#        return
#     else:
#         if cho == 1:
#             basevalue=in1 + basevalue
#             print("연산 결과:",basevalue)
#         elif cho == 2:
#             basevalue=basevalue - in1
#             print("연산 결과:",basevalue)
#         elif cho== 3:
#             basevalue=basevalue * in1 
#             print("연산 결과:",basevalue)
#         elif cho == 4:
#             basevalue= basevalue/ in1
#             print("연산 결과:",basevalue)
    


# select0peration()


# books = []
# while True:
#     title = input("도서 제목을 입력하세요(종료하려면 '종료' 입력): ")
#     if title=='종료':
#         break
#     books.append(title)
# print("도서 목록:",books)
    
# m=[1,2,3,4]
# i=int(input())
# if i <= len(m):
#     print(m[i])
# else:
#     print(5)
    
    
    
    
# t= int(input())
# for i in range(t):
#     a,b=map(int,input().split())
#     print(a+b)
    
    
#영수증에 적힌 총금액 x
#영수증에 적힌 구매한 물건의 종류의 수 n
#각 물건의 가격 
# a와 개수 b가 공백을 사이에 두고 주어진다

# x=int(input())
# n=int(input())
# c=0
# for i in range(n):
#     a,b=map(int,input().split())
#     c= c + (a * b)
# if c == x:
#     print("Yes")
# else:
#     print("No")


#1~6까지
#같은 눈 3 = 10000 + 같은눈 * 1000
#같은 눈 2 = 1000 + 같은눈 * 100
#모든 다른 눈 = 그중가장 큰 눈 * 100



# a,b,c=map(int,input().split())
# max_number=max(a,b,c)

# if a==b==c :
#     print(10000 + a * 1000)
# elif a==b :
#     print(1000 + a * 100)
# elif b==c :
#     print(1000 + b * 100)
# elif a==c :
#     print(1000 + a * 100)
# else:
#     print(max_number * 100)        


# X=int(input())
# N=int(input())
# c=0
# for i in range(N):
#     a,b=map(int,input().split())
#     print(c+(a * b))
# if  i == X:
#     print("Yes")
# else:
#     print("No")
    
# x=int(input())
# n=int(input())
# c=0
# for i in range(n):
#     a,b=map(int,input().split())
#     c= c + (a * b)
# if c == x:
#     print("Yes")
# else:
#     print("No")



# T= int(input())
# for i in range(1, T+1):
#     A,B=map(int,input().split())
#     print(f"case#{i}:",A + B)



# T=int(input())
# for i in range(1,T+1):
#     A,B=map(int,input().split())
    
    
#     print(f"Case #{i}:", A+B)




# book = []


# while True:
#     book_tittle=input("도서 제목을 입력하세요 (종료하려면 '종료' 입력):   " )
#     if book_tittle == '종료':
#         break
#     book.append(book_tittle)

# print("도서 목록:", book)    



# bar=[10,20,30,40]
# for index in range(0,len(bar)): #0,3: len(리스트) -리스트의 원소 개수
#     print(bar[index]) #index 0 ->2




# bar =[value for value in range(10,20)]
# print(bar)
# #[10,11,12,13,14,15,16,17,18,91]

# #slicing
# #참조 변수[start:stop:step]
# foo =bar[0: 4: 1]
# print("foo :",foo)
# print("bar :",bar)



# for i in range(1,101):
#     if i %3 ==0 or  i %7 ==0:
#         print(i, "\t",end="" )


# for i in range(1,101):
#     if i %3 ==0 and  i %7 ==0:
#         print(i, "\t",end="" )



# count = 0
# s=0
# for i in range(1,6):
#     use =int(input())
#     s+= i
    
# print(F"합계 {s}")
# a= s/5 
# print(f"평균 {a}")






# input_num = 5
# sum =0 
# avg = 0.0
# input_value= int(input())
# if input_value <0:
#     print("에러")
      
#     while True:
#         if input_value >0 :
#             for t in range(0,input_num):
#             msg = str(t) +"번쨰 입력:"
#             input_value = int(input(msg))
    
#             sum = sum +input_value
# avg = sum / input_value
# print(sum,avg)
    
    
 #정수 5개받아서  평균 합계 구하기  
# input_num = 5

# sum = 0
# avg = 0.0

# for trial_count in range(1, input_num + 1):
#     while True:
#         msg = str(trial_count) + "번째 입력 : "
#         input_value = int(input(msg))
#         if input_value >0 : # 0보다 작으면 다시돌아가기
#             break
#     sum += input_value
    
# avg = sum /input_num

# print(sum, avg)    






# for i in range(1,20,2):
#     print(i,end="")
    
    
    
# for i in range(1,20):
#     if i %2 != 0:
#         print(i)




# import random
# #1 에서 100 까지의 랜덤 정수를출력하세요
# random_number = random.randint(1,101)
# list_num =[]
# while True:
#     n = int(input("값을 입력하세요(1-100)"))
#     #n값이 1~100이아니면 에러 입니다
#     if 1 > n or  100> n:
#         print("에러다 이자식아")
#         break
#     #n값 안에 들어간다면 n값만큼 랜덤수를 뽑아낸다
#     for n in range(1,101):
#         print(list_num[n])
# #인덱스를 받는다  범위는 n값만큼 랜덤 리스트안에서 받는다
# #범위를 벗어나면 에러






result_1 = 1 + 2

result_2 = 2 + 1.5

result_3 = 3 * 2

result_4 =  6 / 2

print(result_1,result_2,result_3,result_4)

print(type(result_1),type(result_2),type(result_3),type(result_4))


#실수와 정수를 나누면 몫과 나머지를 나와야하기때문에 정수를 실수로 변환한다


result_1 = 2**3   # ** 거듭제곱 2의3
print(result_1)


for v in range(11): #10까지 돌면서 거듭제곱을 찾는다
    print(2**v)     #v = 0 일 때, 2**0 = 1
                    # v = 1 일 때, 2**1 = 2
                    # v = 2 일 때, 2**2 = 4
                    # v = 3 일 때, 2**3 = 8
                    # v = 4 일 때, 2**4 = 16
                    # v = 10 일 때, 2**10 = 1024