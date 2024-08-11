while True:
    a,b,c = map(int,input().split())
    if a and b and c == 0:
        break
    if a > b+c or b > c+a or c > a+b:
        print("lnvalid")
    elif a == b == c:
        print("Equilateral")
    elif a == b or a ==c or b ==c:
        print('lsosceles') 
    else:
        print("Scalene")
