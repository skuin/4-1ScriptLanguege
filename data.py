import game_framework
import urllib
from urllib.request import Request
from urllib.request import urlopen
from urllib.parse import quote_plus
from urllib.parse import urlencode
import json
from pprint import pprint
from xml.etree import ElementTree
import smtplib
from email.mime.text import MIMEText

from tkinter import Tk, ttk, StringVar,messagebox
from tkinter import *
from tkinter import ttk

# 정신과
# https://openapi.gg.go.kr/Hosptlevaltnpsychs?Key=87b45899e7ae4c1abd87299b4ef3ce04&pIndex=1&pSize=100
# 천식
# https://openapi.gg.go.kr/Hosptlevaltnast?Key=87b45899e7ae4c1abd87299b4ef3ce04&pIndex=1&pSize=100
# 폐렴
# https://openapi.gg.go.kr/Hosptlevaltnpen?Key=87b45899e7ae4c1abd87299b4ef3ce04&pIndex=1&pSize=100
# 혈액투석
# https://openapi.gg.go.kr/Hosptlevaltnboldi?Key=87b45899e7ae4c1abd87299b4ef3ce04&pIndex=1&pSize=100
# 폐암
# https://openapi.gg.go.kr/Hosptlevaltnlunc?Key=87b45899e7ae4c1abd87299b4ef3ce04&pIndex=1&pSize=100
# 관상동맥우회술
# https://openapi.gg.go.kr/Hosptlevaltncorarby?Key=87b45899e7ae4c1abd87299b4ef3ce04&pIndex=1&pSize=100
# 대장암
# https://openapi.gg.go.kr/Hosptlevaltnlgsnc?Key=87b45899e7ae4c1abd87299b4ef3ce04&pIndex=1&pSize=100

# 약처방비용
# https://openapi.gg.go.kr/Hosptlevaltnmcex?Key=87b45899e7ae4c1abd87299b4ef3ce04&pIndex=1&pSize=100

def sendMail(you, msg):
    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.starttls()
    smtp.login('skuin2004@gmail.com', 'fyqagbhejffalhew')
    msg = MIMEText(msg)
    msg['Subject'] = '병원정보서비스'
    smtp.sendmail('skuin2004@gmail.com', you, msg.as_string())
    smtp.quit()
    messagebox.showinfo("메일전송", you+"로 메일을 전송하였습니다.")

#sendMail("skuin2004@naver.com", "테스트 메일")

