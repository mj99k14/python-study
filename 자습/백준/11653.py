# n =int(input())
# a = []
# while True:
#     for i in range(2,n):
#         s = n / i 
#         if s and n % i == 0:
#             s 
            

n =int(input())
d = []
while n <1:
    for i in range(2,n):
        if n % i == 0:
            n = n / i
            d.append(i)



       

   
       