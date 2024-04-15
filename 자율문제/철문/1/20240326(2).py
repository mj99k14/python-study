# # 사용자로부터세변의길이를입력으로받습니다.
a=int(input("첫번쨰 변의 길이를 입력하세요:"))
b=int(input("두번쨰 변의 길이를 입력하세요:"))
c=int(input("세번째 변의 길이를 입력하세요:"))

# if a==b and b==c and a==c:
#     print("입력하신 변의 길이로는 정삼각형을 만들 수 있습니다")   
# elif a==b!=c and a==c!=b and c==b!=a:
#     print("입력하신 변의 길이로는 이등변삼각형을 만들 수 있습니다")
# elif a!=b and a!=c and b!=c:
#     print("입력하신 변의 길이로는 부등변삼각형을 만들 수 있습니다.")
# elif a+b>=c or b+c>=a or c+a>=b:
#     print("입력하신 변의 길이로는 삼각형을 만들 수 없습니다.")
#     print("삼각형을 만들기위해서는 어떤 두 변의 길이보다 커야 합니다.")
    


if (a+b>c) and (c+b>a) and (c+a>b):
    if a==b==c:
        print("입력하신 변의 길이로는 정삼각형을 만들 수 있습니다")
    elif a==b  or b==c or c==a:
        print("입력하신 변의 길이로는 이등변삼각형을 만들 수 있습니다")
    elif a!=b!=c:
        print("입력하신 변의 길이로는 부등변삼각형을 만들 수 있습니다.")
else:
    print("입력하신 변의 길이로는 삼각형을 만들 수 없습니다")
    print("삼각형을 만들기위해서는 어떤 두 변의 길이보다 커야 합니다.")
    

    
    








