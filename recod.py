import json
import os

# 기록 파일 이름
record_file = "records.json"

# 기록 파일을 로드하는 함수
def load_records():
    if os.path.exists(record_file):
        with open(record_file, "r") as file:
            return json.load(file)
    return []

# 기록을 저장하는 함수
def save_records(records):
    with open(record_file, "w") as file:
        json.dump(records, file)

# 현재 게임의 기록을 추가하고 등수를 계산하는 함수
def add_record(elapsed_time):
    records = load_records()
    records.append(elapsed_time)
    records.sort()  # 시간 순으로 정렬 (작은 값이 높은 등수)
    save_records(records)
    return records.index(elapsed_time) + 1  # 0-based index이므로 1을 더해줌

# 게임 종료 시 등수 계산
if s_rect.collidelist(fall_rect_list) != -1:
    the_end.play()
    pygame.time.wait(2000)  # 2초 동안 대기
    
    # 현재 게임 시간을 등수에 추가
    rank = add_record(elapsed_time)
    print(f"게임 종료! 당신의 등수는 {rank}위입니다.")
    
    running = False

