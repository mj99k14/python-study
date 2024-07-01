
msg = """pos foo foo pos test pos
foo kin pos kin
dk test pos"""



count = 0 #글의수
count_lines = 1 #줄 수 
count_char = 0 #글자 수
count_word = 0 #단어수
count_found_word = 0 #검색된 단어수


prev = "" # 이전 글자를 저장하기 위한 변수

find_word = "pos"
find_word_index = 0 #현재 단어랑 일치하는 수
find_word_len = len(find_word) #찾고자 하는 단어의길이
find_word_pos = [] #찾은 단어의 위치 저장

for cur in msg: 
                                    #find_word[0] == cur이랑 맞는지확인
    if find_word[find_word_index] == cur: #현재 글자가  찾고자 하는 단어의 해당 위치 글자와 일치하는지확인 
        find_word_index += 1 #일치하면 증가 
        if find_word_index == find_word_len: # 글자를 찾았다!!!!
            count_found_word += 1 # 증가
            find_word_index = 0 
            find_word_pos.append(count - find_word_len + 1) #찾아야할 인덱스의 첫번쨰 인덱스번호를 찾아야하기때문에
    else:
        find_word_index = 0 #초기화
        
    if cur == " " or cur == "\n": 
        if prev != " " and prev != "\n":
            count_word += 1
    elif count == len(msg) - 1: # 마지막 글자
        if prev != " " and prev != "\n":
            count_word += 1
            
    if cur != " " and cur != "\n":
        count_char += 1
    
    if cur == "\n":
        count_lines += 1
    
    count += 1
    
    prev = cur # 현재 글자를 이전 글자로 업데이트
    
print(f"총 글자수: {count_char}")        
print(f"총 줄수: {count_lines}") 
print(f"총 단어수: {count_word}")   
print(f"검색된 단어수: {count_found_word}")     
print(f"검색된 단어 위치: {find_word_pos}")  