import matplotlib
import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


page = 0


def drug_data(page_number):
    url = 'https://avtoelon.uz/uz/avto/chevrolet/?page=' + str(page_number)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    cars = soup.find_all("div", class_=lambda value: value and value.startswith("row list-item"))
    cars_list=[]
    for car in cars:
        try:
            car_detail = {}
            name = car.find("div", class_="a-info-side col-right-list").find("span", class_="a-el-info-title").text
            car_name = name.split(",")[0]
            car_detail["name"] = car_name
            url = "https://avtoelon.uz"
            button_url = car.button["data-url"]
            car_url = url+button_url
            car_page = requests.get(car_url)
            soup = BeautifulSoup(car_page.content, 'html.parser')
            table = soup.find("dl")
            table_keys = table.find_all("dt")
            table_values = table.find_all("dd")
            for key, value in zip(table_keys, table_values):
                car_detail[key.text.strip()]=value.text.strip()
            cars_list.append(car_detail)
        except:
            pass
    cars_df = pd.DataFrame(cars_list)
    cars_df.to_csv("cars_df.csv", index=False)


while True:
    try:
        page += 1
        drug_data(page)
    except Exception as ex:
        print(ex)
        print("probably last page:", page)
        break
    print(page)
# print(page_title)