def run():
    global window
    window = Tk()
    window.title('병원정보')
    window.geometry('800x600')

    label3 = Label(window, text='질병선택',relief='ridge', width=8, height=1)
    label3.place(x=20, y=100)

    # 콤보박스
    str2 = StringVar()
    combo = ttk.Combobox(window, width=20, textvariable=str2)
    combo['values'] = ('정신질환', '천식', '폐렴', '폐암', '대장암', '혈액투석', '동맥우회술')
    combo.place(x=100, y = 100)
    combo.current(0)

    def clickMe():
        label = Label(window, text=combo.get(), relief='ridge', width=15, height=2)
        label.place(x=120, y=180)

        label2 = Label(window, text='지역선택', relief='ridge', width=8, height=1)
        label2.place(x=20, y=230)

        strSigun = StringVar()
        strGrade = StringVar()
        combo2 = ttk.Combobox(window, width=20, textvariable=strSigun)
        combo2['values'] = ('수원시', '구리시', '군포시', '부천시', '성남시', '시흥시', '안산시', '안양시', '평택시', '화성시',
                            '하남시', '포천시', '파주시', '이천시', '의정부시', '의왕시', '용인시')
        combo2.place(x=100, y=230)
        combo2.set('시도군 선택')

        if combo.get() == '정신질환':
            action2 = ttk.Button(window, text="확인", command=lambda: HospitalInfo(combo2.get()))
            action2.place(x=135, y=260)
            labelMail = Label(window, text='메일전송', relief='ridge', width=8, height=1)
            labelMail.place(x=20, y=320)
            entry = Entry(window)
            entry.place(x= 100, y=320)
            send = ttk.Button(window, text="전송", command=lambda: sendMail(entry.get(), msg=infoMsg))
            send.place(x=260, y=318)

        elif combo.get() == '천식':
            action2 = ttk.Button(window, text="확인", command=lambda: HospitalInfoCehnsick(combo2.get()))
            action2.place(x=135, y=260)
            labelMail = Label(window, text='메일전송', relief='ridge', width=8, height=1)
            labelMail.place(x=20, y=320)
            entry = Entry(window)
            entry.place(x=100, y=320)
            send = ttk.Button(window, text="전송", command=lambda: sendMail(entry.get(), msg=chenMsg))
            send.place(x=260, y=318)

        elif combo.get() == '폐렴':
            action2 = ttk.Button(window, text="확인", command=lambda: HospitalInfoPaeryeom(combo2.get()))
            action2.place(x=135, y=260)
            labelMail = Label(window, text='메일전송', relief='ridge', width=8, height=1)
            labelMail.place(x=20, y=320)
            entry = Entry(window)
            entry.place(x=100, y=320)
            send = ttk.Button(window, text="전송", command=lambda: sendMail(entry.get(), msg=paeRyeomMsg))
            send.place(x=260, y=318)

        elif combo.get() == '폐암':
            action2 = ttk.Button(window, text="확인", command=lambda: HospitalInfopaecancer(combo2.get()))
            action2.place(x=135, y=260)
            labelMail = Label(window, text='메일전송', relief='ridge', width=8, height=1)
            labelMail.place(x=20, y=320)
            entry = Entry(window)
            entry.place(x=100, y=320)
            send = ttk.Button(window, text="전송", command=lambda: sendMail(entry.get(), msg=paecancerMsg))
            send.place(x=260, y=318)

        elif combo.get() == '대장암':
            action2 = ttk.Button(window, text="확인", command=lambda: HospitalInfoDaejangcanser(combo2.get()))
            action2.place(x=135, y=260)
            labelMail = Label(window, text='메일전송', relief='ridge', width=8, height=1)
            labelMail.place(x=20, y=320)
            entry = Entry(window)
            entry.place(x=100, y=320)
            send = ttk.Button(window, text="전송", command=lambda: sendMail(entry.get(), msg=DaecancerMsg))
            send.place(x=260, y=318)

        elif combo.get() == '혈액투석':
            action2 = ttk.Button(window, text="확인", command=lambda: HospitalInfoBlood(combo2.get()))
            action2.place(x=135, y=260)
            labelMail = Label(window, text='메일전송', relief='ridge', width=8, height=1)
            labelMail.place(x=20, y=320)
            entry = Entry(window)
            entry.place(x=100, y=320)
            send = ttk.Button(window, text="전송", command=lambda: sendMail(entry.get(), msg=bloodMsg))
            send.place(x=260, y=318)

        elif combo.get() == '동맥우회술':
            action2 = ttk.Button(window, text="확인", command=lambda: HospitalInfoGwansang(combo2.get()))
            action2.place(x=135, y=260)
            labelMail = Label(window, text='메일전송', relief='ridge', width=8, height=1)
            labelMail.place(x=20, y=320)
            entry = Entry(window)
            entry.place(x=100, y=320)
            send = ttk.Button(window, text="전송", command=lambda: sendMail(entry.get(), msg=gwanMsg))
            send.place(x=260, y=318)

    action = ttk.Button(window, text="확인", command=clickMe)
    action.place(x=135, y=130)

    #str3 = combo.get()
    #print(str3)
    #combo.current(0)

    label = Label(window, text='병원정보서비스',relief='ridge',width=30,height=3)
    label.place(x=90, y=20)

    #label2 = Label(window, text=' ', relief='ridge', width=47, height=7)
    #label2.place(x=40, y=460)

    #label = Label(window, text = '지역선택')
    #label.place(x=180,y=470)

    #button = Button(window, text="수원", command= lambda : HospitalInfo('수원시'))
    #button.place(x=30+20,y=500)

    #button2 = Button(window, text="시흥", command=lambda: HospitalInfoDraw('시흥시'))
    #button2.place(x=70+20,y=500)

    #button3 = Button(window, text="경기", command=lambda: HospitalInfo('경기'))
    #button3.place(x=110+20,y=500)

    #button4 = Button(window, text="인천", command=lambda: HospitalInfo('인천'))
    #button4.place(x=150+20,y=500)

    #button5 = Button(window, text="광주", command=lambda: HospitalInfo('광주'))
    #button5.place(x=190+20,y=500)

    #button6 = Button(window, text="대전", command=lambda: HospitalInfo('대전'))
    #button6.place(x=230+20,y=500)

    #button7 = Button(window, text="강원", command=lambda: HospitalInfo('강원'))
    #button7.place(x=270+20,y=500)

    #button8 = Button(window, text="충북", command=lambda: HospitalInfo('충북'))
    #button8.place(x=310+20,y=500)

    #button9 = Button(window, text="충남", command=lambda: HospitalInfo('충남'))
    #button9.place(x=30+20,y=530)

    #button10 = Button(window, text="전북", command=lambda: HospitalInfo('전북'))
    #button10.place(x=70+20,y=530)

    #button11 = Button(window, text="전남", command=lambda: HospitalInfo('전남'))
    #button11.place(x=110+20,y=530)

    #button12 = Button(window, text="경북", command=lambda: HospitalInfo('경북'))
    #button12.place(x=150+20,y=530)

    #button13 = Button(window, text="경남", command=lambda: HospitalInfo('경남'))
    #button13.place(x=190+20,y=530)

    #button15 = Button(window, text="울산", command=lambda: HospitalInfo('울산'))
    #button15.place(x=230+20,y=530)

    #button16 = Button(window, text="세종", command=lambda: HospitalInfo('세종'))
    #button16.place(x=270+20,y=530)

    #button14 = Button(window, text="제주", command=lambda: HospitalInfo('제주'))
    #button14.place(x=310+20,y=530)

    photo = PhotoImage(file="hospital.gif")
    imageLabel = Label(window, image=photo)
    imageLabel.place(x= 60, y=380)

    hosInfo = Listbox(window)
    hosInfo.place(x=400, y=10, width=380, height=570)

    window.mainloop()

