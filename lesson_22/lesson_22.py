import requests
from datetime import datetime


class Bank:
    def __init__(self):
        self.url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"

    def get_data(self):
        response = requests.get(self.url)
        return response.json()

    def exchanges(self, data):
        exchanges_list = []
        for index, currency in enumerate(data, 1):
            exchanges_list.append(f"{index}. {currency['cc']} to UAH: {currency['rate']}\n")
        return exchanges_list

    def save_data(self, data, filename):
        exchanges_list = self.exchanges(data)
        with open(filename, 'w') as file:
            file.write(f"Дата создания запроса: {datetime.now()}\n\n")
            file.writelines(exchanges_list)


currency_pareser = Bank()
exchange_rates_data = currency_pareser.get_data()
currency_pareser.save_data(exchange_rates_data, 'text.txt')
