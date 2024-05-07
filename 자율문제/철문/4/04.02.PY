msg="프로그램 시작"
print(msg)

def bar(argb1,args2):
    msg1 = "안녕!" + foo(argb1)
    print(msg1)
    
    msg2 = "hello!" + foo(args2)
    print(msg2)


def foo(argf):
    msg = argf + "님"
    msg = pos(msg)
    return msg

def pos(argp):
    msg = "*" + argp + "*"
    return msg
    
bar("정영철","YC Jung")

msg = "프로그램 종료"
print(msg)