import customtkinter as ctk
from tkinter import simpledialog, messagebox
import ctypes
import pygetwindow as gw
import psutil
import threading
import time

# 윈도우 스타일 상수
WS_EX_LAYERED = 0x00080000
GWL_EXSTYLE = -20
LWA_ALPHA = 0x00000002
WS_EX_TOOLWINDOW = 0x00000080
WS_EX_APPWINDOW = 0x00040000

# 리소스 모니터링 스레드 컨트롤
current_monitor_thread = None

# 함수: 투명도 설정
def set_transparency(hwnd, transparency):
    extended_style = ctypes.windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
    ctypes.windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE, extended_style | WS_EX_LAYERED)
    ctypes.windll.user32.SetLayeredWindowAttributes(hwnd, 0, transparency, LWA_ALPHA)

# 함수: Alt+Tab에서 숨기기
def hide_from_alt_tab(hwnd):
    style = ctypes.windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
    new_style = style & ~WS_EX_APPWINDOW | WS_EX_TOOLWINDOW
    ctypes.windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE, new_style)

# 함수: Alt+Tab에 다시 보이게 하기
def show_in_alt_tab(hwnd):
    style = ctypes.windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
    new_style = style & ~WS_EX_TOOLWINDOW | WS_EX_APPWINDOW
    ctypes.windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE, new_style)

# 함수: 리소스 사용량 가져오기
def get_resource_usage(pid):
    try:
        process = psutil.Process(pid)
        return process.cpu_percent(interval=0.1), process.memory_info().rss / (1024 * 1024)
    except:
        return 0, 0

# 리소스 모니터링
def monitor_resources(hwnd, title):
    global current_monitor_thread
    # 기존 스레드가 있다면 종료
    current_monitor_thread = threading.Event()

    def update_resource_usage():
        while not current_monitor_thread.is_set():
            cpu, memory = get_resource_usage(hwnd)
            resource_label.configure(text=f"{title} 리소스 사용량:\nCPU: {cpu:.2f}%\nMemory: {memory:.2f} MB")
            time.sleep(1)

    monitor_thread = threading.Thread(target=update_resource_usage, daemon=True)
    monitor_thread.start()
    current_monitor_thread = monitor_thread

# GUI 기능 함수
def apply_function():
    selected_title = listbox.get()
    if not selected_title:
        messagebox.showerror("오류", "창을 선택하세요.")
        return

    hwnd = None
    for w in gw.getWindowsWithTitle(selected_title):
        hwnd = w._hWnd
        break
    if not hwnd:
        messagebox.showerror("오류", "선택한 창을 찾을 수 없습니다.")
        return

    # 기능 선택
    action = simpledialog.askstring(
        "기능 선택", 
        "원하는 기능을 입력하세요:\n1. 투명도 설정\n2. Alt+Tab 숨기기\n3. 리소스 모니터링\n4. Alt+Tab 다시 보이기"
    )

    if action == "1":
        transparency = simpledialog.askinteger("투명도 설정", "투명도를 입력하세요 (0~255):", minvalue=0, maxvalue=255)
        if transparency is not None:
            set_transparency(hwnd, transparency)
            messagebox.showinfo("완료", f"창 '{selected_title}' 투명도 설정 완료.")
    elif action == "2":
        hide_from_alt_tab(hwnd)
        messagebox.showinfo("완료", f"창 '{selected_title}' Alt+Tab에서 숨김.")
    elif action == "3":
        monitor_resources(hwnd, selected_title)
    elif action == "4":
        show_in_alt_tab(hwnd)
        messagebox.showinfo("완료", f"창 '{selected_title}' Alt+Tab에 다시 보이게 설정됨.")
    else:
        messagebox.showerror("오류", "잘못된 입력입니다.")

# GUI 초기화
ctk.set_appearance_mode("System")  # "Light", "Dark" or "System"
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("창 관리 시스템")
root.geometry("500x600")

# 타이틀
title_label = ctk.CTkLabel(root, text="창 관리 시스템", font=("Helvetica", 24, "bold"))
title_label.pack(pady=20)

# 창 리스트
listbox = ctk.CTkComboBox(root, values=[w.title for w in gw.getAllWindows() if w.title], font=("Helvetica", 14))
listbox.pack(pady=20, padx=20)

# 버튼
apply_button = ctk.CTkButton(root, text="기능 적용", command=apply_function, font=("Helvetica", 16))
apply_button.pack(pady=20)

# 리소스 모니터링 라벨
resource_label = ctk.CTkLabel(root, text="리소스 모니터링 정보", font=("Helvetica", 14))
resource_label.pack(pady=20)

# 실행
root.mainloop()
