import urllib
from urllib.request import Request
from urllib.request import urlopen
from urllib.parse import quote_plus
from urllib.parse import urlencode
import json
from pprint import pprint
from xml.etree import ElementTree

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

def Start():
    global window
    window = Tk()
    window.title('병원정보')
    window.geometry('800x600')

    label = Label(window, text='병원정보서비스',relief='ridge',width=30,height=5)
    label.place(x=100, y=20)

    label2 = Label(window, text=' ', relief='ridge', width=47, height=7)
    label2.place(x=40, y=460)

    label = Label(window, text = '지역선택')
    label.place(x=180,y=470)

    button = Button(window, text="수원", command= lambda : HospitalInfo('수원시'))
    button.place(x=30+20,y=500)

    button2 = Button(window, text="시흥", command=lambda: HospitalInfo('시흥시'))
    button2.place(x=70+20,y=500)

    button3 = Button(window, text="경기", command=lambda: HospitalInfo('경기'))
    button3.place(x=110+20,y=500)

    button4 = Button(window, text="인천", command=lambda: HospitalInfo('인천'))
    button4.place(x=150+20,y=500)

    button5 = Button(window, text="광주", command=lambda: HospitalInfo('광주'))
    button5.place(x=190+20,y=500)

    button6 = Button(window, text="대전", command=lambda: HospitalInfo('대전'))
    button6.place(x=230+20,y=500)

    button7 = Button(window, text="강원", command=lambda: HospitalInfo('강원'))
    button7.place(x=270+20,y=500)

    button8 = Button(window, text="충북", command=lambda: HospitalInfo('충북'))
    button8.place(x=310+20,y=500)

    button9 = Button(window, text="충남", command=lambda: HospitalInfo('충남'))
    button9.place(x=30+20,y=530)

    button10 = Button(window, text="전북", command=lambda: HospitalInfo('전북'))
    button10.place(x=70+20,y=530)

    button11 = Button(window, text="전남", command=lambda: HospitalInfo('전남'))
    button11.place(x=110+20,y=530)

    button12 = Button(window, text="경북", command=lambda: HospitalInfo('경북'))
    button12.place(x=150+20,y=530)

    button13 = Button(window, text="경남", command=lambda: HospitalInfo('경남'))
    button13.place(x=190+20,y=530)

    button15 = Button(window, text="울산", command=lambda: HospitalInfo('울산'))
    button15.place(x=230+20,y=530)

    button16 = Button(window, text="세종", command=lambda: HospitalInfo('세종'))
    button16.place(x=270+20,y=530)

    button14 = Button(window, text="제주", command=lambda: HospitalInfo('제주'))
    button14.place(x=310+20,y=530)

    photo = PhotoImage(file="hospital.gif")
    imageLabel = Label(window, image=photo)
    imageLabel.place(x= 60, y=200)

    hosInfo = Listbox(window)
    hosInfo.place(x=400, y=10, width=380, height=570)

    window.mainloop()

def init():
    MakeXML()

    pass

#init()

def HospitalInfo(text):
    mentalUrl = "https://openapi.gg.go.kr/Hosptlevaltnpsychs?Key=87b45899e7ae4c1abd87299b4ef3ce04&pIndex=2&pSize=100"
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

Start()
#HospitalInfo("수원시")
