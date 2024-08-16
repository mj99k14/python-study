import random
#단어 3개 입력받아 리스트
# word_list = [input("단어를 입력하세요:") for i in range(3)]
word_list = ["hello", "hello" ,"hello"]
print(word_list)
#글자 3이상 20이하
#3개중하나 임의 
random_word = [random.choice(word_list)]
print(random_word)
#같은리스트하나만듬
same_list = list(random_word)[:]
print(same_list)
#블라인드 해줄숫자 구함
word = len(random_word)
word_half = word  / 2
if word_half > word // 2:
    word_half += 1
word_half = int(word_half)

#비교할 숫자 구함

#사용자로부터 하나 입력받음
#블라인드 비교 하기
#블라인드 추가 
#입력한게 같으면  블라인드 해제