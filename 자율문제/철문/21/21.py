#미리 입력된 문장 입력
sentence = """pos pos hello  bar
foo bar foo pos kin pos
test test pos"""


# sentence_num = len(sentence)
count = 0
count_lines = 1
count_char = 0
count_word = 0
count_found_word = 0

prev =""

find_word = "hello"
find_word_index = 0
find_word_len = len(find_word)
find_word_hello= []

for cur in sentence:
    if find_word[find_word_index] == cur:
        find_word_index +=1
        if find_word_index == find_word_len:
            count_found_word +=1
            find_word_index = 0
            find_word_hello.append(count-find_word_len+1)
    else:
        find_word_index = 0

    if cur == " " or cur =="\n":
        if prev != " " and prev !="\n":
            count_word +=1
    elif count ==len(sentence) -1:
        if prev != " " and prev != "\n":
            count_word +=1

    if cur != " " and cur != "\n":
        count_char +=1

    if cur =="\n":
        count_lines +=1

    count +=1

    prev = cur
         
 
 

#검색된문자열 개수
#검색된 문자열의 위치
#단어의 개수
#전체 문자 수
#줄수



# print(f"전체 글자수:{sentence_num}")

