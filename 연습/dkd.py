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





import random
def rock(user):
    
    choices = ['가위','바위','보']
    computer_choice = random.choice(choices)
    print(computer_choice)
    if user=='가위':
        if computer_choice =='보':
            msg = "당신이 이겼습니다!"
        elif computer_choice =='바위':
            msg = "당신이 졌습니다!"
        else:
            msg = "무승부입니다!"
    
    if user == '바위':
        if computer_choice =='가위':
            msg = "당신이 이겼습니다!"
        elif computer_choice == '보':
            msg = "당신이 졌습니다!"
        else:
            msg = "무승부입니다!"
    
    if user == '보':
        if computer_choice =='바위':
            msg = "당신이 이겼습니다!"
        elif computer_choice =='가위':
            msg ='당신이 졌습니다!'
        else:
            msg ='무승부입니다'
    return msg

user = input("가위, 바위, 보 중 하나를 선택하세요:")
result = rock(user)
print(result)