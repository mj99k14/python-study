# value = int(input(""))
# for i in value:
#     if  1<= i <=100:
        
        
        
        
# a, b, c = input().split()
# a, b, c = int(a), int(b), int(c)
# print((a if a < b else b) if ((a if a < b else b) < c) else c)




# a if a < b else b
# if a < b:
#     print(a)
# else:
#     print(b)
    
    
    
# ((a if a < b else b) < c)

# if a<c and b<c:
#     print(c)
# else:
#     if a < b:
#         print(a)
#     else:
#         print(b)
        
        
a, b, c = input().split()
a, b, c = int(a), int(b), int(c)      
print((a if a < b else a) if ((a if a < b else a) < c) else c)
    
    
