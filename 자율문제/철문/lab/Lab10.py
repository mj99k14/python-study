# #  사용자로부터세개의정수숫자를입력받습니다.
# number1 =int(input("첫번쨰 숫자를 입력하세요:"))
# number2 =int(input("두번째 숫자를 입력하세요:"))
# number3 =int(input("세번쨰 숫자를 입력하세요:"))
# # – 입력받은숫자들중가장큰숫자를판별합니다.
# largest_number=max(number1,number2,number3)
# # – 가장큰숫자를출력합니다.
# print("가장큰숫자는",largest_number,"입니다")



# 사용자로부터세개의정수숫자를입력받습니다.
number1 =int(input("첫번쨰 숫자를 입력하세요:"))
number2 =int(input("두번쨰 숫자를 입력하세요:"))
number3 =int(input("세번쨰 숫자를 입력하세요:"))
# – 입력받은숫자들중가장큰숫자를판별합니다.
if number1>number2 and number1>number3:
    print("가장큰숫자는",number1,"입니다.")
elif number2>number1 and number2>number3:
    print("가장큰숫자는",number2,"입니다")
elif number3>number1 and number3>number2:
    print("가장큰숫자는",number3,"입니다")
# – 가장큰숫자를출력합니다