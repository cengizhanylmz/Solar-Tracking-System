import requests
import datetime
import math
import time
from bs4 import BeautifulSoup
while True:
    a = datetime.datetime.now()

    if a.month == 1:
        total_day = a.day
    elif a.month == 2:
        total_day = a.day + 31
    elif a.month == 3:
        total_day = a.day + 59
    elif a.month == 4:
        total_day = a.day + 90
    elif a.month == 5:
        total_day = a.day + 120
    elif a.month == 6:
        total_day = a.day + 151
    elif a.month == 7:
        total_day = a.day + 181
    elif a.month == 8:
        total_day = a.day + 212
    elif a.month == 9:
        total_day = a.day + 243
    elif a.month == 10:
        total_day = a.day + 273
    elif a.month == 11:
        total_day = a.day + 304
    elif a.month == 12:
        total_day = a.day + 334
    k = datetime.datetime.now()
    declikasyon = math.radians(23.45 * (math.sin(math.radians(360 * (284 + total_day) / 365))))
    enlem_acisi = math.radians(39)
    print(" ")
    GBD = (math.acos((-math.tan(declikasyon) * math.tan(enlem_acisi))))

    B = math.radians(360 * (total_day - 81) / 365)

    E = 9.87 * math.sin(2 * B) - 7.53 * math.cos(B) - 1.5 * math.sin(B)

    GBS = math.degrees(GBD) / 15

    fark = (3 - (E - 4 * (-33)) / 60) * 60

    t1 = datetime.datetime.strptime('12:00', '%H:%M')
    minutes = GBS * 60
    td = t1 - datetime.timedelta(minutes=minutes)

    tb = t1 + datetime.timedelta(minutes=minutes)

    günes_dogus = td + datetime.timedelta(minutes=fark)

    saat_farkı = tb + datetime.timedelta(minutes=fark)

    azimuth_list = [0]
    altitude_list = [0]

    while (k.hour >= günes_dogus.hour) and k.hour <= saat_farkı.hour:
        url = "https://www.timeanddate.com/sun/turkey/ankara?month=4&year=2020"
        try:
            request = requests.get(url, timeout=4)
            print("Connected to the Internet")

            url = "https://www.timeanddate.com/sun/turkey/ankara?month=4&year=2020"
            response = requests.get(url)

            html_icerigi = response.content

            soup = BeautifulSoup(html_icerigi, "html.parser")

            azimuth = soup.find_all("td", {"id": "sunaz"})

            altitude = soup.find_all("td", {"id": "sunalt"})

            for i in azimuth:
                i = i.text
                azimuth_list.insert(0, i[2:5])

            for j in altitude:
                j = j.text
                altitude_list.insert(0, j[0:2])

            horizontal_movement = int(azimuth_list[0]) - int(azimuth_list[1])
            vertical_movement = int(altitude_list[0]) - int(altitude_list[1])
            print(azimuth_list)
            print(altitude_list)
            print(horizontal_movement)
            print(vertical_movement)
            time.sleep(1200)

        except (requests.ConnectionError, requests.Timeout) as exception:
            print("No internet connection.")
            now = datetime.datetime.now()

            time_now=now.strftime("%X")
            HMS = [60 * 60, 60, 1]
            dec_time = sum(a * b for a, b in zip(HMS, map(int, time_now.split(":"))))
            dec_time /= 3600.
            print(dec_time)

            saat_açısı = math.radians(15 * (dec_time - 12))

            günes_yükseklik_acısı = (math.asin(math.cos(declikasyon) * math.cos(enlem_acisi) * math.cos(saat_açısı) + math.sin(declikasyon) * math.sin(enlem_acisi)))

            azimut = math.degrees(math.asin(math.cos(declikasyon) * math.sin(saat_açısı) / math.cos(günes_yükseklik_acısı)))

            if k.hour < 12 or k.hour >= 12:
                azimut += 180

            zenit_acisi = math.degrees(günes_yükseklik_acısı)
            dikey_aci = round(abs(zenit_acisi - altitude_list[0]))
            yatay_aci = round(abs(azimut - azimuth_list[0]))
          

            altitude_list.insert(0, zenit_acisi)
            azimuth_list.insert(0, azimut)
            print(dikey_aci)
            print(yatay_aci)
            time.sleep(20)







