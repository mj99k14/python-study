import random

# 사용자로부터 start, end, n 값을 받는다
random_list = []
print("난수를 생성할 범위와 개수를 입력하세요")

while True:
    start = int(input("start(0 이상의 정수): "))
    if start <= 0:
        print("start는 0 이상의 정수여야 합니다. 다시 입력하세요.")
        continue  # start가 올바르지 않으면 다시 입력받음

    end = int(input("end(start보다 큰 정수): "))
    if start >= end:
        print("end는 start보다 커야 합니다. 다시 입력하세요.")
        continue  # end가 올바르지 않으면 다시 입력받음

    n = int(input("n(생성할 난수의 개수): "))
    if not (start <= n <= end):
        print(f"n은 {start}부터 {end} 사이의 정수여야 합니다. 다시 입력하세요.")
        continue  # n이 올바르지 않으면 다시 입력받음

    # 입력이 유효하면 루프를 종료
    break

# 난수 생성
while len(random_list) < n:
    random_num = random.randint(start, end)
    if random_num not in random_list:
        random_list.append(random_num)

print(f"생성된 난수 리스트: {random_list}")

