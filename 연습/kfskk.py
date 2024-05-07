#정수 3개를 입력받아서
abest= int(input())
bbest= int(input())
cbest= int(input())
if abest == bbest != cbest:
    print(abest)
    if abest ==cbest !=bbest:
        print(abest)
    else:
        print(cbest)
elif abest> bbest and abest>cbest:
    print(abest)
elif bbest >cbest and bbest>abest:
    print(bbest)
else:
    print(cbest)



    
    
# 정수 3개를 입력 받아서 제일 큰 값을 출력하시오?

input_1 = int(input("1번"))
input_2 = int(input("2번"))
input_3 = int(input("3번"))

max = input_1

if max < input_2:
    max = input_2

if max < input_3:
    max = input_3
    
print(max)




max = -1

for trial_count in range(1, 4):
    msg = str(trial_count) + "번"
    input_value = int(input(msg))
    
    if max < input_value:
        max = input_value
    
print(max)