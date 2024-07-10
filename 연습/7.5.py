
#내가원하는 숫자를 받고 리스트안에  ->3줄

count = int(input("Enter the number of elements"))
user = [int(input(f"Enter value{i+1}")) for i in range(count)]
print(user)
user1 = [[user] for i in range(3)]
print(user1)

for i in user1:
    for s in i:
        print(s,end=" ")
    print()


    #23,34
    #23,34
    #23,34
    