#init()

def HospitalInfo(text):
    mentalUrl = "https://openapi.gg.go.kr/Hosptlevaltnpsychs?Key=87b45899e7ae4c1abd87299b4ef3ce04&pIndex=1&pSize=100"
    res = urllib.request.urlopen(mentalUrl)
    decoding = str(res.read().decode("utf-8"))
    # pprint(decoding)

    data = urllib.request.urlopen(mentalUrl).read()
    f = open("hospitalGrade.xml", "wb")
    f.write(data)
    f.close()

    sigun_Name = []
    hos_Name = []
    div_Name = []
    Grade = []
    addr = []
    addr_Num = []

    tree = ElementTree.parse("hospitalGrade.xml")
    root = tree.getroot()

    for a in root.findall('.//row'):
        sigun_Name.append(a.findtext("SIGUN_NM"))
        hos_Name.append(a.findtext("INST_NM"))
        div_Name.append(a.findtext("DIV_NM"))
        Grade.append(a.findtext("GRAD"))
        addr.append(a.findtext("REFINE_ROADNM_ADDR"))
        addr_Num.append(a.findtext("REFINE_ZIP_CD"))

    count = len(sigun_Name)
    index = 0
    num = 1
    #window = Tk()
    hosInfo = Listbox(window)
    hosInfo.place(x=400, y=10, width=380, height=570)

    global infoMsg

    for i in range (0, count):
        if sigun_Name[i] == text:
            hosInfo.insert(index, '[ ' + str(num) + ' ]')
            index += 1
            hosInfo.insert(index, '등급: ' + Grade[i])
            index += 1
            hosInfo.insert(index, '병원이름: '+ hos_Name[i])
            index +=1
            hosInfo.insert(index, '평가내역: ' + div_Name[i])
            index += 1
            hosInfo.insert(index, '주소:' + addr[i])
            index +=1
            hosInfo.insert(index, '우편번호: ' + addr_Num[i])
            index += 1
            hosInfo.insert(index, '===========================================================')
            index += 1
            num += 1
            if Grade[i] == "1등급":
                infoMsg = str('[ 1등급 병원 정보 ]\n' +
                             '병원이름 : ' + hos_Name[i] + '\n' +
                             '평가내역 : ' + div_Name[i] + '\n' +
                             '등급 : ' + Grade[i] + '\n' +
                             '주소 : ' + addr[i] + '\n' +
                             '우편번호 : ' + addr_Num[i] + '\n' +
                             '===========================================================\n'
                             )


    #hosInfo.insert(1, hosNameList[0])
    #hosInfo.insert(2, hosAddrList[0])

    #hosInfo.insert(0, )

    pass

