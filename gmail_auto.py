from selenium import webdriver # 크롬 드라이버 관련
from selenium.webdriver.chrome.service import Service  # 크롬 드라이버 관련
from webdriver_manager.chrome import ChromeDriverManager  # 크롬 드라이버 관련

from tkinter import * # GUI 모듈
import tkinter.ttk as ttk #combo box 예제를 위해 필요
import tkinter.messagebox as msbox # messagebox 예제를 위해 필요

import time

root = Tk()
root.title("전자(세금)계산서 합계표 조회") # 타이틀 제목
root.geometry("640x700+100+100") # 가로 * 세로 + x좌표 + y좌표

root.resizable(False, False) # 창 크기 값 변경 불가

# button 예제
def run_cmd():
    print("버튼이 클릭되었습니다.")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    url = 'https://www.hometax.go.kr/websquare/websquare.wq?w2xPath=/ui/pp/index_pp.xml'
    driver.get(url)
    driver.maximize_window()
    time.sleep(5)

    try:
        #세무대리 납세관리 버튼 클릭
        btn1_button = driver.find_element("css selector", "#hdTxt548")
        btn1_button.click()
        time.sleep(5)

        
        

    except Exception as e:
        print(f"예외 발생: {e}")

    driver.quit()

#frame 예제

Label(root, text="메뉴를 선택해주세요").pack(side="top")
btn_run = Button(root, text="실행", command=run_cmd).pack(side="bottom")

frame_drink = LabelFrame(root, text="음료")
frame_drink.pack(side="right", fill="both", expand=True)
Button(frame_drink, text="콜라").pack()
Button(frame_drink, text="사이다").pack()


root.mainloop()


