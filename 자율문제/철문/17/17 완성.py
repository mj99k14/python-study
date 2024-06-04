import random

list_words = []

for index in range(3):
    while True:
        input_value = input("단어를 입력하세요")
        
        if 5 <= len(input_value) <= 20:
            list_words.append(input_value)
            break
        
        print("5이상 20이하 글자의 단어 입력")
            
    

#list_words = ["kkiikk", "aannaaf", "aeekeet"]

word_selected = list(list_words[random.randint(0, 2)])
word_printed = word_selected[:]

print("선택된 단어: ", word_printed)

# 선택된 단어의 글자 수
char_num_word = len(word_selected)

# 선택된 단어의 글자 수의 50%를 블라인드 처리
blind_num_word = char_num_word / 2

# 반올림 처리 알고리즘 // 연산자는 몫만 가지고 온다.
if blind_num_word > char_num_word // 2:
    blind_num_word += 1
    
blind_num_word = int(blind_num_word)
# 랜덤 단어를 문자열로 분리해줌
list_blind_index = [value for value in range(0, char_num_word)]
#글자수에서 블라인드 처리할 숫자뺴고 나머지를 - 해준다
for index in range(0, char_num_word - blind_num_word):
    del list_blind_index[random.randint(0, len(list_blind_index) - 1)]
#복사된 리스트에 블라인드를 처리해줌  
for index in list_blind_index:
    word_printed[index] = "_"

count = 1
while len(list_blind_index) > 0:
    print(word_printed)
    
    input_value = input("글자를 입력하세요: ")
 #잠시 비교를위해 만들어준 리스트
    found_index_list = []
    if input_value in word_selected:
        for index in list_blind_index:
            if word_selected[index] == input_value:
                word_printed[index] = input_value
                found_index_list.append(index)
                
        for f_index in found_index_list:
            list_blind_index.remove(f_index)
        print(f"정답{count} ")
    else:
        print(f"없는 글자얌{count}")
    count += 1
    if input_value ==  word_selected:
        print(f"정답! 이제끝내자!{count}")
        break

print(word_printed)



