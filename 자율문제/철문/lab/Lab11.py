# 사용자로부터섭씨온도를입력받아화씨온도로변환하는함수를작성하고, 변환된화씨온도를출력하는프로그램을작성하세요.
celsius=int(input("섭씨 온도를 입력하세요:"))
# 화씨온도는섭씨온도에9/5를곱한후32를더해계산합니다
def convert_celsius_to_fahrenheit(celsius):
    fahrenheit=float((celsius*9/5)+32)
    return fahrenheit
fahrenheit=convert_celsius_to_fahrenheit(celsius)
# F = (C * 9/5) + 32 
# 사용자에게섭씨온도를입력받습니다.
print("화씨온도는",fahrenheit,"입니다.")
# – 블릿2: 섭씨를화씨로변환하는함수를작성합니다.
# – 블릿3: 변환된화씨온도를출력합니다.