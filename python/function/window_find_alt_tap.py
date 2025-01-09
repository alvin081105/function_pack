import ctypes
import pygetwindow as gw

# 윈도우 스타일 설정 상수
GWL_EXSTYLE = -20
WS_EX_TOOLWINDOW = 0x00000080
WS_EX_APPWINDOW = 0x00040000

def show_in_alt_tab(window_title):
    hwnd = None

    # 창 핸들 가져오기
    for w in gw.getWindowsWithTitle(window_title):
        if window_title in w.title:
            hwnd = w._hWnd
            break

    if not hwnd:
        print(f"Window with title '{window_title}' not found.")
        return

    # 현재 창 스타일 가져오기
    style = ctypes.windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)

    # WS_EX_TOOLWINDOW 제거, WS_EX_APPWINDOW 추가   
    new_style = style & ~WS_EX_TOOLWINDOW | WS_EX_APPWINDOW
    ctypes.windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE, new_style)

    print(f"Window '{window_title}' is now visible in Alt+Tab.")

if __name__ == "__main__":
    window_title = "GBSW 4th"  # 원래 숨겼던 창 제목
    show_in_alt_tab(window_title)
