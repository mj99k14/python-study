# bar = "hello world"
# print(bar[0],bar[1],bar[2],bar[3],bar[-1],bar[-2],bar[-3])
# SGFSD






# for i in range(5,0,-1):
#     print(" "*(5-i)+"*"*i) #공백 *(점점 줄어들어야하니깐 5-I,별이 줄어들어야하니깐*i)
    
    
    
    
# for i in range(1,101):
#     if "3" in str(i):
#             print(i)




# total =0
# for i in range(0,6):
#     print(f"{i}번쨰 값 입력 {i}")
#     total+= i
#     avarge =total / 5
# print(f"합계 : {total}")
# print(f"평균 : {avarge}")


# while True:
#     user =int(input("정수를 입력 하세요"))
#     if user > 0 :
#         print("양수입니다.")
#     elif user < 0:
#         print("음수입니다.")
#     else:
#         print("정수를 입력 하세요")
#         break
    
    
    
    
# while True:
#     p =int(input(f"정수를 입력 하세요"))
#     if  p < 0:
#         print("음수 입니다.")
#     elif p> 0:
#         print("양수 입니다.")
#     else:
#         print("정수를 입력 하세요")
#         break




# while True:
#     user = int(input("정수를 입력 하세요"))
#     if user < 0:
#         print("음수입니다.")
#     elif user > 0:
#         print("양수 입니다.")
#     else:
#         ("정수를 입력하세요")
#         break
        
        
        
# user = input("문자열 입력:")
# lan = input("단어 입력:")
# reslut =user.count(lan)
# print(f"단어 '{lan}'의 출현 빈도:{reslut}")







#키보드로 부터 정수를 입력 받고 입력받은 정수 개수 만큼 *을ㅊ ㅜㄹ렷
# w = input()
# for i in range(w):
#     print("*"* (i+1))f
    
# w =input()
# count =0
# for i in range(w+1):




# w =int(input())
# print("*" * w)

# w =int(input())
# for value in range(0,w):
#     print("*",w)
    
    
# print("bar1")
# print("bar2")
# print("bar3")
# print()
# print("bar4")


# w =int(input())
# for value in range(0,w+1):
#     for value1 in range(0,w+1):
#         print("*"*value1)
    

# w =int(input(""))
# for value in range(0,w+1):
#     for value1 in range(0,w+1):
#         print("*" * value,"*" * value1)






# www = int(input("입력값"))
# for value in range(0,www):            #세로           #중첩 반복문 
    
#     for value in range(0,www):        #가로
#         print("*",end ="")    #end =""는    개행문자  (\n)   
        
#     print()


# count = 1
# for _ in range(3):
#     for _ in range(2):  #e 두개 짜리가 3개잇다는말
#         print(count)
#         count +=1
        
        
# for _ in range(3):
#     for _ in range(3): #안쪽에있는 for문 *밖쪽 for문 
#         print("*", end="")
#     print()
    
    
    


# for _ in range(2):       #세로
#     for _ in range(4):    #가로
#         print("*",end="")
        
#     print()               #for문 안에 있어서 print()두줄 띄우기
#     print()
    
str_n1= input("문자열 입력: ")
words = input("단어 입력")
count =0
for words in str_n1:
    count+=words
    print(f"단어{words}의 출현 빈도{count}")
    