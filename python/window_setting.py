import ctypes
import pygetwindow as gw
import time

# 윈도우 스타일과 속성 정의
WS_EX_LAYERED = 0x00080000
GWL_EXSTYLE = -20
LWA_ALPHA = 0x00000002

# 투명도 설정 함수
def set_window_transparency(window_title, transparency):
    hwnd = None

    # 창 핸들 가져오는 부분분
    for w in gw.getWindowsWithTitle(window_title):
        if window_title in w.title:
            hwnd = w._hWnd
            break
    
    if not hwnd:
        print(f"Window with title '{window_title}' not found.")
        return
    
    # 윈도우 확장 스타일
    extended_style = ctypes.windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
    
    # 스타일에 WS_EX_LAYERED 추가
    ctypes.windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE, extended_style | WS_EX_LAYERED)
    
    ctypes.windll.user32.SetLayeredWindowAttributes(hwnd, 0, transparency, LWA_ALPHA)
    print(f"Transparency set to {transparency} for window '{window_title}'.")

if __name__ == "__main__":
    window_title = "새 탭" # 여기에 크롬창에 완전한 제목 입력력
    transparency = 200  # 0 = 완전 투명, 255 = 완전 불투명
    
    # 투명도 설정
    set_window_transparency(window_title, transparency)
    
    # 몇 초간 유지 후 프로그램 종료 근데 어차피 한번 적용하면 창을 다시 닫았다가 열때까지 적용 해제X
    time.sleep(5)
