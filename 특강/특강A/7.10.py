import csv
# read 모드
# encoding='utf-8'은 파일의 인코딩을 utf-8 로지정하여 한글및 기타언어 처리
# with open("grad1.csv", "r", newline='', encoding='utf-8') as f_handler:
#     reader = csv.reader(f_handler)

#     header = next(reader) #next는(줄단위로 불러오고) 현재 포인터의 가르키고  그다음줄을 나타낸다
#     # header = next(reader)
    
#     for i in header:
#         print(i,"\t",end="")
#     print()


#     for row in reader:
#         print(row) 


#writer
# with open("grad1.csv", mode= "w", newline='', encoding='utf-8') as f_handler:
#      writer = csv.writer(f_handler)

#      writer.writerow (['name','age','email']) #한줄
#      writer.writerows([['alice',30,'alice@example.com'], ['bob', 25,'bob@example.com']]) #여러줄

#딕셔너리
# with open("grad1.csv", newline='', encoding='utf-8') as f:
#     reader = csv.DictReader(f)

#     for row in reader:
#         print(f"{row['이름']},{row['총점']},{row['평균']}")

with open("output.csv", mode= "w", newline='', encoding='utf-8') as f:
    fields =['name','age','email']

    writer =csv.DictWriter(f, fieldnames=fields)
    
    writer.writeheader()

    writer.writerow({'name':'alice','age':'30','email':'alice@example.com'})
    writer.writerow({'name':'bob','age':25,'email':'bob@example.com'})

