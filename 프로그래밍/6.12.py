#argument

#1) positional argument

# def foo(arg_a,arg_b,arg_c):
#     print(arg_a,arg_b,arg_c)

# foo(1,2,3)

# def pos(arg_a,arg_b,arg_c):
#     print(arg_a,arg_b,arg_c)

# pos(arg_c= 1,arg_a = 2,arg_b= 3)



# data = [2, 3, 4, 5]
# def kin(arg_a ,arg_b ,arg_c ,arg_d ):
#     print(arg_a , arg_b, arg_c, arg_d)

# kin(data)


# import random
# lunch =["짜파게티","불닭","짜장밥","카레"]
# s = random.choice(lunch)
# print(s)


#구구단 출력하는 프로그램을 작성 2
#함수로 작성

# def gugudan(arg_start , arg_end =None):
#     if arg_end == None:
#         for i in range(1,10):
#             print(f"{arg_start} * {i}  = {arg_start * i }")
#     else:
#         for i in range(arg_start , arg_end+1):
#             for s in range(1,10):
#                 print(f"{i} * {s} = {i * s}")

            
# gugudan(2,5)



# def printmultable(arg_start , arg_end =None):
#     arg_end = arg_start +1 if arg_end is None  else arg_end +1
#     # if arg_end == None:
#     #     arg_end = arg_start
#     for i in range(arg_start , arg_end + 1):
#         for s in range(2,10):
#             print(f"{i} * {s} = {i * s}")
# printmultable(2)






# * -> 가변 : tuple로 받겠다
# def foo(*args):
#     print(len(args))
#     for value in args:
#         print(value)

# foo(1)
# foo(1,2,3,4,5,6,7,8,9,10,11,12)


# def bar(*args):
#     if len(args) == 1:
#         start = end = args[0]
#     elif len(args) == 2:
#         start,end = args
#     else:
#         return
    
#     for dan in range(start, end + 1):
#         for num in range(1,10):
#              print(f"{dan} * {num} = {dan * num}")

# bar(2,5)


def foo(arg_a ,arg_b ,arg_c ,arg_d,arg_e): #
    print(arg_a ,arg_b ,arg_c ,arg_d,arg_e)
arg_list  = [value for value in range(1,6)]

foo(*arg_list)

