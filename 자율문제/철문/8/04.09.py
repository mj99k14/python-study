import random

def generate_password(length):
    #대문자,소문자,숫자를 포함한 문자열 정의
    uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lowercase_letters = uppercase_letters.lower()# 대문자를 소문자로 변환
    digits = '0123456789'
    #모든 가능한 문자를 하나의 문자열로 결합
    all_characters = uppercase_letters + lowercase_letters + digits
    
    #패스워드 초기화
    password = ""
    
    #지정된 길이만큼 랜덤 문자 선택
    for _ in range(length):
        password += random.choice(all_characters)# 랜덤 문자를 패스워드에 추가
        #생성된 패스워드 반환
        
    #함수 호출하여 패스워드 생성
    check1 = False #대문자
    check2 = False #소문자
    check3 = False# 숫자 확인
    
    #비밀검증
    for i in uppercase_letters: #대문자 확인
        if i in password:
            check1 = True
            break
        
    for i in lowercase_letters: #소문자 확인
        if i in password:
            check2 = True
            break
        
    for i in digits: #숫자 확인
        if i in password:
            check3 = True
            break
    #검증을 통과했으면 password를 반환 통과하지 못하였으면 함수를 재호출
        if check1 and check2 and check3:
            return password
        else:
            return generate_password(length)
#입력
password_length = int(input("생성할 패스워드의 길이를 입력해주세요: "))

#무한 반복을 막기 위하여 3자리 이상의 경우에만 동작
if password_length >= 3:
    generated_password = generate_password(password_length)
    print(generate_password)
else:
    print("3자리 미민의 패스워드는 생성할 수 없습니다. ")
    
    
    
    
    