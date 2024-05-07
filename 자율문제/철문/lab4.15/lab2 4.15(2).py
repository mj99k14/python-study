# 사용자는 먼저 생성할 랜덤 정수의 개수 N을 입력합니다.
# • N은 1 이상 100 이하의 정수여야 합니다. 
# ② 입력받은 N에 따라, 1부터 100까지의 숫자 중 중복되지 않은 N개의 랜덤 숫자를 생성합니다. 
# ③ 생성된 랜덤 숫자들은 리스트에 저장됩니다. 
# ④ 사용자에게 리스트에서 원하는 원소의 인덱스를 입력받습니다.
# • 인덱스는 0부터 N−1까지의 값이어야 합니다. 
# ⑤ 프로그램은 사용자가 선택한 인덱스에 해당하는 리스트의 원소를 출력합니다.

# import random
# n = input("N값을 입력하세요 (1 - 100): ")
# random_number =random.randint(1,100)
# list_num =[]

# for i in random_number:
#     for o in random_number:
#         list_num.append(o)
        
# # while True:
#     if  n < 0  or  n >101:
#         print("에러: n은 1 이상 100 이하의 정수여야 합니다.")
#         break
#     else:
#         list_num.append(random_number)
#         print("생성된 리스트:[]")
                


#랜덤
# import random
# def unm():
#     random_number =random.randint(1,100)
#     if unm(random_number):
#         return random_number
#     else:
#         return unm()
    
            
 
 
#     while True:
#     n = int(input("N값을 입력하세요0"))
     
    
    
    
# import random
# n = input("N값을 입력하세요 (1 - 100): ")
# random_number =random.randint(1,100)
# list_num =[]

# for i in random_number:
#     print(list_num.append(random_number))
    
    
    
    
    

# while True:
#     n = int(input("N값을 입력하세요 (1 - 100): "))
#     bar = list()
#     if 1 <= n or n  <= 100:
#         for _ in range(n):
#             bar.append(random.randint(1,100))
#         print("생성된 리스트:",bar)
#     else:
#         print("에러: n은 1이상 100이하의 정수여야 합니다.")
#         break
# #중복 체크
#     duplicates =  set()
#     for i in bar:
#         if bar.count(i) >1:
#             duplicates.add(i)
#     else:   
#         print("에러: n은 1이상 100이하의 정수여야 합니다.")
#         break
    
  
# index = int(input(f"원하는 원소의 인덱스를 입력하세요(0-{n-1}): ")) #넣은 만큼 
# if  0 <= index < n:
#     print("선택한 인덱스 원소: ",bar[index])
# else:
#     print("에러: 유효한 인덱스 범위를 벗어났습니다.")

    


    
    
    
    
    
    
    
import random    
n = int(input("N값을 입력하세요 (1-100): "))    
generated_random_num = []
#5번쨰
for trial_count in range(0,5):
    found_dupliation = True
    while found_dupliation:
        found_dupliation = False
        random_num = random.randint(1,6)
        
        
        
    for made_num_index in range (0,trial_count):
        if generated_random_num[made_num_index] == random_num:
            
            found_dupliation = True
            break
    generated_random_num.append(random_num)
n= int(input(f"원하는 원소의 인덱스 범의를 벗어났습니다{(0-n)}"))
if 0 <= made_num_index or n >= made_num_index :
    print(f"선택한 인덱스 원소{generated_random_num.append(random_num)}")
else:
    print("에러: 유효한 인덱스를 입력하세요")