def HospitalInfoPaeryeom(text):
    mentalUrl = "https://openapi.gg.go.kr/Hosptlevaltnpen?Key=87b45899e7ae4c1abd87299b4ef3ce04&pIndex=1&pSize=100"
    res = urllib.request.urlopen(mentalUrl)
    decoding = str(res.read().decode("utf-8"))
    # pprint(decoding)

    data = urllib.request.urlopen(mentalUrl).read()
    f = open("hospitalGrade.xml", "wb")
    f.write(data)
    f.close()

    sigun_Name = []
    hos_Name = []
    div_Name = []
    Grade = []
    addr = []
    addr_Num = []

    tree = ElementTree.parse("hospitalGrade.xml")
    root = tree.getroot()

    for a in root.findall('.//row'):
        sigun_Name.append(a.findtext("SIGUN_NM"))
        hos_Name.append(a.findtext("INST_NM"))
        div_Name.append(a.findtext("DIV_NM"))
        Grade.append(a.findtext("GRAD"))
        addr.append(a.findtext("REFINE_ROADNM_ADDR"))
        addr_Num.append(a.findtext("REFINE_ZIP_CD"))

    count = len(sigun_Name)
    index = 0
    num = 1
    #window = Tk()
    hosInfo = Listbox(window)
    hosInfo.place(x=400, y=10, width=380, height=570)
    global paeRyeomMsg

    for i in range (0, count):
        if sigun_Name[i] == text:
            hosInfo.insert(index, '[ ' + str(num) + ' ]')
            index += 1
            hosInfo.insert(index, '병원이름: '+ hos_Name[i])
            index +=1
            hosInfo.insert(index, '평가내역: ' + div_Name[i])
            index += 1
            hosInfo.insert(index, '등급: ' + Grade[i])
            index += 1
            hosInfo.insert(index, '주소:' + addr[i])
            index +=1
            hosInfo.insert(index, '우편번호: ' + addr_Num[i])
            index += 1
            hosInfo.insert(index, '===========================================================')
            index += 1
            num += 1
            if Grade[i] == "1등급":
                paeRyeomMsg = str('[ 1등급 병원 정보 ]\n' +
                             '병원이름 : ' + hos_Name[i] + '\n' +
                             '평가내역 : ' + div_Name[i] + '\n' +
                             '등급 : ' + Grade[i] + '\n' +
                             '주소 : ' + addr[i] + '\n' +
                             '우편번호 : ' + addr_Num[i] + '\n' +
                             '===========================================================\n'
                             )



    #hosInfo.insert(1, hosNameList[0])
    #hosInfo.insert(2, hosAddrList[0])

    #hosInfo.insert(0, )

    pass

