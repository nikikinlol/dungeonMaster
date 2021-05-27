import requests
from bs4 import BeautifulSoup
from urllib.parse import quote
import parse
class Link:
    def __init__(self):
        pass

    def enter_the_inf(self):
        print("Потрібно ввести назву міста спочатку на російській потім на англійській, нажміть на enter ще раз після першого вводу")
        x = str(input(("Введіть назву міста:")))
        return x
    def poiskpersSin(self, nick):
        geourl = "https://ua.sinoptik.ua/{0}".format(quote(nick))
        return geourl
    def poiskpersMet(self, nick):
        geourl  = "https://www.meteoprog.ua/ru/{0}".format(quote(nick))
        return geourl

class Request:
    HEADERS = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) '
                      'Chrome/88.0.4324.190 Safari/537.36',
        'accept': '*/*'}
    def __init__(self, URL1):
        self.URL1 = URL1

    def get_html(self, params=None):
        r = requests.get(self.URL1, headers=self.HEADERS, params=params)
        return r.text

class Weather_father():
    def __init__(self, html, mainClass, mainNextDay, tabsContentInner, temperature, pClassOne, pClassTwo, pClassThree, min, max):
        self.html = html
        self.mainClass = mainClass
        self.mainNextDay = mainNextDay
        self.tabsContentInner = tabsContentInner
        self.temperature = temperature
        self.pClassOne = pClassOne
        self.pClassTwo = pClassTwo
        self.pClassThree = pClassThree
        self.min = min
        self.max = max
    def start_gettingSinoptik(self):
        soup = BeautifulSoup(self.html, 'html.parser')
        # Ищет в этом классе
        items = soup.find_all('div', class_=self.mainClass)
        weather1 = []
        weather2 = []
        weather3 = []
        weatherNextDay = []
        for item in items:
            weather1.append(dict(
                title=item.find('p', class_= self.pClassOne).get_text(),
                date1=item.find('p', class_= self.pClassTwo).get_text(),
                date2=item.find('p', class_= self.pClassThree).get_text(),
                temp=item.find('div', class_= self.min).get_text(),
                temp2=item.find('div', class_= self.max).get_text(),
            ))
            itemsNextDay = soup.find_all('div', id=self.mainNextDay)
            for item in itemsNextDay:
                weatherNextDay.append(dict(
                    title=item.find('a', class_=self.pClassOne).get_text(),
                    date1=item.find('p', class_=self.pClassTwo).get_text(),
                    date2=item.find('p', class_=self.pClassThree).get_text(),
                    temp=item.find('div', class_=self.min).get_text(),
                    temp2=item.find('div', class_=self.max).get_text(),
                ))

            # print(weatherNextDay)
            item2 = soup.find_all('div', class_=self.tabsContentInner)

            for item in item2:
                weather2.append(
                    dict(vol1=item.find('td', class_='p1').get_text(), vol2=item.find('td', class_='p2').get_text(),
                         vol3=item.find('td', class_='p3').get_text(), vol4=item.find('td', class_='p4').get_text(),
                         vol5=item.find('td', class_='p5').get_text(), vol6=item.find('td', class_='p6').get_text(),
                         vol7=item.find('td', class_='p7').get_text(),
                         vol8=item.find('td', class_='p8').get_text()))

            item3 = soup.find_all('tr', class_=self.temperature)

            for item in item3:
                weather3.append(
                    dict(vol1=item.find('td', class_='p1').get_text(), vol2=item.find('td', class_='p2').get_text(),
                         vol3=item.find('td', class_='p3').get_text(), vol4=item.find('td', class_='p4').get_text(),
                         vol5=item.find('td', class_='p5').get_text(), vol6=item.find('td', class_='p6').get_text(),
                         vol7=item.find('td', class_='p7').get_text(),
                         vol8=item.find('td', class_='p8').get_text()))
        return [weather1, weather2, weather3, weatherNextDay]

    def start_gettingMeteoprog(self):
        soup = BeautifulSoup(self.html, 'html.parser')
        items = soup.find_all(attrs={'data-daynumber': '0'})
        weather1 = []

        for item in items:
            weather1.append(dict(
                title=item.find('div', class_=self.tabsContentInner).get_text(),
                date1=item.find('div', class_=self.temperature).get_text(),
                temp1=item.find('div', class_=self.pClassOne).get_text(),
                temp2=item.find('div', class_=self.pClassTwo).get_text(),
            ))
        itemsNextDay = soup.find_all(attrs={'data-daynumber': '1'})
        weather2 = []

        for item in itemsNextDay:
            weather2.append(dict(
                title=item.find('div', class_=self.tabsContentInner).get_text(),
                date1=item.find('div', class_=self.temperature).get_text(),
                temp=item.find('div', class_=self.pClassOne).get_text(),
                temp2=item.find('div', class_=self.pClassTwo).get_text(),
            ))
        return [weather1, weather2]

