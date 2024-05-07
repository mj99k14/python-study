
#사용자에게 입력받음
user = input("문자열 입력: ")
word = input("단어 입력: ")
b=[]
count = ""
#공백전까지만 단어 취급 , 문자열을 단어로 나눠주기 위함 
for i in user:
    if i != " ":
        count+= i 
    else:
        b.append(count)
        count=""
         
        

#마지막 단어처리 
if count:
    b.append(count)
    
    
#결과 단어 횟수
word_count =0
for i1 in b:
    if i1 == word:
        word_count += 1 
        
print(f"단어 {word}의 출현 빈도: {word_count}")