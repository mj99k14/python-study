#"text.txt" 파일을 읽기 및 쓰기 모드"rt"로 열고,
# 파일 객체를 "f_handler"  변수에 할당
#오픈한다
f_handler = open("text.txt","r+")
                #path + file name  #파일오픈 모드

#파일에서 모든 내용을 읽어 문자열로"msg" 변수에 저장
#읽는다
msg = f_handler.read()
msg += "hello world"
f_handler.write(msg)

#닫는다
f_handler.close()