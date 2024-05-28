# a=int(input("첫번쨰 길이를 입력하세요"))
# b=int(input("두번쨰 길이를 입력하세요"))
# c=int(input("세번쨰 길이를 입력하세요"))

# if (a+b>=c) and (a+c>=b) and (b+c>=a):
#     if a==b==c:
#         print("입력하신 변의 길이로는 정삼각형을 만들 수있습니다.")
#     elif a==b or b==c or a==c:
#         print("입력하신 변의 길이로는 이등변삼각형을 만들 수있습니다")
#     elif a!=b!=c:
#         print("입력하신 변의 길이로는 부등변삼각형을 만들 수있습니다")
# else:
#         print("입력 하신 변의 길이로는 삼각형을 만들수없습니다.")
#         print("삼각형을 만들기 위해서는 어떤 두 변의 길이의 합이 다른 한변의 길이보다 커야합니다")


# foo = [10,20,30]

# bar = [100,200,300]

# bar = foo

# bar[0] = 7000
# print(foo[0],bar[0])
 







# # 만약세변의길이가모두같다면, '정삼각형'입니다.def foo():
#     mag="hello"
#     print(gretting)
    
# gretting = "안녕하세요"
 
# foo()

#  ② 만약세변중두변의길이가같다면, '이등변삼각형'입니다.
#  ③ 만약세변의길이가모두다르다면, '부등변삼각형'입니다.
#  ④ 만약어느두변의길이합이나머지한변의길이보다작거나같다면, 삼각형을형성할수
# 없습니다



# a=int(input("첫 번쨰 수 입력:"))
# b=int(input("두 번쨰 수 입력:"))
# c=int(input("세 번쨰 수 입력:"))

# if a == b == c:
#     print("모는 수가 같습니다.")
# else:
#     aya=[ a , b , c ]
#     ta=max(aya)
#     if a != b != c and ta:
#         print("모든 수가 다릅니다.가장 큰 수는" ,ta,"입니다.")
#     if a==b:
#         print(f"두수가 같습니다{a}와{b}")
#     elif a==c:
#         print(f"두수가 같습니다{a}와{c}")
#     elif b==c:
#         print(f"두수가 같습니다{b}와{c}")




# def num(a,b,c):
#     if a==b==c:
#         return("모는 수가같습니다")
#     else:
#         i=max(a,b,c)
#         if a !=max(a,b,c):
#             return(f"모든 수가 다릅니다. 가장 큰수는 {a}입니다")
#         elif a==b: 
#             return(f"두수가 같습니다{a}와{b}")
#         elif b==c:
#             return(f"두수가 같습니다{b}와{c}")
#         elif c==a:
#             return(f"두수가 같습니다{c}와{a}")
        
# a=int(input("첫 번쨰 수 입력:"))
# b=int(input("두 번쨰 수 입력:"))
# c=int(input("세 번쨰 수 입력:"))   

# print(num(a,b,c))


# # N=int(input())
# # for i in range(1,N+1):
# #     print("*"*i)

# # for i in range(N-1,0,-1):
# #   print("*"*i)




# #incremenrcount 함수 정의:
# # - 전역 변수 count의 값을 1 증가
# def incrementcount():
#     global count;
#     count = count + 1
    
# #deccreementcount 함수 정의:
# # - 전역 변수 count의 값을 1 감소
# def decrementcount():
#     global count;
#     count = count - 1

# #전역 변수 count를 1로 초기화
# count = 1

# incrementcount()
# print(count)

# decrementcount()
# print(count)

# incrementcount()
# print(count)
# incrementcount()
# print(count)





# def bar():
#     msg1 = " << " + name 
    
#     msg2 = foo(msg1)
#     msg2 += " " # msg2 = msg2 +  "  "
    
#     msg3 =  pos(msg2)
#     msg3 += " "
    
#     return msg3

# def foo(argf):
#     msg = argf + "님"
#     return msg


# def pos(argf):
#     msg = argf + "님"
#     return msg

# name = "홍길동"

# result = bar()

# print(result)


# a,b=map(int,input().split())
# print(a,b)
# if a > b:
#     print("Yes")
# else:
#     print("No")





# import random
# def rock(user):
    
#     choices = ['가위','바위','보']
#     computer_choice = random.choice(choices)
#     print(computer_choice)
#     if user=='가위':
#         if computer_choice =='보':
#             msg = "당신이 이겼습니다!"
#         elif computer_choice =='바위':
#             msg = "당신이 졌습니다!"
#         else:
#             msg = "무승부입니다!"
    
