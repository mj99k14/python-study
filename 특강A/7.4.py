import os #operating system

#현재 working directory
os.getcwd()
print()
f_handlder = open("../../test.txt",)
print(os.getcwd())


#오픈한다
f_handlder = open()

#읽는다
msg = f_handlder.read()

print(msg)

#닫는다
f_handlder.close()