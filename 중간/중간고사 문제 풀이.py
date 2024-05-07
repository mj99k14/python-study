
count = 0
for i in range(1,6):
    msg = str(i)+"번째 값을 입력하세요:"
    a =int(input(msg))
    count +=a
    
    
avg = count /5
print("합계 : ",count)
print("평균 : ",avg )


# sum = 0
# for count in range(1, 6):
#     msg = str(count) + "번째 입력하세요: "
#     input_value = int(input(msg))
#     sum += input_value
    
    
# avg = sum / 5    


# # 합계, 평균 출력
# print("합계: ", sum)
# print("평균: ", avg)