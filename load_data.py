import os
import json
import django

# Set up Django's environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stock_market.settings')
django.setup()

from market_app.models import JSONData

def load_stock_data():
    with open('/home/mechano/devel_codes/django/stock_market/stock_market_data.json') as file:
        data = json.load(file)
        for entry in data:
            JSONData.objects.create(
            date=entry['date'],
            trade_code=entry['trade_code'],
            high=float(entry['high'].replace(',', '')),
            low=float(entry['low'].replace(',', '')),
            open=float(entry['open'].replace(',', '')),
            close=float(entry['close'].replace(',', '')),
            volume=int(entry['volume'].replace(',', ''))
            )

if __name__ == "__main__":
    load_stock_data()
