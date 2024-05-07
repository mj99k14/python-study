#사용자에서 주민등록번호를 입력받는다
#입력받은 주민등록번호 앞 12자리를 각각 2,3,4,5,6,7,8,9,2,3,4,5로 곱한다
#나온값을다더한다 그리고 /11 나머지 구함
#11- 나머지 = 두자리경우 10버리고 1자리만사용
#최종 결과가 주민등록증 마지막 숫자랑 일치하면 유효한 주민등록 번호


text = input("주민등록 번호를 입력하세요: ").replace("-", "")
text1 = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5]
total_result = 0  # total_result 변수 초기화

for i in range(12):
    result = int(text[i]) * (text1[i])
    total_result +=  result
result3 = total_result  % 11 
result4 = 11 - result3
result5= result4 % 10
if result5 ==int(text[12]):
   print("유효한 주민등록 번호입니다.")     
else:
    print("유효하지 않은 주민번호입니다.")