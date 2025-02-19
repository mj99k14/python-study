import json

bar = {"name":"kimmimjung", "age":100, "phone":239403}



# print(bar.items())

# for key,value in bar.items():
#     print(f"key:{key}, value :{value}")


#     #key값이 value의값을 가지고있는 매타데이터
# print((bar['name']))

# del bar['name']

# print(bar)


#네트워크로 전송 -> 문자열 (text) -> JSON
#bar는 메모리 존재하는 데이터 ->JSON Serializer
#->JSON 기반 TEXT

#with open("text.txt",'w') as file_handler:


#serializing
json_str = json.dumps(bar)
print(type(json_str),json_str)

#parsing
rcvd_data = json.loads(json_str)


print(rcvd_data.get('phone'))
#psrsing을하고난뒤iteam이있는지확인 ->get은 없으면 none이나온다

print(type(rcvd_data['age']), type(rcvd_data['phone']))