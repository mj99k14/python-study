numbers_str = input("숫자들을 쉼표로 구분하여 입력하세요: ")
numbers = numbers_str.split(',')
list_m =[]
count = 0
kg100_choka = False
for i in numbers_str:
   
    num= int(i)
    count +=num
    list_m.append(i)
    