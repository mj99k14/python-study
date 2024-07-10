def print_matrix(arg_list):
    for row in arg_list:
        for col in row:
            print(col,"\t",end="")
        print()
    print("-" * 20)

def del_col(arg_list ,col_num):
    for i in range(len(arg_list)):
        del arg_list[i][col_num]


matrix =[[1,2,], [4,5,6], [7,8,9,10]]

# print_matrix(matrix)

# del matrix[2][2] # ->9를 없애줌
# for i in matrix:
#     del i[1]   # matrix에 원소들이 i 에 저장되고 i의 2번쨰가 삭제되기떄문에 
#     #1  3
#     #4  6
#     #7  9

# print_matrix(matrix)
# del_col(matrix,1)
matrix = [[1,2],[4,5,6],[7,8,9,10]]\
        ,[[10,11,12,14],[15,23,4,5,6]]
# print(len(matrix))
# print(len(matrix[0])) # 1,2, ->2
# print(len(matrix[1])) # 4,5,6 -> 3
# print(len(matrix[2])) # 7,8,9,10 -> 4 

# matrix[2].append(100)
# print(matrix)

# matrix[2][2]=1000
# print(matrix)

# matrix.append([8,9,10,11])
# print(matrix)


# a =[8,9,10,11]
# matrix.append(a)
# print(matrix)
# a = [100,200,300]
# matrix.insert(2,a) #  ->insert는 삽입 해주는거 (위치,삽입할것)  
# print(matrix)

print(matrix)

