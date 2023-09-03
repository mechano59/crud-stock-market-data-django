from django.shortcuts import render
from .models import JSONData

def stock_data_table(request):
    stock_data = JSONData.objects.all()
    return render(request, 'market_app/stock_data_table.html', {'stock_data': stock_data})
