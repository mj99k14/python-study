
user_input = list(map(int,input("숫자 입력하세요: ").split()))

def is_valid_input(user_input):
 
    for i in user_input:
        if 2 > i or i > 9: 
            return False
    return True

if not is_valid_input(user_input):
    print("야내가만만하냐 2 ~ 9중에 입력하라고~ ")
      
else:
    if len(user_input) == 1:
            arg_start = user_input[0]
            arg_end = arg_start
    else:
        arg_start = user_input[0]
        arg_end =user_input[1]

    def gugudan(arg_start,arg_end):
        for i in range(arg_start , arg_end + 1):
                for u in range(1,10):
                    print(f"{i} * {u} = {i * u}")

                print()

    gugudan(arg_start,arg_end)
                    