class ContentSinoptik(Weather_father, Link):
    def __init__(self, html, mainClass, mainNextDay, tabsContentInner, temperature, pClassOne, pClassTwo, pClassThree, min, max):
        super(ContentSinoptik, self).__init__(html, mainClass, mainNextDay, tabsContentInner, temperature, pClassOne, pClassTwo, pClassThree, min, max)

    def outputInf(self, weatherList):
        dicSet = super().enter_the_inf()
        weatherFather = weatherList[0]
        weatherFather2 = weatherList[1]
        weatherFather3 = weatherList[2]
        weatherNextDay = weatherList[3]

        for i in weatherFather:
            w1 = i
        for i in weatherFather2:
            w2 = i
        for i in weatherFather3:
            w3 = i
        for i in weatherNextDay:
            w4 = i
        print("------------------------------------------------------")
        print("\t\t\t\t\t\t\t\t\t\tПогода з сайту Sinoptik " + dicSet)
        print("День:" + w1['title'])
        print("Число: " + w1['date1'], ' ', w1['date2'])
        print("Температура: :" + w1['temp'], " ||  " + w1['temp2'])
        print()

        mw2 = []
        for i in w2:
            mw2.append(w2[i])
        mw3 = []
        for i in w3:
            mw3.append(w3[i])
        print("Прогноз на день")
        for i in mw2:
            print(i, end='     ')
        print()
        for j in mw3:
            print(j, end='       ')
            if j == mw3[4]:
                print(end='  ')
            if j == mw3[5]:
                print(end='   ')
        print()

        # ТЕМПЕРАТУРА НА СЕГОДНЯ
        result1 = w1['temp'] + w1['temp2']
        currentTemp = []
        num = ""
        for char in result1:
            if char.isdigit():
                num = num + char
            else:
                if num != '':
                    currentTemp.append(int(num))
                    num = ''
        if num != '':
            currentTemp.append(int(num))
        # ---------------------

        # ТЕМПЕРАТУРА НА ЗАВТРА
        result1 = w4['temp'] + w4['temp2']
        weatherFuture = []
        num2 = ""
        for char in result1:
            if char.isdigit():
                num2 = num2 + char
            else:
                if num2 != '':
                    weatherFuture.append(int(num2))
                    num2 = ''
        if num2 != '':
            weatherFuture.append(int(num2))
        # ---------------------

        # ЗАПИСИСЬ ТЕКУЩЕЙ ПОГОДЫ В ФАЙЛ
        try:
            files = open("w1.txt", "w")
            files.write(str(currentTemp))
            files.close()
        except:
            print()
        # ---------------------

        # ЗАПИСЬ БУДУЮЩЕЙ ПОГОДЫ В ФАЙЛ ДЛЯ ПОДАЛЬШЕГО СРАВНЕНИЯ
        try:
            files = open("w2.txt", "a")
            files.write(str(weatherFuture))
            files.close()
        except:
            print()
        # ---------------------
        # ЗАПИСЬ ЗАВТРАШНЕЙ И СЕГОДНЯШНЕЙ ТЕМПЕРАТУРЫ В ПЕРЕМЕННЫЕ
        files = open("w2.txt", "r")
        openWeatherPast = files.read()
        files.close()
        files = open("w1.txt", "r")
        openWeatherCurrent = files.read()
        files.close()

        # ПРЕОБРАЗОВАНИЕ В МАСИВ
        pastW = list(map(int, openWeatherPast[1:-1].split(',')))
        currentW = list(map(int, openWeatherCurrent[1:-1].split(',')))
        # ---------------------

        minTemp = currentW[0] - pastW[0]
        maxTemp = currentW[1] - pastW[1]
        print("Відхилення погоди на sinoptik.ua може становити від {} до {} градусів".format(abs(maxTemp), abs(minTemp)))
        print("------------------------------------------------------")