def HospitalInfoCehnsick(text):
    mentalUrl = "https://openapi.gg.go.kr/Hosptlevaltnast?Key=87b45899e7ae4c1abd87299b4ef3ce04&pIndex=1&pSize=100"
    res = urllib.request.urlopen(mentalUrl)
    decoding = str(res.read().decode("utf-8"))
    # pprint(decoding)

    data = urllib.request.urlopen(mentalUrl).read()
    f = open("hospitalGrade.xml", "wb")
    f.write(data)
    f.close()

    sigun_Name = []
    hos_Name = []
    div_Name = []
    Grade = []
    addr = []
    addr_Num = []

    tree = ElementTree.parse("hospitalGrade.xml")
    root = tree.getroot()

    for a in root.findall('.//row'):
        sigun_Name.append(a.findtext("SIGUN_NM"))
        hos_Name.append(a.findtext("INST_NM"))
        div_Name.append(a.findtext("DIV_NM"))
        Grade.append(a.findtext("GRAD"))
        addr.append(a.findtext("REFINE_ROADNM_ADDR"))
        addr_Num.append(a.findtext("REFINE_ZIP_CD"))

    count = len(sigun_Name)
    index = 0
    num = 1
    #window = Tk()
    hosInfo = Listbox(window)
    hosInfo.place(x=400, y=10, width=380, height=570)

    global chenMsg

    for i in range (0, count):
        if sigun_Name[i] == text:
            hosInfo.insert(index, '[ ' + str(num) + ' ]')
            index += 1
            hosInfo.insert(index, '병원이름: '+ hos_Name[i])
            index +=1
            hosInfo.insert(index, '평가내역: ' + div_Name[i])
            index += 1
            hosInfo.insert(index, '등급: ' + Grade[i])
            index += 1
            hosInfo.insert(index, '주소:' + addr[i])
            index +=1
            hosInfo.insert(index, '우편번호: ' + addr_Num[i])
            index += 1
            hosInfo.insert(index, '===========================================================')
            index += 1
            num += 1
            if Grade[i] == "양호":
                chenMsg = str('[ 양호 병원 정보 ]\n' +
                             '병원이름 : ' + hos_Name[i] + '\n' +
                             '평가내역 : ' + div_Name[i] + '\n' +
                             '등급 : ' + Grade[i] + '\n' +
                             '주소 : ' + addr[i] + '\n' +
                             '우편번호 : ' + addr_Num[i] + '\n' +
                             '===========================================================\n'
                             )



    #hosInfo.insert(1, hosNameList[0])
    #hosInfo.insert(2, hosAddrList[0])

    #hosInfo.insert(0, )

    pass

