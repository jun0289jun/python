from selenium import webdriver # 크롬 드라이버 관련
from selenium.webdriver.chrome.service import Service  # 크롬 드라이버 관련
from webdriver_manager.chrome import ChromeDriverManager  # 크롬 드라이버 관련

from selenium.webdriver.common.keys import Keys #키 입력을 위해 필요

from selenium.webdriver.common.alert import Alert # 알럿 처리를 위해 필요

from tkinter import * # GUI 모듈
import tkinter.ttk as ttk #combo box 예제를 위해 필요
import tkinter.messagebox as msbox # messagebox 예제를 위해 필요

import time

root = Tk()
root.title("전자(세금)계산서 합계표 조회") # 타이틀 제목
root.geometry("800x300+100+100") # 가로 * 세로 + x좌표 + y좌표

root.resizable(False, False) # 창 크기 값 변경 불가

# button 예제
def run_cmd():
    print("버튼이 클릭되었습니다.")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    url = 'https://www.hometax.go.kr'
    driver.get(url)
    driver.maximize_window()
    time.sleep(1)

    try:
        # 로그인 버튼 클릭
        driver.find_element("css selector", "#group1544").click()
        print("로그인 버튼 클릭")
        time.sleep(1)

        # 상위 iframe으로 이동
        # driver.switch_to.parent_frame()

        # iframe 전환 : 로그인화면은 화면전체가 iframe
        iframe = driver.find_element("css selector", "#txppIframe")
        driver.switch_to.frame(iframe)

        # 공인인증서 로그인 버튼 클릭
        driver.find_element("css selector", "#anchor22").click()
        print("공인인증서 로그인 버튼 클릭")
        time.sleep(2)

        # iframe 전환 : 공인인증서 로그인 화면
        iframe = driver.find_element("css selector", "#dscert")
        driver.switch_to.frame(iframe)

        # 공인인증서 선택
        driver.find_element("css selector", "a > span[title='김여울(yeoultaxaccounting firm)008102420121130181000590']").click()
        print("공인인증서 선택")
        time.sleep(2)

        # 비밀번호 입력
        passwd = 'kyw8320108!'
        driver.find_element("css selector", "#input_cert_pw").send_keys(passwd)
        print("비밀번호 입력")
        time.sleep(1)

        # 확인버튼 클릭
        driver.find_element("css selector", "#btn_confirm_iframe").click()
        print("확인버튼 클릭")
        time.sleep(2)

        # Alert 객체 생성
        alert = Alert(driver)

        # 알림 텍스트 출력
        print("알림 텍스트:", alert.text)

        # 예 선택 (확인 버튼 클릭)
        #alert.accept()
        #print("알림을 수락했습니다.")

        # 또는 아니오 선택 (취소 버튼 클릭)
        alert.dismiss()
        time.sleep(2)
        print("알림을 취소했습니다.")


        # iframe원복
        driver.switch_to.default_content()
        
        # 세무대리 납세관리 클릭
        driver.find_element("css selector", "#hdGrp9222").click()
        print("세무대리 납세관리 클릭")
        time.sleep(2)

        # iframe 전환 : 세무대리 납세관리 화면
        iframe = driver.find_element("css selector", "#txppIframe")
        driver.switch_to.frame(iframe)

        # 전자(세금)계산서 합계표 조회 클릭
        driver.find_element("css selector", "#a_a_4801100000").click()
        print("전자(세금)계산서 합계표 조회 클릭")
        time.sleep(2)

        # iframe원복
        driver.switch_to.default_content()

        # iframe 전환 : 세금계산서 합계표 조회 화면
        iframe = driver.find_element("css selector", "#txppIframe")
        driver.switch_to.frame(iframe)
        
        num = IntVar()
        num.set(0)
        # 여러 개의 사업자 번호 갯수 만큼 반복
        for business_number in business_numbers:
            num.set(num.get() + 1)
            print(f"현재 처리 중인 사업자 번호: {business_number} {num.get()}번째 반복")


            # 수임사업자전환 클릭
            driver.find_element("css selector", "#trigger501").click()
            print("수임사업자전환 클릭")
            time.sleep(2)

            # 사업자번호 검색
            # 현재 활성화된 요소에서 TAB 키를 누르기
            driver.switch_to.active_element.send_keys(Keys.TAB)
            time.sleep(1)
            driver.switch_to.active_element.send_keys(Keys.TAB)
            time.sleep(1)
            driver.switch_to.active_element.send_keys(Keys.TAB)
            time.sleep(1)
            if num.get() > 1:
                driver.switch_to.active_element.send_keys(Keys.TAB)
                time.sleep(1)

            # 화살표 아래 키를 눌러옵션 선택
            driver.switch_to.active_element.send_keys(Keys.ARROW_DOWN)
            time.sleep(1)

            # 현재 활성화된 요소에서 TAB 키를 누르기
            driver.switch_to.active_element.send_keys(Keys.TAB)
            time.sleep(1)

            driver.switch_to.active_element.send_keys(business_number)
            time.sleep(1)

            # 현재 활성화된 요소에서 TAB 키를 누르기
            driver.switch_to.active_element.send_keys(Keys.TAB)
            time.sleep(1)

            # 엔터 키를 눌러 옵션 선택
            driver.switch_to.active_element.send_keys(Keys.ENTER)
            time.sleep(2)
            
            # 현재 활성화된 요소에서 TAB 키를 누르기
            driver.switch_to.active_element.send_keys(Keys.TAB)
            time.sleep(1)

            # 현재 활성화된 요소에서 스페이스바 키를 누르기
            driver.switch_to.active_element.send_keys(Keys.SPACE)
            time.sleep(1)

            # 현재 활성화된 요소에서 TAB 키를 누르기
            driver.switch_to.active_element.send_keys(Keys.TAB)
            time.sleep(1)
            driver.switch_to.active_element.send_keys(Keys.TAB)
            time.sleep(1)
            driver.switch_to.active_element.send_keys(Keys.TAB)
            time.sleep(1)

            # 엔터 키를 눌러 옵션 선택
            driver.switch_to.active_element.send_keys(Keys.ENTER)
            time.sleep(2)

            # 분류선택
            if classifi_var.get() == 0:
                print("전자세금계산서 선택")
                driver.find_element("css selector", "#radioEtxivClsfCd_input_0").click()
                time.sleep(2)

                # 구분선택
                if division_var.get() == 0:
                    print("매출 선택")
                    driver.find_element("css selector", "#radio7_input_0").click()
                    time.sleep(2)

                    # 작성일자선택
                    if date_var.get() == 0:
                        print("일자별 선택")
                        driver.find_element("css selector", "#radio5_input_0").click()
                        time.sleep(2)
                    elif date_var.get() == 1:
                        print("월별 선택")
                        driver.find_element("css selector", "#radio5_input_1").click()
                        time.sleep(2)
                    elif date_var.get() == 2:
                        print("분기별 선택")
                        driver.find_element("css selector", "#radio5_input_2").click()
                        time.sleep(2)
                        
                # 구분선택
                elif division_var.get() == 1:
                    print("매입 선택")
                    driver.find_element("css selector", "#radio7_input_1").click()
                    time.sleep(2)

                    # 작성일자선택
                    if date_var.get() == 0:
                        print("일자별 선택")
                        driver.find_element("css selector", "#radio5_input_0").click()
                        time.sleep(2)
                    elif date_var.get() == 1:
                        print("월별 선택")
                        driver.find_element("css selector", "#radio5_input_1").click()
                        time.sleep(2)
                    elif date_var.get() == 2:
                        print("분기별 선택")
                        driver.find_element("css selector", "#radio5_input_2").click()
                        time.sleep(2)

            # 분류선택
            elif classifi_var.get() == 1:
                print("전자계산서 선택")
                driver.find_element("css selector", "#radioEtxivClsfCd_input_1").click()
                time.sleep(2)

                # 구분선택
                if division_var.get() == 0:
                    print("매출 선택")
                    driver.find_element("css selector", "#radio7_input_0").click()
                    time.sleep(2)

                    # 작성일자선택
                    if date_var.get() == 0:
                        print("일자별 선택")
                        driver.find_element("css selector", "#radio5_input_0").click()
                        time.sleep(2)
                    elif date_var.get() == 1:
                        print("월별 선택")
                        driver.find_element("css selector", "#radio5_input_1").click()
                        time.sleep(2)
                    elif date_var.get() == 2:
                        print("분기별 선택")
                        driver.find_element("css selector", "#radio5_input_2").click()
                        time.sleep(2)
                    elif date_var.get() == 3:
                        print("년도별 선택")
                        driver.find_element("css selector", "#radio5_input_3").click()
                        time.sleep(2)
                # 구분선택
                elif division_var.get() == 1:
                    print("매입 선택")
                    driver.find_element("css selector", "#radio7_input_1").click()
                    time.sleep(2)
                    # 작성일자선택
                    if date_var.get() == 0:
                        print("일자별 선택")
                        driver.find_element("css selector", "#radio5_input_0").click()
                        time.sleep(2)
                    elif date_var.get() == 1:
                        print("월별 선택")
                        driver.find_element("css selector", "#radio5_input_1").click()
                        time.sleep(2)
                    elif date_var.get() == 2:
                        print("분기별 선택")
                        driver.find_element("css selector", "#radio5_input_2").click()
                        time.sleep(2)
                    elif date_var.get() == 3:
                        print("년도별 선택")
                        driver.find_element("css selector", "#radio5_input_3").click()
                        time.sleep(2)

            # 조회버튼 클릭
            driver.find_element("css selector", "#trigger23").click()
            print("조회버튼 클릭")
            time.sleep(2)

            # 조회버튼 클릭
            driver.find_element("css selector", "#trigger25").click()
            print("명세서 조회버튼 클릭")
            time.sleep(2)
            

            # 매출 전자세금계산서 합계표 출력(매출처별 명세)
            driver.find_element("css selector", "#trigger33").click()
            print("출력버튼 클릭")
            time.sleep(3)

            alert = None
            alert = Alert(driver)

            if alert:
                # 알림 텍스트 출력
                print("알림 텍스트:", alert.text)

                # 예 선택 (확인 버튼 클릭)
                alert.accept()
                print("확인 버튼 클릭.")
                time.sleep(1)
                # 다음 for문으로 이동
                break
                print("다음 사업자번호 처리")
            else:
                # 알럿이 나타나지 않은 경우에 실행할 코드
                print("알림이 나타나지 않았습니다. 명령을 계속 진행합니다.")

            # 현재 창의 핸들 가져오기
            current_window_handle = driver.current_window_handle

            # 새로운 링크나 버튼 클릭 등으로 새 창이 열린다면
            # 새로운 창의 핸들을 가져오기
            new_window_handle = None
            while not new_window_handle:
                for handle in driver.window_handles:
                    if handle != current_window_handle:
                        new_window_handle = handle
                        break

            # 새 창으로 전환
            driver.switch_to.window(new_window_handle)

            # 현재 활성화된 요소에서 TAB 키를 누르기
            driver.switch_to.active_element.send_keys(Keys.TAB)
            time.sleep(4)
            driver.switch_to.active_element.send_keys(Keys.TAB)
            time.sleep(4        )

            # 엔터치는 여기가 문제

            # 화살표 아래 키를 눌러옵션 선택
            driver.switch_to.active_element.send_keys(Keys.ARROW_DOWN)
            time.sleep(1)

            # 화살표 아래 키를 눌러옵션 선택
            driver.switch_to.active_element.send_keys(Keys.ARROW_DOWN)
            time.sleep(1)

            # 현재 활성화된 요소에서 TAB 키를 누르기
            driver.switch_to.active_element.send_keys(Keys.TAB)
            time.sleep(1)
            driver.switch_to.active_element.send_keys(Keys.TAB)
            time.sleep(1)
            driver.switch_to.active_element.send_keys(Keys.TAB)
            time.sleep(1)
            driver.switch_to.active_element.send_keys(Keys.TAB)
            time.sleep(1)
            driver.switch_to.active_element.send_keys(Keys.TAB)
            time.sleep(1)
            driver.switch_to.active_element.send_keys(Keys.TAB)
            time.sleep(1)

            # 엔터 키를 눌러 파일 다운로드 선택
            driver.switch_to.active_element.send_keys(Keys.ENTER)
            time.sleep(3)

            # 새 창을 닫기 (예: 자동으로 닫히는 경우는 생략 가능)
            driver.close()

            # 새 창에서 작업이 완료되면 원래 창으로 전환
            driver.switch_to.window(current_window_handle)

            # iframe원복
            driver.switch_to.default_content()

            # iframe 전환 : 세금계산서 합계표 조회 화면
            iframe = driver.find_element("css selector", "#txppIframe")
            driver.switch_to.frame(iframe)



            
            


    except Exception as e:
        print(f"예외 발생: {e}")

    driver.quit()


