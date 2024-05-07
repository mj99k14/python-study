numbers_str = input("숫자들을 쉼표로 구분하여 입력하세요:")
numbers = numbers_str.split(',')
result = 0

while True:
    for num_str in numbers:
        num = int(num_str.strip())  # 각 숫자의 좌우 공백을 제거하고 정수로 변환
        result += num
        
        if result >= 100:
            print("입력된 숫자의 총합이 100을 초과하거나 같습니다.")
            print("입력된 모든 숫자들:", numbers)
            print("최종 총합:", result)
            break
    else:
        print("입력된 숫자의 총합이 100을 초과하지 않았습니다.")
        print("입력된 모든 숫자들:", numbers)
        print("최종 총합:", result)
        break
