# words = input()
# l = len(words)
# s = [0 for s in range(l)]
# # m = max(words)
# for c in words:
#     s[c] += 1
# print(s)

words = input()
words_list = []
w_s = set(words)
for s in w_s:
    words_list.append(s)