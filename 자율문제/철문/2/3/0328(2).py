
# 계산식:20점- (20 × 결석시간 수/ 총수업시간수)– 총수업시간계산법: 
# 시수/주 × 15– 지각처리규칙: 
# 지각3회는결석1시간으로처리– 결석처리규칙: 
# 결석시수가총수업시수의1/4을초과할경우학점미부여(F처리  
    
    
    
    
    

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


