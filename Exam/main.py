from datetime import datetime

import requests

from dbcontext import DBContext

from bs4 import BeautifulSoup

from parsehtml import ParserHTLM

context = DBContext("exam_table.sl3", 5.0)

context.Query("CREATE TABLE links(id INT PRIMARY KEY, link VARCHAR(100), name VARCHAR(20))")
context.Query("CREATE TABLE money(id INT PRIMARY KEY, currency FLOAT, hrn FLOAT, result FLOAT)")
context.Query("CREATE TABLE weather(id INT PRIMARY KEY, date DATETIME,result VARCHAR(100))")

context.Query('INSERT INTO links(id, link, name) VALUES ("https://bank.gov.ua/", "bank")')


choice = int(input("Купівля валюти у NBU - 1\nдізнатися про температуру повітря у Києві - 2\nваш вибір - "))

if choice == 1:
    selectedCurrency = int(input("Оберіть валюту: \n[EU - 1]\n[USD - 2]: "))
    amount = float(input("Введіть суму гривень: "))
    parser = ParserHTLM("https://bank.gov.ua/")
    isUSD = True
    symbol = "$"
    if selectedCurrency == 1:
        isUSD = False
        symbol = "€"
    parser.ParseNBU('value-full', 'small', isUSD)
    result = amount / parser.Result[0]
    context.Query(f"INSERT INTO money(id, currency, hrn, result) VALUES ( {amount}, '{parser.Result[0]}',  {result})")
    print(f"сума - {amount} hrn\n"
          f"ціна - {parser.Result[0]} {symbol}\n"
          f"результат - {result:.2f} {symbol}")
else:
    url = 'https://sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%BA%D0%B8%D0%B5%D0%B2/10-%D0%B4%D0%BD%D0%B5%D0%B9'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    temperature_info_html = soup.select_one(f"#bd1 div.max span")
    temperature = temperature_info_html.text.strip("°+-")
    current_date = datetime.now()
    print(temperature)
    print(current_date)
    context.Query(f"INSERT INTO weather(id, date, result) values('{current_date.date()}', '{temperature}')")