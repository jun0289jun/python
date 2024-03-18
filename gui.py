import tkinter.ttk as ttk #combo box 예제를 위해 필요
import tkinter.messagebox as msbox # messagebox 예제를 위해 필요
from tkinter import *
import time

root = Tk()
root.title("전자(세금)계산서 합계표 조회") # 타이틀 제목
#root.geometry("640x480") # 가로 * 세로
root.geometry("640x1024+100+100") # 가로 * 세로 + x좌표 + y좌표

#root.resizable(False, False) # 창 크기 값 변경 불가


# button 예제
# btn1 = Button(root, text = "버튼1") # 버튼 선언
# btn1.pack() #버튼 출력

# btn2 = Button(root, padx = 5, pady = 10, text = "버튼2") # 버튼 선언(x y 값으로 패딩값 지정)
# btn2.pack() #버튼 출력

# btn3 = Button(root, padx = 10, pady = 5, text = "버튼3") # 버튼 선언(x y 값으로 패딩값 지정)
# btn3.pack() #버튼 출력

# btn4 = Button(root, width = 10 , height = 3, text = "버튼4") # 버튼 선언(버튼 크기 자체를 선언(글자수와 무관))
# btn4.pack() #버튼 출력

# btn5 = Button(root, fg="red" , bg = "yellow", text = "버튼5") # 버튼 선언(fg는 글자색, bg는 배경색)
# btn5.pack() #버튼 출력


# photo = PhotoImage(file="C:/RPA/btn6.gif") # 이미지 호출
# btn6 = Button(root, image=photo) # 버튼 선언 (이미지 사용)
# btn6.pack()

# def btncmd():
#     print("버튼이 클릭되었습니다.")

# btn7 = Button(root, text = "동작하는 버튼7", command=btncmd) # 버튼 선언
# btn7.pack() #버튼 출력




# label 예제

# label1 = Label(root, text="안녕하세요")
# label1.pack()

# or_photo = PhotoImage(file="C:/RPA/btn6.gif") # 이미지 호출
# label2 = Label(root, image=or_photo) # 레이블 선언 (이미지 사용)
# label2.pack()

# def change():
#     label1.config(text="눌렀네요")

#     global ch_photo # photo2가 가비지콜랙터를 통해 삭제되는것을 방지하기 위해 전역변수로 선언
#     ch_photo = PhotoImage(file="C:/RPA/change.gif") # 이미지 호출
#     label2.config(image=ch_photo)

# btn = Button(root, text="클릭", command=change)
# btn.pack()



#text box 예제

# txt = Text(root, width=30, height=5) #개행 가능
# txt.pack()

# txt.insert(END, "글자를 입력하세요") #기본값 입력

# e = Entry(root, width=30) # 개행 불가능
# e.pack()

# e.insert(0, "한줄만 가능합니다")


# def btn_ch_cmd():
#     # 콘솔에 내용 출력
#     print(txt.get("1.0", END)) #텍스트로부터 값을 가져오는 구문. 1은 첫번째 행부터 0번째 열(컬럼)의 인덱스 부터 가져와라
#     print(e.get())  #엔트리는 한줄만 입력하므로 상대적으로 간단

#     #내용 삭제
#     txt.delete("1.0", END)
#     e.delete(0, END)

# btn_ch_txt = Button(root, text="글자 가져오기", command=btn_ch_cmd)
# btn_ch_txt.pack()



# select box 예제(중복 선택 가능)
# listbox = Listbox(root, selectmode="extended", height=0) # 0인 경우 모든 리스트 출력 그 외 숫자는 해당 개수만큼 리스트 출력
# listbox.insert(0, "사과")
# listbox.insert(1, "딸기")
# listbox.insert(2, "바나나")
# listbox.insert(END, "수박") # 하나하나 인덱스 관리가 번거로우니 END 사용
# listbox.insert(END, "포도") # 하나하나 인덱스 관리가 번거로우니 END 사용
# listbox.pack()

# def btn_function_cmd():
#     #삭제
#     #listbox.delete(END) # 맨 뒤의 리스트 삭제 0인경우 맨 앞 인덱스가 삭제됨

