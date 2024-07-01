
# # #def 함수명(매개변수):
# # #       함수 호출 시 실행 명령어

# # #함수 정의: ->1번
# # def print_name(name):
# #     print(name,"님 하이하이")

# # # ->이름을 써주는 이유 (구분 하기위해)
# # #함수 호출 : -> 2번 
# # print_name("김성식")
# # print_name('조원준')





# # def suma():
# #     input_user1, input_user2, input_user3 = map(int,(input("정수: ").split()))
# #     sum = input_user1 + input_user2 + input_user3
# #     sum_1 = sum / 3

# #     print(sum , sum_1)
# # suma()


    
        
# # def get_int(arg_num):
# #     input_value = []
# #     for _ in range(arg_num):
# #         input_value.append(int(input("입력 값 :")))

# #     return input_value

# # def get_sum_avg(arg_list):
# #     sum = 0
# #     for value in arg_list:
# #         sum+= value

# #     avg =  sum / len(arg_list)
# #     return sum , avg


# # def get_sum(arg_list):
# #     sum = 0
# #     for value in arg_list:
# #         sum += value

# #         return sum
    

# # input_list = get_int(5)

# # sum , avg = get_sum_avg(input_list)

# # print(sum , avg)

  

# def sum (arg_frist, arg_secound):
    
#     sum = arg_frist + arg_secound
    
#     if sum < 0:
#         print("음수")
#         return
#     #함수 정의 시 return 있어도 되고 없어도 된다 .즉option이다 

#     return sum #1)함수 종료
#                #2)값 반환
#                # ->호출된 곳으로 되돌아간다
# result = sum(-2, -3) 
# print(result)

# #함수를 호출하면 함수가 정의되어있는곳으로 간다 


# #한개 정수키보드 입력

# def s():
#     input_user = int(input("입력 하셈:"))
#     if input_user % 2 == 0:
#         msg = "짝수"
#     else:
#         msg = "홀수"
    
#     return msg 

# result = s()
# print(result)

# def s():
#     input_user = int(input("입력 하셈:"))
#     if input_user % 2 == 0:
#         msg = "짝수"
#     else:
#         msg = "홀수"
    
#     return msg 
# print(s)
# s()
# print(result)

# def s():
#     input_user = int(input("입력 하셈:"))
# msg = "짝수"if input_user % 2 == 0 else: 홀수
#         msg = "짝수"
#     else:
#         msg = "홀수"
    
#     return msg 
# print(s)
# s()



# 함수에 인자 값 4개를  입력받아 합계와 평균을 반환하는 함수를 작성하라
# #그리고 반환ㄷ힌 합께와 평균
# a = [80,45,77,87]
# i1= 0
# def s():

#     i1= 0
#     for  i in a :
#         i1+=i 
#     print(i1)

# s()

# def s():
#     avg = i1 / 4
#     print(avg)

# s()


# def get_sum( arg1,arg2,ag3,arg4):
#     sum = arg1 + arg2 + ag3 + arg4

#     avg = sum / 4

#     return sum , avg #반환값이 두개 이상이면 tuple로 변환후 반환한다

# sum ,avg = get_sum(1,2,3,4,)  #(10, 2.5)
# print(sum,avg) 
 


# value =get_sum(1,2,3,4)
# print(value[0],value[1])


#call-by-value , call-by-reference


# bar = 3  #처음에 bar가 선언이 3으로 선언이되었고
# def foo(bar):  #계산 
#     bar =  bar + 1
#     print("1: ",bar) #bar = 4

# #호출끝남 

# foo(bar)  #호출할때 bar = 3  

# print("2: ", bar)  # 호출이 끝나기 때문에 3




