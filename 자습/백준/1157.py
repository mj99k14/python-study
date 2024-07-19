# n = input()
# s =n.upper()
# ap=set(s)
# ap_list = []
# for i in s:
#     if s[i]== s[i+1]:




N = int(input())
group_word = N

for i in range(N) :
    word = input()
    for j in range(len(word)-1) :
        if word[j] == word[j+1] :
            continue
        elif word[j] in word[j+1:] :
            group_word -= 1
            break
print(group_word)
