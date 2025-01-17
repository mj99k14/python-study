import random

# 이름 리스트
a = ["김민정", "권혁일", "귤페리", "김규민", "김다연", "김민석", "김성관", "김민석", 
     "김효찬", "디네쉬", "조원준", "김민규", "박정민", "배영민", "윤성빈", "아야메", 
     "임영은", "사츠키", "이신우", "유키", "키무송식", "하루나", "홍지강"]

# 리스트를 랜덤하게 섞음
random.shuffle(a)

# 4명씩 그룹으로 나눔
groups = [a[i:i + 4] for i in range(0, len(a), 4)]

# 그룹 출력
for idx, group in enumerate(groups):
    print(f"그룹 {idx + 1}: {', '.join(group)}")