def HospitalInfoBlood(text):
    mentalUrl = "https://openapi.gg.go.kr/Hosptlevaltnboldi?Key=87b45899e7ae4c1abd87299b4ef3ce04&pIndex=1&pSize=100"
    res = urllib.request.urlopen(mentalUrl)
    decoding = str(res.read().decode("utf-8"))
    # pprint(decoding)

    data = urllib.request.urlopen(mentalUrl).read()
    f = open("hospitalGrade.xml", "wb")
    f.write(data)
    f.close()

    sigun_Name = []
    hos_Name = []
    div_Name = []
    Grade = []
    addr = []
    addr_Num = []

    tree = ElementTree.parse("hospitalGrade.xml")
    root = tree.getroot()

    for a in root.findall('.//row'):
        sigun_Name.append(a.findtext("SIGUN_NM"))
        hos_Name.append(a.findtext("INST_NM"))
        div_Name.append(a.findtext("DIV_NM"))
        Grade.append(a.findtext("GRAD"))
        addr.append(a.findtext("REFINE_ROADNM_ADDR"))
        addr_Num.append(a.findtext("REFINE_ZIP_CD"))

    count = len(sigun_Name)
    index = 0
    num = 1
    #window = Tk()
    hosInfo = Listbox(window)
    hosInfo.place(x=400, y=10, width=380, height=570)

    global bloodMsg

    for i in range (0, count):
        if sigun_Name[i] == text:
            hosInfo.insert(index, '[ ' + str(num) + ' ]')
            index += 1
            hosInfo.insert(index, '병원이름: '+ hos_Name[i])
            index +=1
            hosInfo.insert(index, '평가내역: ' + div_Name[i])
            index += 1
            hosInfo.insert(index, '등급: ' + Grade[i])
            index += 1
            hosInfo.insert(index, '주소:' + addr[i])
            index +=1
            hosInfo.insert(index, '우편번호: ' + addr_Num[i])
            index += 1
            hosInfo.insert(index, '===========================================================')
            index += 1
            num += 1
            if Grade[i] == "1등급":
                bloodMsg = str('[ 1등급 병원 정보 ]\n' +
                             '병원이름 : ' + hos_Name[i] + '\n' +
                             '평가내역 : ' + div_Name[i] + '\n' +
                             '등급 : ' + Grade[i] + '\n' +
                             '주소 : ' + addr[i] + '\n' +
                             '우편번호 : ' + addr_Num[i] + '\n' +
                             '===========================================================\n'
                             )



    #hosInfo.insert(1, hosNameList[0])
    #hosInfo.insert(2, hosAddrList[0])

    #hosInfo.insert(0, )

    pass

def HospitalInfopaecancer(text):
    mentalUrl = "https://openapi.gg.go.kr/Hosptlevaltnlunc?Key=87b45899e7ae4c1abd87299b4ef3ce04&pIndex=1&pSize=100"
    res = urllib.request.urlopen(mentalUrl)
    decoding = str(res.read().decode("utf-8"))
    # pprint(decoding)

    data = urllib.request.urlopen(mentalUrl).read()
    f = open("hospitalGrade.xml", "wb")
    f.write(data)
    f.close()

    sigun_Name = []
    hos_Name = []
    div_Name = []
    Grade = []
    addr = []
    addr_Num = []

    tree = ElementTree.parse("hospitalGrade.xml")
    root = tree.getroot()

    for a in root.findall('.//row'):
        sigun_Name.append(a.findtext("SIGUN_NM"))
        hos_Name.append(a.findtext("INST_NM"))
        div_Name.append(a.findtext("DIV_NM"))
        Grade.append(a.findtext("GRAD"))
        addr.append(a.findtext("REFINE_ROADNM_ADDR"))
        addr_Num.append(a.findtext("REFINE_ZIP_CD"))

    count = len(sigun_Name)
    index = 0
    num = 1
    #window = Tk()
    hosInfo = Listbox(window)
    hosInfo.place(x=400, y=10, width=380, height=570)

    global paecancerMsg

    for i in range (0, count):
        if sigun_Name[i] == text:
            hosInfo.insert(index, '[ ' + str(num) + ' ]')
            index += 1
            hosInfo.insert(index, '병원이름: '+ hos_Name[i])
            index +=1
            hosInfo.insert(index, '평가내역: ' + div_Name[i])
            index += 1
            hosInfo.insert(index, '등급: ' + Grade[i])
            index += 1
            hosInfo.insert(index, '주소:' + addr[i])
            index +=1
            hosInfo.insert(index, '우편번호: ' + addr_Num[i])
            index += 1
            hosInfo.insert(index, '===========================================================')
            index += 1
            num += 1
            if Grade[i] == "1등급":
                paecancerMsg = str('[ 1등급 병원 정보 ]\n' +
                             '병원이름 : ' + hos_Name[i] + '\n' +
                             '평가내역 : ' + div_Name[i] + '\n' +
                             '등급 : ' + Grade[i] + '\n' +
                             '주소 : ' + addr[i] + '\n' +
                             '우편번호 : ' + addr_Num[i] + '\n' +
                             '===========================================================\n'
                             )


    #hosInfo.insert(1, hosNameList[0])
    #hosInfo.insert(2, hosAddrList[0])

    #hosInfo.insert(0, )

    pass