# frame
Label(root, text="사전 선택사항을 체크해주세요").pack(side="top") #상단에 배치
btn_run = Button(root, text="실행", command=run_cmd).pack(side="bottom") #하단에 배치

frame_01 = LabelFrame(root, text="사업자번호 입력(다중입력시 엔터)")
frame_01.pack(side="top", anchor="nw", expand=False)

frame_02 = LabelFrame(root, text="분류")
frame_02.pack(side="left", fill="both", expand=True)

frame_03 = LabelFrame(root, text="구분")
frame_03.pack(side="left", fill="both", expand=True)

frame_04 = LabelFrame(root, text="작성일자", width=60)
frame_04.pack(side="left", fill="both", expand=True)

frame_05 = LabelFrame(root, text="작성일자 세부선택", width=80)
frame_05.pack(side="left", fill="both", expand=True)

def save_to_variable():
    global business_numbers
    business_numbers = txt.get("1.0", "end-1c").splitlines()
    print("입력값 : ", business_numbers)

def update_selection():
    create_additional_widgets()

def create_additional_widgets():
    # 기존의 추가 위젯 제거
    for widget in additional_widgets:
        widget.destroy()

    # 선택된 분류에 따라 추가 위젯 생성
    if classifi_var.get() == 0:
        date_radio_01 = Radiobutton(frame_04, text="일자별", variable=date_var, value=0)
        date_radio_02 = Radiobutton(frame_04, text="월별", variable=date_var, value=1)
        date_radio_03 = Radiobutton(frame_04, text="분기별", variable=date_var, value=2)
        date_radio_01.pack()
        date_radio_02.pack()
        date_radio_03.pack()
        additional_widgets.extend([date_radio_01, date_radio_02, date_radio_03])
    elif classifi_var.get() == 1:
        date_radio_01 = Radiobutton(frame_04, text="일자별", variable=date_var, value=0)
        date_radio_02 = Radiobutton(frame_04, text="월별", variable=date_var, value=1)
        date_radio_03 = Radiobutton(frame_04, text="분기별", variable=date_var, value=2)
        date_radio_04 = Radiobutton(frame_04, text="년도별", variable=date_var, value=3)
        date_radio_01.pack()
        date_radio_02.pack()
        date_radio_03.pack()
        date_radio_04.pack()
        additional_widgets.extend([date_radio_01, date_radio_02, date_radio_03, date_radio_04])


