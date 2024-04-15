#사용자로 부터 수학,과학,영어의 점수를 입력받습니다
math=float(input("수학 점수를 입력하세요:"))
science=float(input("과학 점수를 입력하세요:"))
english=float(input("영어 점수를 입력하세요:"))
#입력받은 점수들을 바탕으로 평균을 계산합니다
average=int(math+science+english)/3
#게산된 평균 점수를 사용하여 학점등급을 결정합니다

#학점등급은평균점수에따라다음과같이할당됩니다:
# • A: 90점 이상
# • B: 80점 이상 90점 미만
# • C: 70점 이상 80점 미만
# • D: 60점 이상 70점 미만
# • F: 60점 미만
if average>=90:
    print("평균 점수는",average,"이고, 학점은 A입니다.")
elif 80<=average<90:
    print("평균 점수는",average,"이고, 학점은 B입니다.")
elif 70<=average<80:
    print("평균 점수는",average,"이고, 학점은 C입니다.")
elif 60<=average<70:
    print("평균 점수는",average,"이고, 학점은 D입니다.")
else:
    print("평균 점수는",average,"이고, 학점은 F입니다.")    