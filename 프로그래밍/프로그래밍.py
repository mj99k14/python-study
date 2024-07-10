# value = int(input("정수 입력"))
# #입력 값이 3이하 이면
# if value <3.0:
#     print("참")
# else:
#     print("거짓")
    
# c=int(input())    
# if 1< c <=3: #1초과 3 이하
#     print("")    
    
# print(2 > 3 < 4)
# #왼쪽 -> 오른쪽
# #2 > 3 ->false -> 종료
# print(2 < 3 < 4 < 5 < 6 < 7)
# #2 < 3 이true고 다음값도 계속 true값이기때문에
# #계속 true false값을 만나면 종료


# if value % 2 == 0 and value % 3 == 0:
#     print("참")
# else:
#     print("거짓") 
    

# value = 4     #not은 단항
# if not value:  #not이 무조건 우측, not은 무조건 t/f
#     print("참")#FALSE을 true
# else:
#     print("거짓")




def bar(argvalue):
    print("bar is invoked")
    return argvalue

if False and bar(2) == 2:#false 이기 떄문에 뒤에는 게산을 안함 
                        #true 이기 때문에 뒤에껄 실행
    print("참")
else:
    print("거짓 ")