# 라디오 버튼을 위한 변수 설정
classifi_var = IntVar()
date_var = IntVar()

# 분류 선택 라디오 버튼 생성
classifi_radio_01 = Radiobutton(frame_02, text="전자세금계산서", variable=classifi_var, value=0, command=update_selection)
classifi_radio_02 = Radiobutton(frame_02, text="전자계산서", variable=classifi_var, value=1, command=update_selection)
classifi_radio_01.pack()
#classifi_radio_01.select()  # Radiobutton을 생성한 후에 select() 메서드 호출
classifi_radio_02.pack()

division_var = IntVar()  # 여기에 선택된 구분의 값을 int형으로 저장
btn_division_01 = Radiobutton(frame_03, text="매출", value=0, variable=division_var)
btn_division_01.pack()
#btn_division_01.select()  # Radiobutton을 생성한 후에 select() 메서드 호출

btn_division_02 = Radiobutton(frame_03, text="매입", value=1, variable=division_var)
btn_division_02.pack()

# 추가적인 위젯들을 저장하는 리스트
additional_widgets = []

# Text 위젯 생성
frame_01 = LabelFrame(root, text="사업자번호 입력(다중입력시 엔터)")
frame_01.pack(side="top", anchor="nw", expand=False)
txt = Text(frame_01, width=15, height=20, wrap="word")
txt.pack(side=LEFT, fill=BOTH, expand=True)
scrollbar = Scrollbar(frame_01, command=txt.yview)
scrollbar.pack(side=RIGHT, fill=Y)
txt.config(yscrollcommand=scrollbar.set)
txt.insert(END, "")

# 버튼 생성
button = Button(frame_01, text="입력", command=save_to_variable)
button.pack()

# 윈도우 실행
root.mainloop()