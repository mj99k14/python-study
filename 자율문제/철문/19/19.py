avga, avgb, avgc, avgd, avgf = 0, 0, 0, 0, 0
scores = [92, 85, 34, 76, 58, 90, 61, 70, 45, 99, 82, 67, 50, 77, 89]
# 90 이상: 'A' 등급
a = [i for i in scores if i >= 90]
for a1 in a:
    avga += a1 / len(a)
print(f"A 등급: 평균 점수 = {format(avga,".2f")}\n{len(a)*"*" }({len(a)}명)")
# • 80 이상 90 미만: 'B' 등급
b = [i for i in scores if i >= 80 and i < 90]
for a1 in b:
    avgb += a1 / len(b)
print(f"B 등급: 평균 점수 = {format(avgb,".2f")}\n{len(b)*"*" }({len(b)}명)")
# • 70 이상 80 미만: 'C' 등급
c = [i for i in scores if i >= 70 and i < 80]
for a1 in c:
    avgc += a1 / len(c)
print(f"C 등급: 평균 점수 = {format(avgc,".2f")}\n{len(c)*"*" }({len(c)}명)")
# • 60 이상 70 미만: 'D' 등급
d = [i for i in scores if i >= 60 and i < 70]
for a1 in d:
    avgd += a1 / len(d)
print(f"D 등급: 평균 점수 = {format(avgd,".2f")}\n{len(d)*"*" }({len(d)}명)")
#학생들의 점수 리스트
f = [i for i in scores if i  < 60]
for a1 in f:
    avgf += a1 / len(f)
print(f"F 등급 : 평균 점수 = {format(avgf,".2f")}\n{len(f)*"*" }({len(f)}명)")