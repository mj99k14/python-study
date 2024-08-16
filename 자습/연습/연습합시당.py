
# 사용자로부터 행과 열의 수를 입력 받아, 해당 크기에 맞는 2차원 리스트를 생성
row = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))

matrix = [[ 0 for _ in range(columns)] for i in range(row)]
# -> 0 은 값을 초기화하게 만들어주기위해 안에 행을 만들어준다음 그만큼 열을 만들어줌
for i in range(row):
    for j in range(columns):
        matrix[i][j] = int(input(f"{[i]}{[j]}:"))

for i in range(matrix): # ->  한줄에 깔끔하게 숫자만 나타내기위해서
    for s in i:
        print(s,end="")
    print()

