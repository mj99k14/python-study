# model = input("자동차 모델 입력 구다사이: ")
# maker = ""
# if model == "m3" or model == "m5" or model == "m7":
#     maker  = "bmw" 
# elif model == "Y" or model == "X":
#     maker = "tesla"
# elif model == "ES" or model == "LS":
#     maker ="Lexus"
# elif model == "G80" or model == "G90":
#     maker ="hyundai"
# else:
#     maker = "아이돈노"
    
# print(maker)



# model = input("자동차 모델 입력 구다사이: ")
# bmw =["m1","m2","m3","m4"]
# tesla = ["Y","X"]
# lexus = ["ES","LS"]
# genesis = ["G80","G90"] 

# if model in bmw:
#     msg ="bmw"
# elif model in tesla:
#     msg ="tesla"
# elif model in lexus:
#     msg ="lexus"
# elif model in genesis:
#     msg ="genesis"
# else:
#     msg ="나는 모름"

# print(msg)
    
        
# in  써서      
# model = input("자동차 모델 입력 구다사이: ")
# bmw =["m1","m2","m3","m4"]
# tesla = ["Y","X"]
# lexus = ["ES","LS"]
# genesis = ["G80","G90"] 

# if model in bmw:
#     msg ="bmw"
# elif model in tesla:
#     msg ="tesla"
# elif model in lexus:
#     msg ="lexus"
# elif model in genesis:
#     msg ="genesis"
# else:
#     msg ="나는 모름"

# print(msg)
    

#IN
# model = input("자동차 모델 입력 구다사이: ")
# msg =""
# bmw =["m1","m2","m3","m4"]
# tesla = ["Y","X"]
# lexus = ["ES","LS"]
# genesis = ["G80","G90"]
# for i in bmw:
#     if i == model:
#         msg = "bmw"
#         break

# for i in tesla:
#     if i == model:
#         msg = "tesla"
#         break
# for i in lexus:
#     if i == model:
#         msg = "lexus"
#         break

# for i in genesis:
#     if i == model:
#         msg = "genesis"
#         break
# msg = msg if msg != "" else "아님"
       
model = input("자동차 모델 입력 구다사이: ")
msg ="알수없음"
bmw =["m1","m2","m3","m4"]
tesla = ["Y","X"]
lexus = ["ES","LS"]
genesis = ["G80","G90"]
for i in bmw:
    if i == model:
        msg = "bmw"
        break
    
if model =="":
    for i in tesla:
        if i == model:
            msg = "tesla"
            break
        
if model =="":
    for i in lexus:
        if i == model:
            msg = "lexus"
            break
        
if model =="":
    for i in genesis:
        if i == model:
            msg = "genesis"
            break
print(msg)
    




# text = ["a",'b',"c","d"]

# print("a" in text)#true
# print("c" in text)
# print("d" in text)
# print("e" in text)#false
# #좌항에 있는 값이 우항에있습니까?

#in 없이만들기

