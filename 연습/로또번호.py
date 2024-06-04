import random
list_m = []
# 고유성: 선택된 6개의 번호는 중복되지 않아야 합니다.
while len(list_m)<6:
    random_mun = random.randint(1,46)
    if random_mun not in list_m:
        list_m.append(random_mun)

list_m.sort()
print(list_m)
# 정렬: 선택된 번호는 오름차순으로 정렬하여 출력해야 합니다

