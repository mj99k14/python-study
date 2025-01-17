
def attendance_score(hours_per_week, absence_hours, tardy_count):
    okay = hours_per_week * 15
    if(absence_hours > (okay * 0.25)):
        score = "F (학점 미부여)"
        return score
    else:
        absence_hours = int(tardy_count/3) + absence_hours
        score = 20 - (20 * absence_hours /okay)
        return f"{score:.2f}"


hours_per_week = int(input("주당 수업 시간을 입력하세요: "))
absence_hours = int(input("결석한 총 시간을 입력하세요: "))
tardy_count = int(input("지각 횟수를 입력하세요: "))

score = attendance_score(hours_per_week, absence_hours, tardy_count)

print(f"당신의 출석 점수는 {score}점입니다.")



# 함수 정의 점수 내는 식
def score(week, hours, count):
    n = count // 3 # 지각 처리 식
    score = 20 - ((20 * (hours + n)) /( week * 15)) # 점수 구하는 식
    return score 
# 조건에 맞는 값 입력
week = float(input("주당 수업시간을 입력하세요: "))
hours = float(input("결석한 총 시간을 입력하세요: "))
count = float(input("지각 횟수를 입력하세요: "))

if hours * 4 > week * 15 : # 만약 결석 시수가 총수업시수에 1/4을 초과할 경우
    print("당신의 출석 점수는 F (학점 미부여)점입니다.")

elif score(week, hours, count): 
    print("당신의 출석 점수는",format(score(week, hours, count),".2f"),"점입니다.")