def juminnumber(*arg_a):
    while True:
        u = []
        if len(arg_a)< 15:
            print("다시입략")
        else:
            print("유효")
            break
    for i in arg_a:
        if "-" in arg_a:
            u.append(i)
    s = [2,3,4,5,6,7,8,9,2,3,4,5]
    a = []
    for i in u:
        for a in s :
            sum = i * a
        a.append(sum) #곱해준거 
    sum = 0
    for s in a:
        sum += s #더해준거
    
    r = sum % 11
    r1 = r - 11
    if len(r1) < 10:
        r1 / 10

    if r1 == arg_a[-1]:
        print("유효한 주민등록번호")
    else:
        print("유효하지않음")
arg_a =  input("주민등록번호를 입력하세요:")
juminnumber(arg_a)

        
  
        





       



