from tkinter import * # GUI 모듈

def update_selection():
    selection_label.config(text="선택된 분류: " + classifi_var.get())
    create_additional_widgets()

def create_additional_widgets():
    # 기존의 추가 위젯 제거
    for widget in additional_widgets:
        widget.destroy()

    # 선택된 분류에 따라 추가 위젯 생성
    if classifi_var.get() == "전자세금계산서":
        date_radio_01 = Radiobutton(root, text="일자별", variable=date_var, value="일자별")
        date_radio_02 = Radiobutton(root, text="월별", variable=date_var, value="월별")
        date_radio_03 = Radiobutton(root, text="분기별", variable=date_var, value="분기별")
        date_radio_01.pack()
        date_radio_02.pack()
        date_radio_03.pack()
        additional_widgets.extend([date_radio_01, date_radio_02, date_radio_03])
    elif classifi_var.get() == "전자계산서":
        date_radio_01 = Radiobutton(root, text="일자별", variable=date_var, value="일자별")
        date_radio_02 = Radiobutton(root, text="월별", variable=date_var, value="월별")
        date_radio_03 = Radiobutton(root, text="분기별", variable=date_var, value="분기별")
        date_radio_04 = Radiobutton(root, text="년도별", variable=date_var, value="년도별")
        date_radio_01.pack()
        date_radio_02.pack()
        date_radio_03.pack()
        date_radio_04.pack()
        additional_widgets.extend([date_radio_01, date_radio_02, date_radio_03, date_radio_04])

# Tkinter 윈도우 생성
root = Tk()
root.title("분류 및 작성일자 선택")

# 라디오 버튼을 위한 변수 설정
classifi_var = StringVar()
date_var = StringVar()

# 분류 선택 라디오 버튼 생성
classifi_radio_01 = Radiobutton(root, text="전자세금계산서", variable=classifi_var, value="전자세금계산서", command=update_selection)
classifi_radio_02 = Radiobutton(root, text="전자계산서", variable=classifi_var, value="전자계산서", command=update_selection)
classifi_radio_01.pack()
classifi_radio_02.pack()

# 선택 정보 표시 레이블
selection_label = Label(root, text="선택된 분류: ")
selection_label.pack()

# 추가적인 위젯들을 저장하는 리스트
additional_widgets = []

# 윈도우 실행
root.mainloop()
