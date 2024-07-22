input = input().split()
print(input)
sum_s = 0.0
while input == 0:
    if input[2] == "F" or input_user [2]== "P":
        continue
        
    else:
        sum += input[1]

    print(sum)


# 입력을 받고 리스트로 변환
input_user = input().split()
print(input_user)

sum_s = 0.0

for i in range(0, len(input_user), 3):  # 3개씩 묶음으로 처리
    if input_user[i+2] == "F" or input_user[i+2] == "P":
        continue
    else:
        sum_s += float(input_user[i+1])

print(sum_s)
