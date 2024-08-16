import random

def print_bingo_board(arg_list,col_num):
    for index in range(len(arg_list)):
        print(arg_list[index],"\t",end="")

        if (index + 1) % col_num == 0:
            print()


while True:
    n =int(input("n값: 3 ~ 6"))

    if 3  <= n <= 6:
        break

bingo_element_num = n * n


bingo_b