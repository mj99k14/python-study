import random

# while 
while True:
    n = int(input("n값을 입력하세요 :"))
#n값을 받아서 n값이 1~100사이에요 ok
    if  1 <= n  <= 100:
        break
    #n값이 1~100아니에요 그럼 에러
    print("에러임 ")

num = n
#생성된 리스트  
list_num =[]    
for i in range(0,num):
    
    while True:
        random_num = random.randint(1,100)
        a =False
        for i_1 in range(0,i):
            if list_num[i_1] == random_num:
                a = True 
            break
        if not a :
            list_num.append(random_num)
            break
print(list_num)

while True:
    input_v = int(input("인덱스"))
    if 0 <= input_v < len(list_num):
        print(f"원소 값:{list_num[i]}")
        break
        
        

#n값 1 ~100사이 n값만 큼 리스트에 랜덤숫자를 넣어줘

#인덱스를 넣어줘 0~n만큼
#리스트 중하나 골라줘