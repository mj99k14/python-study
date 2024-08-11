# n =int(input())
# a = []
# while True:
#     for i in range(2,n):
#         s = n / i 
#         if s and n % i == 0:
#             s 
            

# n =int(input())

# if n == 1:
#    print('')

# for i in range(2,n+1):
#    if  n % i == 0:
#       while n % 1  ==  0:
#          print(i)
#          n = n / i








n = int(input())
i = 2
while n != 1:
    if n % i == 0:
        print(i)
        n = n / i
    else:
        i += 1

   
       