#사용자로부터출발시간과 도착시간(시와분으로별도입력) 그리고이동거리를입력받습니다. 
#순서 이동거리 출발시간 도착시간 평균속도 속도상태를 나타내야함
departure_time=int(input("출발 시 (시간)을 입력하세요: "))
departure_minute=int(input("출발 시 (분을)을 입력하세요: "))
arrival_time=int(input("도착 시 (시간)을 입력하세요: "))
arrival_minute=int(input("도착 시 (분)을 입력하세요: "))
distance=float(input("이동 거리(km)를  입력하세요: "))

print(f"이동 시간:{distance}")
print(f"출발 시간:{departure_time}시{departure_minute}분")
print(f"도착 시간:{arrival_time}시{arrival_minute}분")

travel=(arrival_time+arrival_minute/60)-(departure_time+departure_minute/60)
avarge=distance/travel   
print(f"평균 속도:{avarge:.2f}km/h")
if distance/travel  <60:
        print("속도 상태: 느림")
elif 60<= distance/travel < 90:
        print("속도 상태: 보통")
else:
        print("속도 상태: 빠름")
    
 
     
