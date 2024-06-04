# bar,kin,foo = 10,20
# print(f"{bar},{kin},{foo}")


# def getvalue():
#     return 2,3,4,5
# print(getvalue())

# # print(type(getvalue()))

# bar =[2,3,4,5] #리스트
# foo =(6,7,8,9) #튜플

# print(bar[0])
# print(foo[0])

# bar[0] = 20
# foo[0] = 60



# def getvalue():
#     return 2,3,4,5
# bar =[9,4,5,7,] #->list로 packing
# seo,foo,pos,kin = bar
# print(f"{seo},{foo},{pos},{kin}") 
# fin = bar
# print(fin)

# def getvalue():
#     return 2,3,4,5
# #collection unpacking
# #=>,가 있기떄문에 튜플로 팩킹해버린다
# seo,foo,pos,kin = getvalue()

# #walrus operator
# bar = "hello"

# for char in bar:
#     print(char,end="")
# print()

# for char in (foo :="world"): #변수값을 할당 
#     print(char,end="")

# def getcalcvalues(argA,argB):
#     #argA와argB의 +,-,*,/ 값을 반환하는 함수 작성
#     #값 반환시 tuple자료형으로...
#     pass
#     return argA + argB , argA -argB , argA *argB , argA/argB
# sum,substract,multiply,division = getcalcvalues(2,3)
# print(f"{sum},{substract},{multiply},{division}")


# bar +=1 
# bar =+1

# def myinoperator(avgvalue,argseqobj):
#     pass
#     for value in argseqobj:
#         if value == avgvalue:
#             return True
#     return False
   
            
# print("a" in "abc")
# bar =[3,4,5,6]
# print(4 in bar)
# print( 4 not in bar)
# print(myinoperator(3,[2,3,4]))


# def mynotinoperator(avgvalue,argseqobj):
#     pass
#     for value  in argseqobj:
#         if value == avgvalue:
#             return False
#     return True              
# bar =[2,3,4]
# foo =[2,3,4]
# pos = foo
# if bar ==foo:
#     print("참")
# else:
#     print("거짓")
# if bar  is foo:
#     print("참")
# else:
#     print("거짓")
# if foo is pos:
#     print("참")
# else:
#     print("거짓")



bar =[2,3,4]
pos = bar
if bar ==(foo := list((2,3,4))):
    print("참")
else:
    print("거짓")
    
    
print("참"if bar ==(foo := list((2,3,4,)))else "거짓")