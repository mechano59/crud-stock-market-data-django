from django.shortcuts import render
from market_app.models import JSONData
from .forms import JSONDataForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import JSONData

def json_data_list(request):
    data = JSONData.objects.all()
    return render(request, 'market_app/json_data_list.html', {'data': data})

def create_json_data(request):
    if request.method == 'POST':
        form = JSONDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('market_app:json_data_list')
    else:
        form = JSONDataForm()
    return render(request, 'market_app/create_json_data.html', {'form': form})

def update_json_data(request, pk):
    data = get_object_or_404(JSONData, pk=pk)
    if request.method == 'POST':
        form = JSONDataForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('market_app:json_data_list')
    else:
        form = JSONDataForm(instance=data)
    return render(request, 'market_app/update_json_data.html', {'form': form, 'data': data})

def delete_json_data(request, pk):
    data = get_object_or_404(JSONData, pk=pk)
    if request.method == 'POST':
        data.delete()
        return redirect('market_app:json_data_list')
    return render(request, 'market_app/delete_json_data.html', {'data': data})