#1.사용자 입력 오류
#숫자를 입력받아야 하지만 , 문자를 입력할 경우 발생하는 오류
num = int(input("1또는 2숫자를 입력하세요: "))
try: 
    print("pos")
    
    #print(1/0)

    print("bar")

    kin()



except ValueError:
    print("valiseError 예외 발생")
except IndexError as e:
    print(f"예외 발생:{e}")
except NameError as e:
     print(f"예외 발생:{e}")
except ZeroDivisionError:
    print("zerodivisionerror 예외발생")

print(f"결과:0")