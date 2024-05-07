#for 문을 이용해서 다섯개의 정수입력
# input_value = int(input())
                    
# all = 0
# count = 0
# for i in range(0,6):
#     print(f"{input_value}번쨰 값 입력")
#     #합계
#     all += i
#     count +=1
# print(f"합계: {all}")
# #평균
# all_1 =all / 5
# print(f"평균 : {all_1}")
# # while문 사용
# 입력 받은 수가 양수인 경우 "양수"라는 문자열을 출력합니다.
# while True:
#     p =int(input(f"정수를 입력 하세요"))
#     if  p < 0:
#         print("음수 입니다.")
#     elif p> 0:
#         print("양수 입니다.")
#     else:
#         print("정수를 입력 하세요")
#         break
# #  - 입력 받은 수가 음수인 경우 "음수"라는 문자열을 출력합니다.
# #  - 입력 받은 수가 0인 경우 프로그램을 종료합니다





bar = [90,10,20]
def test(a):
    for index in range(0,len(a)):
        a[index] +=1
        
test(bar)

print(bar)