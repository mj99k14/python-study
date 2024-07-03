# a=[]
# for i in range(9):
#     s = int(input())
#     a.append(s)

# max_value = max(a)
# count =  a.index(max)
# print(max_value, count +1) 

a =[int(input())  for i in range(9) ]

print(max(a),a.index(max(a))+1)