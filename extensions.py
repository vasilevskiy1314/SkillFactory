import requests
import json
from config import keys


class ConvertionException(Exception):
    pass


class CurrencyConvertor:
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        if quote == base:
            raise ConvertionException(f'Нельзя конвертировать валюту саму в себя')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f"Не удалось обработать валюту '{quote}'")

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f"Не удалось обработать валюту '{base}'")

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f"Значение '{amount}' не является числом")

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        cost = float(json.loads(r.content)[keys[base]]) * float(amount)

        return cost


