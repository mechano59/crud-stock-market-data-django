import json
import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stock_market.settings')

django.setup()

from market_app.models import JSONData

json_file_path = os.path.abspath('/home/mechano/devel_codes/django/stock_market/stock_market_data.json')

# Open and read the JSON file
with open(json_file_path, 'r') as json_file:
    data = json.load(json_file)
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