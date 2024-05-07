#소득 금액을 입력받는다
income=float(input("소득 금액을 입력하세요:"))
#소득세 계산 함수



def calculate_tax(income):
    if income <= 10000:              # 첫1만달러의소득(income)에는10%의세율이적용됩니다.
        tax=income*0.1
        return tax
    elif 10000<income<=20000:        # –1만달러를초과하고2만달러이하의소득에대해서는초과금액에15%의세율을적용하고, 
        tax=(income-10000)*0.15+1000 # 첫1만달러의세금인1천달러를더합니다.
        return tax
       
    elif 20000<income:
        tax=(income-20000)*0.2+2500  # – 2만달러를초과하는소득에대해서는초과금액에20%의세율을적용하고, 앞선구간의
        return tax                   # 세금인2천5백달러를더합니다
        
#계산합니다.
print("소득세는" ,calculate_tax(income),"달러입니다.")
