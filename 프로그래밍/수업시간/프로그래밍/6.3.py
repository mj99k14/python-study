# #화면에 1 을 10번 출력 
# for i in range(10):
#     print(1)

# for _ in range(10):  # "반복"만 하는경우 단순하게 -을 써주면 간단하게 알수있다.
#     print(1)


# #range(반복,회수)
# #range(시작값,종료값):시작 값은 첫번째 증감값에 대한 적용이 가능할때 선택 
# #range(시작값,종료값,증감값)

# for i in range(7,-8):
#     print(i)
#     #range의 무조건 시작값을 찍지않는다 
#     #반복값이 0이될수도있음 
#     #다음조건이 참이 되어야지 출력이된다


# for _ in range(9):
#     print(_,end="")


# print("\n", "*" *  20)


# for dan in range(2,10):
#     print(dan,end="")


#
#list comprehension (리스트 컴플리헨션)
#  ->리스트 내 원소 값들을 for 문을 사용하여 동적으로 생성  
#프로그램에서 실행하면서 변하는것 ->동적
# [expression for item in item_list if conditional expression]

# list_m =[]
# for i in range(1,21):
#     list_m.append(i)
# print(list_m)


# list_m =list(i for i in range(1,21))
# print(list_m)

# list_m = [i for i in range(1,21)]
# print(list_m)


# list_m = [7 for _ in range(8)] # 7 print 되어야할 값 , range(8)7까지 나와야하기때문에
# print(list_m)



# #value에 if조건이 참이되는 값이 bar list안에 저장되어 print된다
# bar = [value for value in range (1,21) if value % 3 ==0]
# print(bar)


# foo = ["abc", "dcb","ef","gh"]
# bar = [ c1 for c1 in foo   if "c" in c1]
# print(bar)


# #3
# foo = ["abc", "dcb","ef","gh"]
# bar = [ c1 for c1 in foo if len(c1)>=3]
# print(bar)

#삼항 연산자: 참 if 조건식 else 거짓  -> 수식 
# foo = [  i * 20  if  i % 2 == 0 else i *10  for i in range(1,11)]
# print(foo)

#둘다 만족 되면 print == and 랑같음
# s_list =[ value for value in range(1,21) if value % 3 ==0  if value %4 == 0]


# while True :
#     user = int(input())
#     if user >0:
#         print(user)
#         break
#     else:
#         print("다시 입력")
        


# while True :
#     user = int(input())
#     if user >0:
#         break
#     else:
#         print("다시 입력")
        



# count = 1

# while count <= 10:
#         count += 1
#         print(count)
# bar = ["hello","world","richard"]    
# found_word = False
# for word in bar:

#     if word  == "word":
#         print("word 찾았음")
#         found_word = True
#         break

# if not found_word:
#     print("단어 못찾음 ")



bar = ["hello","world","richard"]    
#flag 변수 ->깃발 :boolean
# found_word = False
for word in bar:

    if word  == "wd":
        print("word 찾았음")
        # found_word = True
        break

# if not found_word:
else:
    print("단어 못찾음 ")
    
