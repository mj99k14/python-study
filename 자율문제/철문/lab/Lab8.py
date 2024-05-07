# #  -사용자에게하나의문자를입력받습니다.
# letter=input("하나의 문자를 입력하세요:")
# #  – 입력받은문자가모음인지아닌지확인합니다.
# vowel=['a','e','i','o','u']
# if letter in vowel:
#     print(letter+"는 모음입니다.")
# else:
#     print(letter+"는 모음이 아닙니다.")
# #  – 결과를출력합니다




#  사용자로부터하나의영문자를입력받고, 해당문자가모음(a, e, i, o, u) 중
# 하나인지아닌지를판별하여결과를출력하는프로그램을작성하세요
letter=input("하나의 문자를 입력하세요:")
vowel=("a","e","i","o","u")
# – 사용자에게하나의문자를입력받습니다.
# – 입력받은문자가모음인지아닌지확인합니다.
if letter=="a":
    print(letter,"는 모음입니다.")
elif letter=="e":
    print(letter,"는 모음입니다.")
elif letter=="i":
    print(letter,"는 모음입니다.")
elif letter=="o":
    print(letter,"는 모음입니다.")
elif letter=="u":
    print(letter,"는 모음입니다.")
else:
    print(letter,"는 모음이 아닙니다.")
# – 결과를출력합니다