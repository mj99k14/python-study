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



# import random
# def




                    
# total = 0

# for i in range(1,6):
#     input_value = int(input(f"{i}번쨰 값 입력"))
#     total += input_value
# print(f"합계: {total}")
# #평균
# all_1 =total/ 5
# print(f"평균 : {all_1}")






 
# #정수를 입력받아서짝수이면 짝수 출력
# user =int(input("정수 입력"))
# #짝수가 아니면  아무것도 출력안한가~ #나누기는 3가지 [/몫$나머지, // 몫, %나머지]
# if user % 2 == 0:
#     print("짝수")

    
#정수를 입력받아서짝수이면 짝수 출력 
# 

# user = int(input("정수입력 :"))
# #정수를 입력받아서 0이면 0출력 0초과이면 "양의정수"

# msg = ""
# if user == 0:
#     msg = "0"
# elif user > 0 :
#     msg ="양의 정수"
# #0미만이면 음의 정수를 출력해라
# else:
#     msg ="음의 정수"
# print(msg)

# msg = "결과"
# if user == 0:
#     msg +="0"
# elif user > 0 :
#     msg +="양의 정수"
# #0미만이면 음의 정수를 출력해라
# else:
#     msg +="음의 정수"
# print(msg)


while True:
    numbers_str = input("숫자들을 쉼표로 구분하여 입력하세요:")
    numbers = numbers_str.split(',')
    result = 0
    
    for num_str in numbers:
        result += int(num_str.strip())
   
    if result < 100:
        print("종합이 100을 초과하지 않았습니다")
        print("입력된 모든 숫자들:", numbers)
        print("최종 총합:", result)
    else:    
        print("총합이 100을 초과하였습니다.")
        print("현재까지의 입력값들:", numbers)
        print("현재까지의 총합:", result)
        break
