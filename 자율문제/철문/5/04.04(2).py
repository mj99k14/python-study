
#전역 변수 선언및 사용자로 부터 입력받기

basevalue =  float(input("기본값을 입력하세요: "))
#사용자가 1~4까지 연산방법을 고른다
print("1. 더하기")
print("2. 빼기")
print("3. 곱하기")    
print("4. 나누기")
choice=int(input("선택: "))
num=int(input("숫자 입력: "))
#고른 번호에 따라 연산 하는방법이 달라진다
def select0peration():
    global basevalue
    
    if choice==4 and num==0:
        print("에러: 0으로 나눌 수 없습니다.")
        return
    if choice == 1:
        basevalue=num+basevalue
    elif choice == 2:
        basevalue=basevalue-num
    elif choice == 3:
        basevalue=basevalue*num
    elif choice == 4:
        basevalue=basevalue/num
    
    
    print("연산 결과:",basevalue,)

select0peration()
              

    #숫자 입력을받는다
    #연산 결과는 소수점으로나타낸다
    
    
    
    
    
    
    

    