
N = int(input())
alpha_list = []

for i in range(N):
    t_case = input().split()
    alpha_list.append([t_case[0], t_case[1]])
# print(alpha_list)
for i in range(len(alpha_list)):
    for k in range(len(alpha_list[i][1])):
        print(int(alpha_list[i][0])*alpha_list[i][1][k], end='' )
    print()