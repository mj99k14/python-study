numbes_str = input("숫자들을 쉼표로 구분하여 입력하세요: ")
numbers =  numbes_str.split(',')
result=0
list_m = []
for i in numbers:
    i= int(i)
    result += i
    list_m.append(i)
    over = False
    if result > 100:
        over = True
        print("총합을 100을 초과하였습니다:")
        print("현재까지의 입력값들: ",list_m)
        print("최종 총합:",result)
        break
        
else:
    print("총합이 100을 초과하지 않았습니다.")
    print("입력된 모든 숫자들",list_m)
    print("최종 총합:",result)