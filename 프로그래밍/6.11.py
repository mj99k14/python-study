# def name(arg_name): #arg_name ->매개 변수 최소 0 ~ 무한대
#     print(arg_name,"hello")
#  #
# #매개변수에 넣어주는 값이 인자값
# #인자값은 넣어줄떄마다 바뀔수있음
# name("mj") # - > 인자값


# foo = [2,3]

# bar = [5,4]

# foo,bar = 7,8

# print(foo,bar)


bar = [2,3,5]
def foo (arg_list):
    copied = arg_list[:]

    copied[0] = 100


foo(bar)

print(bar)#2, 100 ,5