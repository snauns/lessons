from datetime import datetime,timedelta

import requests

from bs4 import BeautifulSoup

from dbcontext import DBContext

context = DBContext("kyiv_temperature.sl3", 5.0)

context.Query("CREATE TABLE kyiv_temperature(id INT PRIMARY KEY, date VARCHAR(20), temperature INT)")

url = 'https://sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%BA%D0%B8%D0%B5%D0%B2/10-%D0%B4%D0%BD%D0%B5%D0%B9'
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

for i in range(1,11):
    temperature_info_html = soup.select_one(f"#bd{i} div.max span")
    temperature = temperature_info_html.text.strip("°+-")
    current_date = datetime.now()
    current_date = current_date + timedelta(days=i-1)
    context.Query(f"INSERT INTO kyiv_temperature(id, date, temperature) values({i}, '{current_date.date()}', {temperature})")