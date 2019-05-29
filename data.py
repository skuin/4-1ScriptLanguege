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

def PrintData():
    ServiceKey = "ybnIgV0VKqAjxonAPCPFPvTtRAKhhARpuEKCRgD7Lx5UNuNc%2B56Bg2OEbpi97TdsSizzYpAetBB1TWTyiO2dvQ%3D%3D"
    url = "http://apis.data.go.kr/B551182/hospInfoService/getHospBasisList?pageNo=1&numOfRows=10&ServiceKey=" + ServiceKey

    response = urllib.request.urlopen(url)
    decoding = str(response.read().decode("utf-8"))
    # print(decoding)
    # dict = json.loads(decoding)
    pprint(decoding)
    pass

def MakeXML():
    url = "http://apis.data.go.kr/B551182/hospInfoService/getHospBasisList?pageNo=1&numOfRows=50&ServiceKey=ybnIgV0VKqAjxonAPCPFPvTtRAKhhARpuEKCRgD7Lx5UNuNc%2B56Bg2OEbpi97TdsSizzYpAetBB1TWTyiO2dvQ%3D%3D"
    data = urllib.request.urlopen(url).read()
    f = open("hospital.xml", "wb")
    f.write(data)
    f.close()
    pass

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

    button = Button(window, text="서울", command= lambda : HospitalInfo('서울'))
    button.place(x=30+20,y=500)

    button2 = Button(window, text="부산", command=lambda: HospitalInfo('부산'))
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
    tree = ElementTree.parse("hospital.xml")     # 병원 정보를 xml 형식으로 파싱
    root = tree.getroot()                        # xml의 root 요소를 추출

    # 시도 코드
    # 서울 11 부산 21 대구 22 인천 23 광주 24 대전 25 울산 26 세종 29
    # 경기 31 강원 32 충북 33 충남 34 전북 35 전남 36 경북 37 경남 38 제주 39

    sidoCdList = []     # 시도코드
    hosAddrList = []    # 병원주소
    hosNameList = []    # 병원이름
    clCdNmList = []     # 종별코드 ( 종합병원 등 )
    sidoList = []       # 시도
    sgguList = []       # 시군구
    emdongList = []     # 읍면동
    postNoList = []     # 우편번호
    telnoList = []      # 전화번호
    hospUrl = []        # 홈페이지

    for a in root.findall('.//item'):
        dic = {"addr": a.findtext("addr"), "name": a.findtext("yadmNm")}
        sidoCdList.append(a.findtext("sidoCd"))
        hosAddrList.append(a.findtext("addr"))
        hosNameList.append(a.findtext("yadmNm"))
        clCdNmList.append(a.findtext("clCdNm"))
        sidoList.append(a.findtext("sidoCdNm"))
        sgguList.append(a.findtext("sgguCdNm"))
        emdongList.append(a.findtext("emdongNm"))
        postNoList.append(a.findtext("postNo"))
        telnoList.append(a.findtext("telno"))
        hospUrl.append(a.findtext("hospUrl"))

    count = len(sidoCdList)
    num = 1
    num2 = 1
    index = 0
    for i in range (0, count):
        if sidoList[i] == text:
            print('[ ' + str(num) + ' ]')
            print(hosNameList[i])
            print(hosAddrList[i])
            print(clCdNmList[i])
            print(postNoList[i])
            print(telnoList[i])
            print(hospUrl[i])
            print('===========================================================')
            num+=1

    #window = Tk()
    hosInfo = Listbox(window)
    hosInfo.place(x=400, y=10, width=380, height=570)

    for i in range (0, count):
        if sidoList[i] == text:
            hosInfo.insert(index, '[ ' + str(num2) + ' ]')
            index += 1
            hosInfo.insert(index, '병원이름: '+ hosNameList[i])
            index+=1
            hosInfo.insert(index, '주소:' + hosAddrList[i])
            index+=1
            hosInfo.insert(index, '병원종류: '+ clCdNmList[i])
            index += 1
            hosInfo.insert(index, '우편번호: ' + postNoList[i])
            index += 1
            hosInfo.insert(index, '전화번호: ' + telnoList[i])
            index += 1
            hosInfo.insert(index, '홈페이지: ' + hospUrl[i])
            index += 1
            hosInfo.insert(index, '===========================================================')
            index += 1
            num2+=1



    #hosInfo.insert(1, hosNameList[0])
    #hosInfo.insert(2, hosAddrList[0])

    #hosInfo.insert(0, )

    pass

Start()
HospitalInfo('전북')

