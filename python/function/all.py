import ctypes
import pygetwindow as gw

# 윈도우 스타일과 속성 정의
WS_EX_LAYERED = 0x00080000
GWL_EXSTYLE = -20
LWA_ALPHA = 0x00000002
WS_EX_TOOLWINDOW = 0x00000080
WS_EX_APPWINDOW = 0x00040000

# 투명도 설정 함수
def set_window_transparency(window_title, transparency):
    hwnd = None
    for w in gw.getWindowsWithTitle(window_title):
        if window_title in w.title:
            hwnd = w._hWnd
            break
    if not hwnd:
        print(f"Window with title '{window_title}' not found.")
        return
    extended_style = ctypes.windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
    ctypes.windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE, extended_style | WS_EX_LAYERED)
    ctypes.windll.user32.SetLayeredWindowAttributes(hwnd, 0, transparency, LWA_ALPHA)
    print(f"Transparency set to {transparency} for window '{window_title}'.")

# Alt + Tab 숨기기 함수
def hide_from_alt_tab(window_title):
    hwnd = None
    for w in gw.getWindowsWithTitle(window_title):
        if window_title in w.title:
            hwnd = w._hWnd
            break
    if not hwnd:
        print(f"Window with title '{window_title}' not found.")
        return
    style = ctypes.windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
    new_style = style & ~WS_EX_APPWINDOW | WS_EX_TOOLWINDOW
    ctypes.windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE, new_style)
    print(f"Window '{window_title}' is now hidden from Alt+Tab.")

# Alt + Tab에 다시 표시 함수
def show_in_alt_tab(window_title):
    hwnd = None
    for w in gw.getWindowsWithTitle(window_title):
        if window_title in w.title:
            hwnd = w._hWnd
            break
    if not hwnd:
        print(f"Window with title '{window_title}' not found.")
        return
    style = ctypes.windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
    new_style = style & ~WS_EX_TOOLWINDOW | WS_EX_APPWINDOW
    ctypes.windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE, new_style)
    print(f"Window '{window_title}' is now visible in Alt+Tab.")

# 메인 실행부
if __name__ == "__main__":
    while True:
        print("\n=== 창 관리 프로그램 ===")
        print("1. 창 투명도 설정")
        print("2. Alt + Tab에서 숨기기")
        print("3. Alt + Tab에 다시 표시")
        print("4. 종료")
        choice = input("원하는 기능의 번호를 선택하세요: ")

        if choice == "1":
            window_title = input("창 제목을 입력하세요: ")
            transparency = int(input("투명도를 입력하세요 (0 = 완전 투명, 255 = 불투명): "))
            set_window_transparency(window_title, transparency)
        elif choice == "2":
            window_title = input("창 제목을 입력하세요: ")
            hide_from_alt_tab(window_title)
        elif choice == "3":
            window_title = input("창 제목을 입력하세요: ")
            show_in_alt_tab(window_title)
        elif choice == "4":
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 선택입니다. 다시 입력해 주세요.")
