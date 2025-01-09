import ctypes
import pygetwindow as gw

# 윈도우 스타일 설정 상수
GWL_EXSTYLE = -20
WS_EX_TOOLWINDOW = 0x00000080
WS_EX_APPWINDOW = 0x00040000

def hide_from_alt_tab(window_title):
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

    # WS_EX_APPWINDOW 제거, WS_EX_TOOLWINDOW 추가 (Alt+Tab에서 숨김)
    new_style = style & ~WS_EX_APPWINDOW | WS_EX_TOOLWINDOW
    ctypes.windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE, new_style)

    print(f"Window '{window_title}' is now hidden from Alt+Tab.")

if __name__ == "__main__":
    window_title = "새 탭"  # 원하는 창 제목으로 변경 (예: Google Chrome, 특정 앱 등)
    hide_from_alt_tab(window_title)