# https://www.meteoprog.ua/ru/weather/London/
class ContentMeteoprog(ContentSinoptik):
    def __init__(self, html, mainClass, mainNextDay, tabsContentInner, temperature, pClassOne, pClassTwo, pClassThree, min, max):
        super(ContentMeteoprog, self).__init__(html, mainClass, mainNextDay, tabsContentInner, temperature, pClassOne, pClassTwo, pClassThree, min, max)

    def outputInf(self, weather):
        dicSet = super().enter_the_inf()
        weatherToday = weather[0]
        weatherTomorrow = weather[1]
        for i in weatherToday:
            w1 = i
        for i in weatherTomorrow:
            w2 = i
        print("------------------------------------------------------")
        print("\t\t\t\t\t\t\t\t\t\tПогода з сайту MeteoProg " + dicSet)
        print("День:" + w1['title'].strip())
        print("Число: " + w1['date1'].strip())
        print("Температура: " + w1['temp1'] + " || " + w1['temp2'])
        # ТЕМПЕРАТУРА НА СЕГОДНЯ
        result1 = w1['temp1'] + w1['temp2']
        currentTemp = []
        num1 = ""
        for char in result1:
            if char.isdigit():
                num1 = num1 + char
            else:
                if num1 != '':
                    currentTemp.append(int(num1))
                    num1 = ''
        if num1 != '':
            currentTemp.append(int(num1))
        # ---------------------

        # ТЕМПЕРАТУРА НА ЗАВТРА
        result2 = w2['temp'] + w2['temp2']
        weatherFuture = []
        num2 = ""
        for char in result2:
            if char.isdigit():
                num2 = num2 + char
            else:
                if num2 != '':
                    weatherFuture.append(int(num2))
                    num2 = ''
        if num2 != '':
            weatherFuture.append(int(num2))

        # ---------------------

        # ЗАПИСИСЬ ТЕКУЩЕЙ ПОГОДЫ В ФАЙЛ
        try:
            files = open("w1M.txt", "w")
            files.write(str(currentTemp))
            files.close()
        except:
            print()
        # ---------------------

        # ЗАПИСЬ БУДУЮЩЕЙ ПОГОДЫ В ФАЙЛ ДЛЯ ПОДАЛЬШЕГО СРАВНЕНИЯ
        try:
            files = open("w2M.txt", "a")
            files.write(str(weatherFuture))
            files.close()
        except:
            print()
        # ---------------------

        # ЗАПИСЬ ЗАВТРАШНЕЙ И СЕГОДНЯШНЕЙ ТЕМПЕРАТУРЫ В ПЕРЕМЕННЫЕ
        files = open("w2M.txt", "r")
        openWeatherPast = files.read()
        files.close()
        files = open("w1M.txt", "r")
        openWeatherCurrent = files.read()
        files.close()
        # print("Температура на завтра")
        # print(openWeatherPast)
        # ---------------------

        # ПРЕОБРАЗОВАНИЕ В МАСИВ
        pastW = list(map(int, openWeatherPast[1:-1].split(',')))
        currentW = list(map(int, openWeatherCurrent[1:-1].split(',')))
        # ---------------------
        minTemp = pastW[0] - currentW[0]
        maxTemp = pastW[1] - currentW[1]
        print("Відхилення погоди на meteoprog.ua може становити від {} до {} градусів".format(abs(minTemp), abs(maxTemp)))
        print("------------------------------------------------------")

# Вивід информації х sinoptik
sinoptik= Link()
sinoptikLink = sinoptik.poiskpersSin("погода-"+sinoptik.enter_the_inf())
sinoptikRequest = Request(sinoptikLink)
sinoptikResponse = sinoptikRequest.get_html()
sinoptikOutputInf = ContentSinoptik(sinoptikResponse, 'main loaded', "bd2", 'tabsContentInner', 'temperature', 'day-link', 'date', 'month', 'min', 'max')
sinoptikOutputInf.outputInf(sinoptikOutputInf.start_gettingSinoptik())

# Вивід информації з meteoprog
meteorg = Link()
meteorgLink = meteorg.poiskpersMet("weather/"+meteorg.enter_the_inf()+"/")
meteorgRequest = Request(meteorgLink)
meteorgResponse = meteorgRequest.get_html()
meteorgOutputInf = ContentMeteoprog(meteorgResponse, "activeBg", "someDayOffWeek", 'dayoffWeek', 'dayoffMonth', 'from', 'to', "asd", "asds", "asdfg")
meteorgOutputInf.outputInf(meteorgOutputInf.start_gettingMeteoprog())



