from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
# Create your views here.

def index(request):
    return render(request,'index.html')


def result(request):
    # 삼성전자 
    url1 = "https://finance.naver.com/search/searchList.nhn?query=%BB%EF%BC%BA%C0%FC%C0%DA"
    res = requests.get(url1)
    html = res.text
    soup = BeautifulSoup(res.content, "html.parser")
    data1 = soup.select("td")[1].text
    # 삼성sdi
    url1 = "https://finance.naver.com/search/searchList.nhn?query=%BB%EF%BC%BAsdi"
    res = requests.get(url1)
    html = res.text
    soup = BeautifulSoup(res.content, "html.parser")
    data2 = soup.select("td")[1].text
    print(data2)
    #오늘의 날씨
    url1 = 'https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=%EC%98%A4%EB%8A%98%EC%9D%98+%EB%82%A0%EC%94%A8'
    res = requests.get(url1)
    html = res.text
    soup = BeautifulSoup(res.content, "html.parser")

    # #main_pack > div.sc.cs_weather._weather > div:nth-child(2) > div.weather_box > div.weather_area._mainArea > div.today_area._mainTabContent > div.main_info > div > ul
    data3 = soup.select("p.cast_txt")[0].text
    data4 = soup.select("span.sensible > em")[0].text
    print(data3)
    print(data4)

    context = {
        'samsung1': data1,
        'samsung2': data2,
        'txt':data3,
        'temp':data4,

    }
    pass
    return render(request,'result.html',context)