#     #갯수확인
#     #print("리스트에는", listbox.size(), "개가 있습니다")

#     #항목확인
#     #print("1번째부터 3번째까지의 항목 : ", listbox.get(0, 2))

#     #선택된 항목 확인(index)
#     print("선택한 항목 : ", listbox.curselection())

# btn_function = Button(root, text="기능 실행", command=btn_function_cmd)
# btn_function.pack()


#check box 예제

# chkvar = IntVar() #chkvar에 int형으로 값을 저장
# chkbox = Checkbutton(root, text="오늘 하루 보지 않기", variable=chkvar)
# #chkbox.select() # 자동 선택
# #chkbox.deselect() # 선택 해제
# chkbox.pack()

# chkvar2 = IntVar() #chkvar에 int형으로 값을 저장
# chkbox2 = Checkbutton(root, text="일주일동안 보지 않기", variable=chkvar2)
# chkbox2.pack()

# def btn_function2_cmd():
#     print(chkvar.get()) # 0 : 체크해제, 1 : 체크
#     print(chkvar2.get()) # 0 : 체크해제, 1 : 체크

# btn_function2 = Button(root, text="기능2 실행", command=btn_function2_cmd)
# btn_function2.pack()


#radio box 예제

# label3 = Label(root, text="메뉴를 선택하세요")
# label3.pack()

# burger_var = IntVar() # 여기에 선택된 메뉴 번호를 int형으로 값을 저장
# btn_burger1 = Radiobutton(root, text="햄버거", value=1, variable=burger_var)
# btn_burger1.select()
# btn_burger2 = Radiobutton(root, text="치즈버거", value=2, variable=burger_var)
# btn_burger3 = Radiobutton(root, text="치킨버거", value=3, variable=burger_var)

# btn_burger1.pack()
# btn_burger2.pack()
# btn_burger3.pack()



# label4 = Label(root, text="음료를 선택하세요")
# label4.pack()

# drink_var = StringVar() # 여기에 선택된 음료 명을 string형으로 값을 저장
# btn_drink1 = Radiobutton(root, text="콜라", value="콜라", variable=drink_var)
# btn_drink1.select()
# btn_drink2 = Radiobutton(root, text="사이다", value="사이다", variable=drink_var)
# btn_drink3 = Radiobutton(root, text="환타", value="환타", variable=drink_var)

# btn_drink1.pack()
# btn_drink2.pack()
# btn_drink3.pack()


# def btn_function3_cmd():
#     print(burger_var.get()) # 값 출력
#     print(drink_var.get()) # 값 출력

# btn_function3 = Button(root, text="기능3 실행", command=btn_function3_cmd)
# btn_function3.pack()





#combo box 예제

# label5 = Label(root, text="메뉴를 선택하세요")
# label5.pack()

# values = [str(i) + "일" for i in range(1, 32)] # 1 ~ 31 까지의 숫자
# combobox = ttk.Combobox(root, height=5, values=values)
# combobox.pack()
# combobox.set("카드 결제일") #최초 목록의 제목 설정

# readonly_combobox = ttk.Combobox(root, height=10, values=values, state="readonly")
# readonly_combobox.current(0) # 0번째 인덱스 값을 강제하여 사용자 임의의 작성 방지
# readonly_combobox.pack()
# readonly_combobox.set("카드 결제일") #최초 목록의 제목 설정



# def btn_function4_cmd():
#     print(combobox.get()) # 값 출력
#     print(readonly_combobox.get()) # 값 출력

# btn_function4 = Button(root, text="기능4 실행", command=btn_function4_cmd)
# btn_function4.pack()




#progress bar 예제

# #label6 = Label(root, text="로딩중입니다")
# #label6.pack()

# # #progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate")
# # progressbar = ttk.Progressbar(root, maximum=100, mode="determinate")
# # progressbar.start(10) #10ms마다 움직임
# # progressbar.pack()

# # def btn_function4_cmd():
# #     progressbar.stop() # 중지

# # btn_function4 = Button(root, text="기능4 실행", command=btn_function4_cmd) 
# # btn_function4.pack()

