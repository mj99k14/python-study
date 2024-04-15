p=int(input("현재 온도(섭씨)를 입력하세요"))
p1=float(p)     #정의를 해주면 쉽다
print ("현재 온도:",p1,"도")
if p> 30:
    print("수영")
else:
    if 20 <= p < 30:
        print("등산")
    elif 10 <= p <20:
        print("자전거 타기")
    else:
        print("스키")