def HospitalInfoGwansang(text):
    mentalUrl = "https://openapi.gg.go.kr/Hosptlevaltncorarby?Key=87b45899e7ae4c1abd87299b4ef3ce04&pIndex=1&pSize=100"
    res = urllib.request.urlopen(mentalUrl)
    decoding = str(res.read().decode("utf-8"))
    # pprint(decoding)

    data = urllib.request.urlopen(mentalUrl).read()
    f = open("hospitalGrade.xml", "wb")
    f.write(data)
    f.close()

    sigun_Name = []
    hos_Name = []
    div_Name = []
    Grade = []
    addr = []
    addr_Num = []

    tree = ElementTree.parse("hospitalGrade.xml")
    root = tree.getroot()

    for a in root.findall('.//row'):
        sigun_Name.append(a.findtext("SIGUN_NM"))
        hos_Name.append(a.findtext("INST_NM"))
        div_Name.append(a.findtext("DIV_NM"))
        Grade.append(a.findtext("GRAD"))
        addr.append(a.findtext("REFINE_ROADNM_ADDR"))
        addr_Num.append(a.findtext("REFINE_ZIP_CD"))

    count = len(sigun_Name)
    index = 0
    num = 1
    #window = Tk()
    hosInfo = Listbox(window)
    hosInfo.place(x=400, y=10, width=380, height=570)

    global gwanMsg

    for i in range (0, count):
        if sigun_Name[i] == text:
            hosInfo.insert(index, '[ ' + str(num) + ' ]')
            index += 1
            hosInfo.insert(index, '병원이름: '+ hos_Name[i])
            index +=1
            hosInfo.insert(index, '평가내역: ' + div_Name[i])
            index += 1
            hosInfo.insert(index, '등급: ' + Grade[i])
            index += 1
            hosInfo.insert(index, '주소:' + addr[i])
            index +=1
            hosInfo.insert(index, '우편번호: ' + addr_Num[i])
            index += 1
            hosInfo.insert(index, '===========================================================')
            index += 1
            num += 1
            if Grade[i] == "1등급":
                gwanMsg = str('[ 1등급 병원 정보 ]\n' +
                             '병원이름 : ' + hos_Name[i] + '\n' +
                             '평가내역 : ' + div_Name[i] + '\n' +
                             '등급 : ' + Grade[i] + '\n' +
                             '주소 : ' + addr[i] + '\n' +
                             '우편번호 : ' + addr_Num[i] + '\n' +
                             '===========================================================\n'
                             )




    #hosInfo.insert(1, hosNameList[0])
    #hosInfo.insert(2, hosAddrList[0])

    #hosInfo.insert(0, )

    pass

