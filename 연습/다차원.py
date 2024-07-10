import random
#사용자로 부터 start , end ,n 값을 받는다
random_list = []
print("난수를 생성할 범위와 개수를 입력하세요")
while True:
    start = int(input("start(0이상의 정수):"))
    if 0 >= start :
        print("0이상의 정수를 입력하세요 ") 
        continue

    end = int(input("End는 (start보다 큰 정수): "))
    if  start >= end :
        print("End는 start(1)보다 커야 합니다. ")
    else:    
        break

    n = int(input("N(생성 할 난수의 개수): "))
    if not (start <= n <= end):
        print(f"{start}부터 {end}사이의 정수 여야 합니다.")
        continue
    break
#난수 생성
while len(random_list) < n:
    random_num = random.randint(start,end)
    if random_num not in random_list:
        random_list.append(random_num)

print(f"생성된 난수 리스트: \n {random_list}")

        
#start 와 end 사이에서 중복되지않은 n개의 난수를 생성후 1 차원 리스트에 저장
#1. 모든 입력 값은 유효할 때까지 재입력을 요구한다
# 2. Start는 0 이상이며 End보다 작아야 한다
# 3. End는 Start보다 커야 한다
# 4. N은 Start와 End 사이의 정수 범위 내에서 입력되어야 한다
# 5. 생성된 난수 값은 1차원 리스트에 저장 되어야 한다