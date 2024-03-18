import tkinter as tk

def update_label_text():
    label.config(text="안녕하세요, " + entry.get())

# Tkinter 윈도우 생성
root = tk.Tk()
root.title("동적 화면 예제")

# 레이블 생성
label = tk.Label(root, text="이름을 입력하세요:")
label.pack(pady=10)

# 엔트리(텍스트 입력 상자) 생성
entry = tk.Entry(root)
entry.pack(pady=10)

# 버튼 생성
button = tk.Button(root, text="인사하기", command=update_label_text)
button.pack(pady=10)

# 윈도우 실행
root.mainloop()