def HospitalInfoDaejangcanser(text):
    mentalUrl = "https://openapi.gg.go.kr/Hosptlevaltnlgsnc?Key=87b45899e7ae4c1abd87299b4ef3ce04&pIndex=1&pSize=100"
    res = urllib.request.urlopen(mentalUrl)
    decoding = str(res.read().decode("utf-8"))
    # pprint(decoding)

    data = urllib.request.urlopen(mentalUrl).read()
    f = open("hospitalGrade.xml", "wb")
    f.write(data)
    f.close()

    sigun_Name = []
    hos_Name = []
    div_Name = []
    Grade = []
    addr = []
    addr_Num = []

    tree = ElementTree.parse("hospitalGrade.xml")
    root = tree.getroot()

    for a in root.findall('.//row'):
        sigun_Name.append(a.findtext("SIGUN_NM"))
        hos_Name.append(a.findtext("INST_NM"))
        div_Name.append(a.findtext("DIV_NM"))
        Grade.append(a.findtext("GRAD"))
        addr.append(a.findtext("REFINE_ROADNM_ADDR"))
        addr_Num.append(a.findtext("REFINE_ZIP_CD"))

    count = len(sigun_Name)
    index = 0
    num = 1
    #window = Tk()
    hosInfo = Listbox(window)
    hosInfo.place(x=400, y=10, width=380, height=570)

    global DaecancerMsg

    for i in range (0, count):
        if sigun_Name[i] == text:
            hosInfo.insert(index, '[ ' + str(num) + ' ]')
            index += 1
            hosInfo.insert(index, '병원이름: '+ hos_Name[i])
            index +=1
            hosInfo.insert(index, '평가내역: ' + div_Name[i])
            index += 1
            hosInfo.insert(index, '등급: ' + Grade[i])
            index += 1
            hosInfo.insert(index, '주소:' + addr[i])
            index +=1
            hosInfo.insert(index, '우편번호: ' + addr_Num[i])
            index += 1
            hosInfo.insert(index, '===========================================================')
            index += 1
            num += 1
            if Grade[i] == "1등급":
                DaecancerMsg = str('[ 1등급 병원 정보 ]\n' +
                             '병원이름 : ' + hos_Name[i] + '\n' +
                             '평가내역 : ' + div_Name[i] + '\n' +
                             '등급 : ' + Grade[i] + '\n' +
                             '주소 : ' + addr[i] + '\n' +
                             '우편번호 : ' + addr_Num[i] + '\n' +
                             '===========================================================\n'
                             )




    #hosInfo.insert(1, hosNameList[0])
    #hosInfo.insert(2, hosAddrList[0])

    #hosInfo.insert(0, )

    pass


def HospitalInfoDraw(text):
    mentalUrl = "https://openapi.gg.go.kr/Hosptlevaltnmcex?Key=87b45899e7ae4c1abd87299b4ef3ce04&pIndex=1&pSize=100"
    res = urllib.request.urlopen(mentalUrl)
    decoding = str(res.read().decode("utf-8"))
    # pprint(decoding)

    data = urllib.request.urlopen(mentalUrl).read()
    f = open("hospitalGrade.xml", "wb")
    f.write(data)
    f.close()

    sigun_Name = []
    hos_Name = []
    div_Name = []
    Grade = []
    addr = []
    addr_Num = []

    tree = ElementTree.parse("hospitalGrade.xml")
    root = tree.getroot()

    for a in root.findall('.//row'):
        sigun_Name.append(a.findtext("SIGUN_NM"))
        hos_Name.append(a.findtext("INST_NM"))
        div_Name.append(a.findtext("DIV_NM"))
        Grade.append(a.findtext("GRAD"))
        addr.append(a.findtext("REFINE_ROADNM_ADDR"))
        addr_Num.append(a.findtext("REFINE_ZIP_CD"))

    count = len(sigun_Name)
    index = 0
    num = 1
    #window = Tk()
    hosInfo = Listbox(window)
    hosInfo.place(x=400, y=10, width=380, height=570)

    for i in range (0, count):
        if sigun_Name[i] == text:
            hosInfo.insert(index, '[ ' + str(num) + ' ]')
            index += 1
            hosInfo.insert(index, '병원이름: '+ hos_Name[i])
            index +=1
            hosInfo.insert(index, '평가내역: ' + div_Name[i])
            index += 1
            hosInfo.insert(index, '등급: ' + Grade[i])
            index += 1
            hosInfo.insert(index, '주소:' + addr[i])
            index +=1
            hosInfo.insert(index, '우편번호: ' + addr_Num[i])
            index += 1
            hosInfo.insert(index, '===========================================================')
            index += 1
            num += 1



    #hosInfo.insert(1, hosNameList[0])
    #hosInfo.insert(2, hosAddrList[0])

    #hosInfo.insert(0, )

    pass

#Start()
#HospitalInfo("수원시")