# p_var2 = DoubleVar() # 실수를 반영하기 위해
# progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
# progressbar2.pack()

# def btn_function5_cmd():
#     for i in range(101): # 1 ~ 100
#         time.sleep(0.01) #0.01초 대기

#         p_var2.set(i) # progress bar의 실제 값을 설정
#         progressbar2.update() #for문에 진행에 따라 GUI가 업데이트 됨
#         print(p_var2.get()) # 

# btn_function5 = Button(root, text="기능5 실행", command=btn_function5_cmd) 
# btn_function5.pack()



#menu bar 예제

    # def create_new_file():
    #     print("새파일을 만듭니다.")

    # menu = Menu(root)

    # #File 메뉴
    # menu_file = Menu(menu, tearoff=0)
    # menu_file.add_command(label="New File", command=create_new_file)
    # menu_file.add_command(label="New Window")
    # menu_file.add_separator()
    # menu_file.add_command(label="Open File...")
    # menu_file.add_separator()
    # menu_file.add_command(label="Save All", state="disable") # 비활성화
    # menu_file.add_separator()
    # menu_file.add_command(label="Exit", command=root.quit)
    # menu.add_cascade(label="File", menu=menu_file)

    # #Edit 메뉴(빈 값)
    # menu.add_cascade(label="Edit")

    # #Language 메뉴 추가 (radio 버튼을 통해서 택1)
    # menu_lang = Menu(menu, tearoff=0)
    # menu_lang.add_radiobutton(label="Python")
    # menu_lang.add_radiobutton(label="Java")
    # menu_lang.add_radiobutton(label="C++")
    # menu.add_cascade(label="Language", menu=menu_lang)

    # # View 메뉴 (check 버튼을 통해서 체크 및 체크해제)
    # menu_view = Menu(menu, tearoff=0)
    # menu_view.add_checkbutton(label="Show Minimap")
    # menu.add_cascade(label="View", menu=menu_view)

    # root.config(menu=menu)

    # def info():
    #     msbox.showinfo("알림", "정상적으로 예매완료")

    # def warn():
    #     msbox.showwarning("경고", "매진되었습니다")

    # def error():
    #     msbox.showerror("에러", "결제오류가 발생했습니다")

    # def okcancel():
    #     msbox.askokcancel("확인/취소", "해당좌석은 유아동반석입니다. 예매하시겠습니까?")

    # def retrycancel():
    #     msbox.askretrycancel("재시도/취소", "일시적 오류입니다. 다시 예매하시겠습니까?")

    # def yesno():
    #     msbox.askyesno("예 / 아니오", "해당 좌석은 역방향입니다. 예매하시겠습니까?")

    # def yesnocancel():
    #     response = msbox.askyesnocancel(tilte=None, message="예매 내역이 저장되지 않았습니다. \n 저장하시겠습니까?")
    #     # print("응답 : ", response)
    #     print("응답 : ")
    #     if response == 1: #예, True
    #         print("예")
    #     elif response == 0: #아니오, False
    #         print("아니오")
    #     else:
    #         print("취소") #취소, None

    # Button(root, command=info, text="알림").pack()
    # Button(root, command=warn, text="경고").pack()
    # Button(root, command=error, text="에러").pack()

    # Button(root, command=okcancel, text="확인 취소").pack()
    # Button(root, command=retrycancel, text="재시도 취소").pack()
    # Button(root, command=yesno, text="예 아니오").pack()
    # Button(root, command=yesnocancel, text="예 아니오 취소").pack()


#frame 예제

# Label(root, text="메뉴를 선택해주세요").pack(side="top")
# Button(root, text="주문하기").pack(side="bottom")

# frame_burger = Frame(root, relief="solid", bd=1)
# frame_burger.pack(side="left", fill="both", expand=True)

# Button(frame_burger, text="햄버거").pack()
# Button(frame_burger, text="치즈버거").pack()
# Button(frame_burger, text="치킨버거").pack()

# frame_drink = LabelFrame(root, text="음료")
# frame_drink.pack(side="right", fill="both", expand=True)
# Button(frame_drink, text="콜라").pack()
# Button(frame_drink, text="사이다").pack()


#scrollbar 예제

