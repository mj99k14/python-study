s = [int(input()) for _ in range(3)] 
if sum(s) != 180:
    print("Error")
elif s[0] == 60 and s[1] ==60 and s[2] == 60:
    print("Equilateral")
elif sum(s) == 180:
    if s[0]==s[1] or s[0]==s[2] or s[1]==s[2]:
        print("Isosceles")
    else:
        print("Scalene")

    
