from tkinter import *

root = Tk()
root.title("전자(세금)계산서 합계표 조회") # 타이틀 제목
#root.geometry("640x480") # 가로 * 세로
root.geometry("640x480+100+300") # 가로 * 세로 + x좌표 + y좌표

#root.resizable(False, False) # 창 크기 값 변경 불가

label1 = Label(root, text="안녕하세요")
label1.pack()

photo = PhotoImage(file="C:/RPA/btn6.gif") # 이미지 호출
label2 = Label(root, image=photo) # 레이블 선언 (이미지 사용)
label2.pack()

def change():
    label1.config(text="눌렀네요")

    global photo2 # photo2가 가비지콜랙터를 통해 삭제되는것을 방지하기 위해 전역변수로 선언
    photo2 = PhotoImage(file="C:/RPA/change.gif") # 이미지 호출
    label2.config(image=photo2)

btn = Button(root, text="클릭", command=change)
btn.pack()


root.mainloop()