# frame = Frame(root)
# frame.pack()

# scrollbar = Scrollbar(frame)
# scrollbar.pack(side="right", fill="y") # fill은 스크롤바 크기

# listbox = Listbox(frame, selectmode="extended", height=10, yscrollcommand = scrollbar.set) # listbox는 yscrollcommand로 scrollbar를 바라보고
# for i in range(1, 32):
#     listbox.insert(END, str(i) + "일")
# listbox.pack(side="left")

# scrollbar.config(command=listbox.yview) # scrollbar는 config(command=listbox.yview)로  listbox를 매핑하여 바라보게 해야 서로 영향을 준다

#grid 예제

# ┌───┬───┬───┐
# │0,0│0,1│0,2│
# ├───┼───┼───┤
# │1,0│1,1│1,2│
# ├───┼───┼───┤
# │2,0│2,1│2,2│
# └───┴───┴───┘

# # 버튼 생성
# btn1 = Button(root, text="버튼1")
# btn2 = Button(root, text="버튼2")

# # 그리드에 버튼 배치
# btn1.grid(row=0, column=0)
# btn2.grid(row=1, column=1)

#계산기 레이어 예제 첫줄(width=5, height=2는 내용길이에 따라 키보드의 크기가 조금씩 다르기때문에 width=5, height=2로 바꿔본다 그러면 키보드 크기가 고정되는것을 볼수 있다.)
btn_f16 = Button(root, text="F16", width=5, height=2)
btn_f17 = Button(root, text="F17", width=5, height=2)
btn_f18 = Button(root, text="F18", width=5, height=2)
btn_f19 = Button(root, text="F19", width=5, height=2)

btn_f16.grid(row=0, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_f17.grid(row=0, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_f18.grid(row=0, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_f19.grid(row=0, column=3, sticky=N+E+W+S, padx=3, pady=3)

#계산기 레이어 예제 둣째줄
btn_clear = Button(root, text="clear", width=5, height=2)
btn_equar = Button(root, text="=", width=5, height=2)
btn_div = Button(root, text="/", width=5, height=2)
btn_mul = Button(root, text="*", width=5, height=2)

btn_clear.grid(row=1, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_equar.grid(row=1, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_div.grid(row=1, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_mul.grid(row=1, column=3, sticky=N+E+W+S, padx=3, pady=3)

#계산기 레이어 예제 셋째줄
btn_7 = Button(root, text="7", width=5, height=2)
btn_8 = Button(root, text="8", width=5, height=2)
btn_9 = Button(root, text="9", width=5, height=2)
btn_sub = Button(root, text="-", width=5, height=2)

btn_7.grid(row=2, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_8.grid(row=2, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_9.grid(row=2, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_sub.grid(row=2, column=3, sticky=N+E+W+S, padx=3, pady=3)

#계산기 레이어 예제 넷째줄
btn_4 = Button(root, text="4", width=5, height=2)
btn_5 = Button(root, text="5", width=5, height=2)
btn_6 = Button(root, text="6", width=5, height=2)
btn_add = Button(root, text="+", width=5, height=2)

btn_4.grid(row=3, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_5.grid(row=3, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_6.grid(row=3, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_add.grid(row=3, column=3, sticky=N+E+W+S, padx=3, pady=3)

#계산기 레이어 예제 넷째줄
btn_1 = Button(root, text="1", width=5, height=2)
btn_2 = Button(root, text="2", width=5, height=2)
btn_3 = Button(root, text="3", width=5, height=2)
btn_enter = Button(root, text="enter", width=5, height=2)

btn_1.grid(row=4, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_2.grid(row=4, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_3.grid(row=4, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_enter.grid(row=4, column=3, rowspan=2, sticky=N+E+W+S, padx=3, pady=3)

#계산기 레이어 예제 다섯째줄
btn_0 = Button(root, text="0", width=5, height=2)
btn_point = Button(root, text=".", width=5, height=2)

btn_0.grid(row=5, column=0, columnspan=2, sticky=N+E+W+S, padx=3, pady=3)
btn_point.grid(row=5, column=2, sticky=N+E+W+S, padx=3, pady=3)


root.mainloop()
