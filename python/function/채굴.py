import pyautogui
import time

MESSAGE = "!mine"
INTERVAL = 25  # 메시지 전송 간격 (초)

time.sleep(5)  # 5초 동안 대기 후 시작 (디스코드 창으로 이동할 시간 확보)

while True:
    pyautogui.write(MESSAGE)  # 메시지 입력
    pyautogui.press("enter")  # 엔터키 눌러 전송
    time.sleep(INTERVAL)  # 지정한 시간 간격 대기
