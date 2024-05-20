# import random

# #리스트 생성: bar(참조변수)
# bar = list()

# for _ in range(0,5):#0,1,2,3,4,
#     #random.randint(1,100)) -> 1~100이하의 정수 중 난수를 한개 선택 
#     bar.append(random.randint(1,100))
# print(bar)




# #예 [90,50,30,100,20]
# print(bar[-1])   #마지막 값찾을때
# print(bar[4])
# print(bar[len(bar)-1]) #len 길이 찾아서 마지막 


# bar = [10,20,30,40,50]

# print(bar[0])
# print(bar[1])
# print(bar[2])
# print(bar[3])
# print(bar[4])
# print(bar[0])
# print(bar[-1])
# print(bar[-2])
# print(bar[-3])
# print(bar[-4])
# print(bar[-5])



# import random
# def generate_password(length):
#     uppercase_letters = 'ABCDEFGHIJKLMNOPGRSTUVWXYZ'
#     lowercase_letters = uppercase_letters.lower()
#     digits = '0123456789'
#     all_characters = uppercase_letters + lowercase_letters +digits
    
#     password = ""
    
#     for _ in range(length):
#         password += random.choice(all_characters)
#     #초기한값 
#     check_1 = False
#     check_2 = False
#     check_3 = False
#     for i in uppercase_letters:
#         if i in password:
#             check_1 = True
#             break
    
#     for i in lowercase_letters:
#         if i in password:
#             check_2 = True
#             break
    
#     for i in digits:
#         if i in password:
#             check_3 = True
#             break
        
        
#     if check_1 and check_2 and check_3:
#         return password
#     else:
#         return  generate_password(length)
        
# password_lenght = int(input("생성할 패스워드의 길이를 입력해주세요: "))

# if password_lenght  >= 3:
#     generate_password = generate_password(password_lenght)
#     print(generate_password)
# else:
#     print("3자리 미만의 패스워드는 생성할 수 없습니다. ")


value = 4
if not value:
    print("참")
else:
    print("거짓")
    
value = 2
if not value:
    print("안녕")
else:
    print("거꾸로")
    
# 그럼 if 문에서 
if not value < 5: #반대로 5이상
   print("이게 정답일껄")
else:
    print("이거틀리면 이해못한거임")
    



