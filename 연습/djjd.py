count =1
num =4
blank = num - 1
#세로
#가로
for _ in range(num):  #공백 먼저
    for _ in range(blank):
        print(" ", end = "")
       
    for _ in range(count):#*
        print("*", end = "")
    print()
    blank -= 1
    count += 2
         