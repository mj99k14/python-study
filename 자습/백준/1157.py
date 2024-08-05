word = input().upper()
s_w = list(set(word))
print(s_w)
word_list =[word.count(i) for i in s_w]

print(word_list)

if word_list.count(max(word_list)) > 1:
    print("?")
else:
    print(max(word))