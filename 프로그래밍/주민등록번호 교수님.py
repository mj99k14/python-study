def get_check_digit(arg_ssid):
    weight = [(value % 8) +2 for value in range(12)] # -> 2,3,4,5,6,7,8,9,2,3,4,5 
 
    ssid = [int(value)for value in arg_ssid] 

    sum_value = [ssid[index] * weight [index] for index in range(12)]
    return (11- sum_value % 11) % 10 
def is_valid_ssid(arg_ssid):
    arg_ssid = arg_ssid.replace("-","")
    
    if len(arg_ssid) != 13:
        return False
    
    # 체크값 계산 알고리즘 구현 필요
    check_dight = 0
    
    if check_dight == int(arg_ssid[-1]):
        return True
    else:
        return False


print(is_valid_ssid("990514-269344"))


