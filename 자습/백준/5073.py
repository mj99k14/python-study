
# while True:
#     a = list(map(int,input().split()))
    # g = a[:]
    # x = max(a)
    # if a[0] == 0 and a[1]==0 and a[2]==0:
    #    break
    # if g[0] == x:
    #     del g[0]
    # elif g[1] == x:
    #     del g[1]
    # else:
    #     del g[2]
    # if sum(g) > x:
    #     if a[0]==a[1]==a[2]:
    #         print("Equilateral")
    #     elif a[0] == a[1] or a[0] == a[2] or a[1] == a[2]: 
    #         print("lsosceles")
    #     else:
    #         print("scalene")
    # else:
    #     print("lnvalid")
   
       
            
# while True:
#     a = list(map(int,input().split()))
#     if a[0]==0 and a[1]==0 and a[2]==0:
#         break
#     a.sort()
#     x = a[2] #-> 가장 큰 수
#     g=a[:2]  #-> 나머지 수
#     if sum(g) > x:
#         if a[0]==a[1]==a[2]:
#             print("Equilateral")
#         elif a[0] == a[1] or a[0] == a[2] or a[1] == a[2]: 
#             print("lsosceles")
#         elif a[0]!=a[1]!=a[2]:
#             print("Scalene")
#     else:
#         print("lnvalid")
   
while True :
  a, b, c = map(int, input().split())
  if a == b == c == 0 :
    break
  if sum((a, b, c)) - max((a, b, c)) <= max((a, b, c)) :
    print("Invalid")
  elif a == b == c :
    print('Equilateral')
  elif a == b or b == c or a == c :
    print("Isosceles")
  else :
    print("Scalene")