#     if user == '바위':
#         if computer_choice =='가위':
#             msg = "당신이 이겼습니다!"
#         elif computer_choice == '보':
#             msg = "당신이 졌습니다!"
#         else:
#             msg = "무승부입니다!"
    
#     if user == '보':
#         if computer_choice =='바위':
#             msg = "당신이 이겼습니다!"
#         elif computer_choice =='가위':
#             msg ='당신이 졌습니다!'
#         else:
#             msg ='무승부입니다'
#     return msg

# user = input("가위, 바위, 보 중 하나를 선택하세요:")
# result = rock(user)
# print(result)








# shopping_list =[]
# shopping_list.append("milk")
# shopping_list.append("bread")
# shopping_list.append("eggs")
# shopping_list.append("apple")
# print("현재 쇼핑 리스트:",shopping_list)
# shopping_list.insert(0,"toilet paper")
# shopping_list.insert(1,"orange juice")
# shopping_list.extend(["chicken","rice"])
# print("최종 쇼핑 리스트:",shopping_list)

# import random
# n = input("N값을 입력하세요 (1 - 100): ")
# random_number =random.randint(1,100)
# list_num =[]

# for i in range(0,n+1):
#     for o in random_number:
#         list_num.append(o)
        
        
# bar = [10,20,30,40]
# foo = bar[0:0:1]
# print(foo)
# foo = bar[0:1:1]
# print(foo)
# foo = bar[0:2:1]
# print(foo)
# foo = bar[0:3:1]
# print(foo)
# foo = bar[0:4:1]
# print(foo)
# foo = bar[1:4:1]
# print(foo)




# bar = [10,20,30,40]
# foo =  bar[:] #0,-1
# print(foo)

# foo = bar[2:]#30,끝까지
# print(foo)

# foo = bar[:3]#0,40전까지
# print(foo)



#770225-3983813
#3개로 구분해서 문자열로 저장
# #첫번쨰 : 생년월일 6자리
#두번쨰: 지역 코드값 6자리
#세번쨰: 패리티 체크값 1자리
# bar = [7,7,0,2,2,5,'-',3,9,8,3,8,1,3]

# print(bar[0:6])

# print(bar[7:13])

# print(bar[-1])


# n= int(input(f"원하는 원소의 인덱스 범의를 벗어났습니다{(0-n)}"))
# if 0 <= made_num_index or n >=made_num_index 
#     print(f"선택한 인덱스 원소{generated_random_num.append(random_num)}")
# else:
#     print("에러: 유효한 인덱스를 입력하세요")









# while True:
#     print("-"*20)
#     print("1. 구구단 출력")
#     print("2. 프로그램 종료")
#     print("-"*20)
#     input_1=int(input(""))
   
#     if input_1 == 1 :
#         print("출력할 구구단의 단을 입력하세요. 구구단의 2~9 사이 입력")
#         while True:
          
#             input_2 = int(input(""))
#             if 2 <= input_2 <=9:
#                 for i in range(1,10):
#                     print(f"{input_2} * {i} = {input_2 * i}")
#                 break
#             elif input_2 == 1 :
#                 print("2~9사이 정수를 입력하세요")
#                 break
#             elif input_2 != 1 or input_2 !=2 :
#                     print("잘못 입력하셨습니다. 다시 입력하세요.")
#                     break   
#     else:
#         print("이용해주셔서 감사합니다.")
#         break


# n = 5
# c = 0
# for i in range(1,n+1):
#     print(f"{}")


# input_value =int(input("성적입력:"))
# #90점이상이면 A
# if input_value >= 90:
#     msg ="에"
# #80점 이상 이면 비
# elif 80 >input_value >90:
#     msg ="비"
# #70점이상이면 씨
# elif 70<= input_value >80:
#     msg = "씨"
# #60점이상이면 디
# elif 60<= input_value >70:
#     msg ="디"
# #60점미만이면 에프
# else:
#     msg ="에프"
# print(msg)



# #!~20까지 정수를 출력 
# for i in range(1,21):
#     print(i,"\t",end="")
#while 
count = 0    
while  count < 21:
    print(count)
    count += 1
   
   
   
count = 0    
while  count < 21:
   
    count += 1
    print(count)
