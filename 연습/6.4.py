
# for i in range(1,5): #1,2,3,4
#     for j in range(1,4): # 1,2,3  
#         for s in range(1,5): #1,2,3,4 밑에서 부터
#             if i == 2:
#                 break
#             print(i, ":", j,";", s)


#break 동작 절차
#1)위로 올라간다
#2)첫번째로 만나는 반복을 종료한다



# for k in range(1,5):
#     for i in range(1,3):
#         for j in range(1,4):
#             if  j == 2 :
#                 break
#             print(i, ":", j)

            
for k in range(1,5):#1
    for i in range(1,3):#1,2,
        for j in range(1,4): # 1 ,2, 3,
            continue
        print(i, ":", j)