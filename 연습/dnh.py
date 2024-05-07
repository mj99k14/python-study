# m = 1.3223213213132

# print(f"{m:.2f}")


# basevalue =float(input("기본값을 입력하세요: "))
# a="1.더하기"
# print(a)
# b="2.뺴기"
# print(b)
# c="3.곱하기"
# print(c)
# d="4.나누기"
# print(d)
# def select0peration():
#     global basevalue
#     if cho ==4 and in1 == 0:
#        return "에러: 0으로 나눌수 없습니다."
#     else:
#         if cho == 1:
#             cho1=in1 + basevalue
#             return cho1
# cho=int(input("선택: " ))
# in1=int(input("숫자 입력: "))
# print("연산 결과:",basevalue)







# a,b,c=map(int,input().split())
# max_number=max(a,b,c)
# if  max_number and range(1,7):
#     n= max_number * 100
#     print(n)
# else:
#     if a==b==c and a in range(1,7):
#         b=10000 + a * 1000
#         print(b)
#     if a==b and a in range(1,7):
#         c= 1000 + a * 100
#         print(c)
#     elif b==c and b in range(1,7):
#         c= 1000 + b * 100
#         print(c)
#     elif a==c and a in range(1,7):
#         c= 1000 + a * 100
#         print(c)
        





# a, b, c = map(int, input().split())
# max_number = max(a, b, c)

# if max_number:
#     n = max_number * 100
#     print(n)
# else:
#     if a == b == c:
#         n = 10000 + a * 1000
#         print(n)
#     elif a == b :
#         n = 1000 + a * 100
#         print(n)
#     elif b == c :
#         n = 1000 + b * 100
#         print(n)
#     elif a == c and a in range(1, 7):
#         n = 1000 + a * 100
#         print(n)





# print("hello")

# print("안녕하세요")


# #CRUD :update
# #befor : [2,3,4,5,6]
# bar[1] =

# bar=[10,12,15,19,56]

# del bar[1] #1번째 원소를 삭제, 삭제
# print(bar,len(bar))

# bar.remove(56) # 해당원소를 만나면 삭제 ,밑에 값을 반환 
# print(bar,len(bar))

# print(bar.pop(0)) #2번쨰 원소를 삭제, 삭제 후 값을 반환 #인자값을 안넣으면 마지막 값을 꺼내온다 



#중복값을 찾자!
import random
n = 5
max_num = 6

sample_list = [ value for value in range(1, max_num) ]          #Value 
# sample_list -> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

random_list = []

for trial_count in range(0, n):#중복되지않는값을 5번뽑아야함
    random_index = random.randint(0, len(sample_list) - 1)  #len 은 마지막 숫자를 포함하기 떄문에 0~4 랜덤 값 
    random_num = sample_list.pop(random_index)#반환한 값을 가져와서 num 에담아줌 
    random_list.append(random_num)    
    
print(random_list)


#list comperehention 




bar =[1,2,3,4,5,6]
bar.clear()
print(bar)


foo =[1,2,3,4,5,6]
del foo   #리스트를 지우지 않고 참조 변수 foo를 지움 (다시 접근 불가)