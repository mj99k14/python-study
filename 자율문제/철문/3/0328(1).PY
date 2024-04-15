#  프로그램은사용자에게다음정보를입력받습니다:
#  • 사용자의나이(age)
#  • 사용자가예약하려는이벤트코드(event_code) - 이벤트코드는'E1', 'E2', 'E3' 중 하나입니다.
#  • 사용자가예약을원하는날짜(reservation_date) - 예약 날짜는 1부터 30까지의 숫자로 입력됩니다.
#  2. 각이벤트코드별로다음과같은규칙이적용됩니다:
#  • 'E1': 만 18세 이상만 예약가능합니다.
#  • 'E2': 모든 연령대가예약가능하지만, 날짜는짝수일에만예약할수있습니다.
#  • 'E3': 만 16세 이상만 예약할수있으며, 7의배수인날짜에만예약가능합니다.
#  3. 사용자는각이벤트코드에따라예약을시도할때다음과같은결과를받게됩니다:
#  • 예약성공: "예약이완료되었습니다!"
#  • 나이미달: "나이제한으로인해예약할수없습니다."
#  • 날짜제한: "선택하신날짜에는예약할수없습니다."
#  • 잘못된입력: "잘못된입력입니다. 프로그램을종료합니다

age=int(input("나이를 입력하세요:"))
event_code=input("예약하려는 이벤트 코드를 입력하세요:")
reservation_date=int(input("원하는 예약 날짜를 입력하세요:"))
if  event_code not in ["E1","E2","E3"] or not (1<= reservation_date <=30):
    print("잘못된 입력입니다.프로그램을 종료합니다.")
else:
    if event_code == "E1":
       if age>=18:
        print("예약이 완료되었습니다!")
       elif age<18:
        print("나이 제한으로 인해 예약할 수 없습니다.")
    if event_code=="E2": 
       if reservation_date %2==0 and 1<=reservation_date<=30:
        print("예약이 완료되었습니다.")
       elif reservation_date %2!=0 and 1<=reservation_date>=30:
        print("선택하신 날짜에는 예약할 수 없습니다.")
    if event_code=="E3":
        if age>=16 and reservation_date %7==0:
            print("예약이 완료되었습니다!")
        elif reservation_date %7!=0:
            print("나이 제한으로 인해 예약할수 없습니다.")
    


















# age=int(input("나이를 입력하세요:"))
# event_code=input("예약하려는 이벤트 코드를 입력하세요:")
# reservation_date=int(input("원하는 예약 날짜를 입력하세요:"))
# if  event_code not in ["E1,E2,E3"] or (1<= reservation_date >=30):
#     print("잘못된입력입니다.")
# else:
#     if age>=18:
#         print("E1")
#         print("예약을 완료되었습니다!")
#     else:
#         print("나이 제한으로 인해 예약할 수 없습니다.")
#     elif reservation_date % 2==0 and reservation_date % 1 !=0:
#         print("E2")
#         print("예약을 완료되었습니다!")
#     else:
#         print("선택하신 날짜에는 예약할 수 없습니다.")
#     elif age<=16 and reservation_date % 7== 0 and age>16 and reservation_date % 7!=0:     
#         print("E3")
#         print("예약을 완료했습니다!")
#     else:
#         print("선택하신 날짜에는 예약할수없습니다.")




# if age>=18:
#         print("E1")
#         print("예약을 완료되었습니다!")
#     else:
#         print("나이 제한으로 인해 예약할 수 없습니다. ")
    
# if reservation_date % 2==0 and reservation_date % 1 !=0:
#         print("E2")
#         print("예약을 완료되었습니다!")
#     else:
#         print("선택하신 날짜에는 예약할 수 없습니다.")
        
    
# if age<=16 and reservation_date % 7== 0 and age>16 and reservation_date % 7!=0:     
#         print("E3")
#         print("예약을 완료했습니다!")
#     else:
#         print("선택하신 날짜에는 예약할수없습니다.")

# else:
#     print("잘못된 입력입니다. 프로그램을 종료합니다.")    

