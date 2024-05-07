# 사용자로부터 여러 개의 숫자를 문자열로 입력 받는다 (예: ＂5, 20, 15, 60＂). 
# • 문자열을 개별 숫자로 분리하고, 
# • 각 숫자를 정수로 변환한 후, 모든 숫자의 합을 계산한다. 
# • 숫자의 총합이 100을 초과하면 해당 순간의 입력 값들과 총합을 출력하고 프로그램을 종료
# • 숫자의 총합이 100을 초과하지 않은 경우 최종 총합과 입력된 숫자들을 출력
# numbers_str = input("숫자들을 쉼표로 구분하여 입력하세요:")
# numbers = numbers_str.split(',')
# result = 0

# while True:
#     result =0
#     for num_str in numbers:
#         result += int(num_str.strip())
   
#     if result < 100:
#         print("종합이 100을 초과하지않았습니다")
#         print("입력된 모든 숫자들",numbers)
#         print("최종 총합",result)
      
        
#     else:    
#         print("총합이 100을 초과하였습니다.")
#         print("현재까지의 입력값들:",numbers)
#         print("현재까지의 총합:",result)
#         break
     



# numbers_str = input("숫자들을 쉼표로 구분하여 입력하세요:")
# numbers = numbers_str.split(',')
# result = 0
# while True:
#     for num_str in numbers:
#         result += int(num_str.strip())  # 각 숫자의 좌우 공백을 제거하고 정수로 변환

#     if result < 100:
#         print("종합이 100을 초과하지 않았습니다")
#         print("입력된 모든 숫자들:", numbers)
#         print("최종 총합:", result)
#     else:    
#         print("총합이 100을 초과하였습니다.")
#         print("현재까지의 입력값들:", numbers)
#         print("현재까지의 총합:", result)
#         break

# while True:
#     numbers_str = input("숫자들을 쉼표로 구분하여 입력하세요:")
#     numbers = numbers_str.split(',')
#     result = 0
    
#     for num_str in numbers:    #numbers 만큼 돌아가고 그 합을 구하기위해
#         result += int(num_str.strip())
   
#     if result < 100:
#         print("종합이 100을 초과하지 않았습니다")
#         print("입력된 모든 숫자들:", numbers)
#         print("최종 총합:", result)
#     elif result > 100:
#         print("총합이 100을 초과하였습니다.")
#         print("현재까지의 입력값들:", numbers)
#         print("현재까지의 총합:", result)
#         break
    
    
  

    
input_num_list = input("숫자를 입력하세요: ")

num_list = input_num_list.split(",")

sum = 0
output_list = []
over_100_flag = False

for num_str in num_list:
    num = int(num_str)
    sum += num
    output_list.append(num)
    
    if sum > 100:
        over_100_flag = True
        break

if over_100_flag:
    print("100 초과", sum)
    print(output_list)
    
else:
    print("100 이하", sum)
    print(output_list)
    
print(sum)