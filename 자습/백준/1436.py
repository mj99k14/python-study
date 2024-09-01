s = int(input())
count = 0
number =666
while count< s: # 카운트 가 s만큼 돌아야하기떄문에
    if '666' in str(number):  # -> 숫자에 666만 포함해야하기떄문에
        count +=1 
    number +=1

print(number -1) # 만약에 1666이나와도 number+1이되고 프린트되기 떄문에 -1 을해줘야함