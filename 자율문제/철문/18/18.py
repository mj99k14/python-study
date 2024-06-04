#학생들의 점수 리스트가 주어졌을 때, 각 점수를 분류하고 분류된 점수들의 평균을
scores = [92, 85, 34, 76, 58, 90, 61, 70, 45, 99]
#90 <= 우수
avg1, avg2, avg3, avg4 = 0,0,0,0
excellent =[ i for i in scores if i  >=90 ]   
for a in excellent:
    avg1+=a
print(excellent,",평균:",avg1 / len(excellent))
# 70 <=   > 90
good = [ i for i in scores if  i >=70 and i <90]
for a in good:
    avg2+=a
print(good,",평균:",avg2 / len(good))
#50 <=  > 70
normal = [ i for i in scores if  i >=50 and i < 70]
for a in normal:
    avg3+=a
print(normal,",평균:",avg3 / len(normal))
# >50
less = [ i for i in scores if i <50]
for a in less:
    avg4+=a
print(less,",평균:",avg4 / len(less))
