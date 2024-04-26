input_value =(input("첫번째 값을 입력하세요 \n"))
if '.' in input_value:
    input_value = float(input_value)
else :
    input_value = int(input_value)
input_value1 = (input("두번째 값을 입력하세요 \n"))
if '.' in input_value1:
    input_value1 = float(input_value1)
else :
    input_value1 = int(input_value1)
a = input("연산자를 선택 하세요(+, -,*,/ 중 하나 입력 \n)")
rusult1 = 0
if a == "+":
    result1 = input_value + input_value1

elif a == "-":
    result1 = input_value - input_value1
elif a == "*": 
    result1 = input_value * input_value1
else:
    result1 = input_value / input_value1

input_rusult = input("결과 값 자료형 (integer ,float ,string 중 하나 입력 \n")

if input_rusult == "integer":
    print(f"결과 값은 아래와 같습니다.\n{input_value}{a}{input_value1} = {int(result1)} ")  
elif input_rusult == "float":
    print(f"결과 값은 아래와 같습니다.\n{input_value}{a}{input_value1} = {float(result1)} ")   
elif input_rusult == "string":
    print(f"결과 값은 아래와 같습니다.\n{input_value}{a}{input_value1} = {str(result1)} ") 
