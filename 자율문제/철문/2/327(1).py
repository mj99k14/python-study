
def convert_to_square_feet(square_meters):
    feet=square_meters * 10.7639
    return feet
def convert_to_acres(square_meters):
    acres= square_meters / 4046.86
    return acres

square_meters = float(input("토지의 면적을 제곱미터(m²) 단위로 입력하세요:"))
                      
if square_meters <0:
    print("잘못된 입력입니다")
else:
    print(square_meters,"제곱미터는" ,convert_to_square_feet(square_meters)," 평방피트 입니다.")
    print(square_meters,"제곱미터는" ,convert_to_acres(square_meters),"에이커 입니다.")
    
