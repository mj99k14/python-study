import random

#1 에서 100 까지의 랜덤 정수를출력하세요
while True:
    trail_num = int(input("n값: "))
#입력 받은 값 만큼 유효범위
    if 1 <= trail_num <= 100:
        break
    
#n값이 1~100이아니면 에러 입니다
    print("에러다 자슥아")

#중복 값이 없는 정수의 개수
num = trail_num
made_list =[]
for count in range(0,num):
    while True:
        random_num = random.randint(1,100)
        
        a = False
        for m in range(0,count):
            #중복값이있으면
            if made_list[m] == random_num:
                a = True
                break
        if not a :
            made_list.append(random_num)
            break
print(made_list)


while True:
    input_m = int(input("인덱스 입력해 : "))
    if 0 <= input_m < len(made_list):
        print(f"원소 값:{made_list[m]}")
        break
    
    
    print("에러")
#n값 안에 들어간다면 n값만큼 랜덤수를 뽑아낸다
    
#인덱스를 받는다  범위는 n값만큼 랜덤 리스트안에서 받는다
#범위를 벗어나면 에러