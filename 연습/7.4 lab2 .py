# bar =  [0,0,0,0,0,0]

# bar = [0 for _ in range(6)]
# print(bar)

# bar = [0] * 6
# print(bar) 

# bar = [10,20,30,40]
# bar.append(20) #뒤에 추가
# print(bar)
# bar.insert(2,100) #삽입
# print(bar)



# print(bar.pop(2))  # pop은 원소를 뺼수있음
# print(bar)

 
# #pop
# while len(bar) > 0:
#     item = bar.pop(0)
#     print(item)


# bar = [1,2,3],[4,5,6],[7,8,9]
# print(bar[2][2])

#안쪽 브라켓이 원소의 개수 를 나타냄
#3~7 = 4 개의 줄을 가짐   
# a = [[ 0 for s in range(3)] for s in range(3,7) ]
# print(a)
# # -> [0,0,0] ->이거를 4줄로 나옴 

# bar =[[0  for s in range(4)],[[0]*4],[s for s in range(5,9)]]
# print(bar)





# bar = [[10,20,30],[40,50],[60,70,80,90]]
# for row in bar: # ->  세로 : 3줄 ->브라켓 개수 
#     for item in row: #[안에원소들을 돌음] -> 가로 
#         print(item,end=' ')
#     print()




rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))


matrix = [[0 for _ in range(columns)] for _ in range(rows)]


for i in range(rows):
    for j in range(columns):
        matrix[i][j] = int(input(f"Enter value for [{i}][{j}]: "))
# print(matrix)

for row in matrix:
    for item in row:
        print(item,end=' ')
    print()