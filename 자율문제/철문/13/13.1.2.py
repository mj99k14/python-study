text = input("문자열 입력: ")
word = input("단어 입력: ")
count = 0 

texts = text.split() #split을 사용해서 단어들을분리  그걸texts에받음
for i1 in texts:
    if i1 == word:
        count +=1
print(f"단어{word}의 출현 빈도 :{count} ")
    