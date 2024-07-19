#rgs 값이 1개또는 2개
#args 값이 1개이면,  args Xargs 매트릭스 생성해서 반환
#args갑이 2개이면 arg[0] x arg[1] 매트릭스를 생성하여 밚환
#초기값은 1~100 사이 랜덤값으로 설정
import random
def get_matrix(*argS):

    if  not(1 <= len(argS) <= 2):
        return None
    matrix_row = argS[0]

    if len(argS) ==1:
        matrix_col = argS[0]
    else:
        matrix_col =argS[1]
    data_frame = {
        "num_row" : matrix_row,
        "num_col" : matrix_col,
        "data" : [[random.randint(1,100) for _ in range(matrix_col)]\
                  for _ in range(matrix_row)]


    }
    data_frame['sum'] = lambda: sum([sum(row) for row in data_frame['data'] ])
    # bar = [[random.randint(1,100) for i in range(matrix_col)] for i in range(matrix_row)]
    return data_frame

foo = dict()
foo['a'] =get_matrix(3,2)
foo['b'] = get_matrix(3,2)
foo['c'] = get_matrix(3,2)
foo['d'] = get_matrix(3,2)

result = sorted(foo.items(),key= lambda arg:arg[1]['sum']())
for item in result:
    print(item[1]['sum']())


# # print(get_matrix(3))
# foo = get_matrix(3,2)
# print(foo["num_row"],"\t",foo['num_col'])
# print(foo['data'])
# print(foo['sum']())

#하나의 데이터가 있는데 설명하기위한 데이터가 ->META DATA

