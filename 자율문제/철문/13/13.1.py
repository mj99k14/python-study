#사용자로 부터 문자열 입력
user = input("문자열 입력: ")
word= input("단어 입력: ")
count_user = user.count(word)
print(f"단어 {word}의 출현 빈도:{count_user}")
#지정단어가 몇번 나오는지 카운트
#단어와 문장은 공백으로 구분됩니다. 
# 결과는 단어의 출현 횟수를 출력합니다