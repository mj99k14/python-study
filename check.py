import os
print("Current working directory:", os.getcwd())  # 현재 작업 디렉토리를 출력
os.chdir("C:/Users/USER/Desktop/pythonmj/")  # 작업 디렉토리를 mp3 파일이 있는 곳으로 변경
print("Changed working directory:", os.getcwd())
